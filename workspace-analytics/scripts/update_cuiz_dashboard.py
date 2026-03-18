#!/usr/bin/env python3
import json
import math
import os
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from statistics import mean
from zoneinfo import ZoneInfo

WORKSPACE = Path('/Users/openclaw/.openclaw/workspace-analytics')
OUT_HTML = WORKSPACE / 'dashboard' / 'cuiz-ai.html'
OUT_JSON = WORKSPACE / 'dashboard' / 'cuiz-ai.json'
PROJECT_ID = '62966'
PROJECT_NAME = 'Cuiz AI'
TZ = ZoneInfo('Europe/London')


def run_posthog(args, expect_json=True):
    env = os.environ.copy()
    env['POSTHOG_PROJECT_ID'] = PROJECT_ID
    cmd = ['posthog'] + args
    proc = subprocess.run(cmd, capture_output=True, text=True, env=env)
    if proc.returncode != 0:
        raise RuntimeError(f"Command failed: {' '.join(cmd)}\nSTDOUT:\n{proc.stdout}\nSTDERR:\n{proc.stderr}")
    text = proc.stdout.strip()
    if expect_json:
        return json.loads(text)
    return text


def pct_change(current, previous):
    if previous in (None, 0):
        return None
    return ((current - previous) / previous) * 100


def fmt_int(n):
    return f"{int(n):,}"


def fmt_pct(n):
    if n is None or (isinstance(n, float) and (math.isinf(n) or math.isnan(n))):
        return '—'
    sign = '+' if n > 0 else ''
    return f"{sign}{n:.1f}%"


def fmt_money(n, currency='GBP', decimals=0):
    symbols = {'GBP': '£', 'USD': '$', 'EUR': '€'}
    symbol = symbols.get((currency or 'GBP').upper(), f"{currency.upper()} ")
    if decimals == 0:
        return f"{symbol}{n:,.0f}"
    return f"{symbol}{n:,.{decimals}f}"


def fmt_dt(ts):
    return datetime.now(TZ).strftime('%Y-%m-%d %H:%M %Z')


def top_dict(pairs, limit=10):
    return [{'label': k, 'value': v} for k, v in pairs[:limit]]


def get_summary():
    return run_posthog(['--json', 'activity', 'summary', '--date-from', '-90d'])


def get_query(hogql):
    data = run_posthog(['--json', 'query', 'run', '--hogql', hogql])
    return data['results']


def classify(change, bad_threshold=-25, warn_threshold=-10):
    if change is None:
        return 'neutral'
    if change <= bad_threshold:
        return 'bad'
    if change <= warn_threshold:
        return 'warn'
    if change > 10:
        return 'good'
    return 'neutral'


def build_assessment(metrics):
    score = 0
    flags = []

    wau_change = metrics['wau_change']
    uploads_change = metrics['file_upload_users_change']
    quiz_change = metrics['quiz_generated_users_change']
    checkout_rate = metrics['checkout_rate']
    completion_rate = metrics['quiz_completion_rate']

    if wau_change is not None:
        if wau_change <= -40:
            score -= 3
            flags.append('active users are falling sharply')
        elif wau_change <= -15:
            score -= 2
        elif wau_change > 10:
            score += 1

    if uploads_change is not None:
        if uploads_change <= -30:
            score -= 2
            flags.append('core usage is shrinking')
        elif uploads_change > 10:
            score += 1

    if quiz_change is not None:
        if quiz_change <= -30:
            score -= 2
        elif quiz_change > 10:
            score += 1

    if completion_rate < 0.3:
        score -= 2
        flags.append('too few generated quizzes are being completed')
    elif completion_rate > 0.5:
        score += 1

    if checkout_rate < 0.05:
        score -= 2
        flags.append('monetization is weak relative to product usage')
    elif checkout_rate > 0.12:
        score += 1

    if score <= -5:
        label = 'Needs attention'
    elif score <= -2:
        label = 'Mixed / softening'
    elif score <= 1:
        label = 'Stable'
    else:
        label = 'Healthy'

    if not flags:
        flags.append('no severe structural issue stands out from the headline metrics')

    return label, flags


def build_summary_text(metrics, assessment):
    parts = []
    wau_change = fmt_pct(metrics['wau_change'])
    upload_change = fmt_pct(metrics['file_upload_users_change'])
    quiz_change = fmt_pct(metrics['quiz_generated_users_change'])
    parts.append(f"Cuiz AI is currently **{assessment.lower()}**.")
    parts.append(
        f"Weekly active users are **{fmt_int(metrics['wau_current'])}** ({wau_change} vs previous week), "
        f"file upload users are **{fmt_int(metrics['file_upload_users_current'])}** ({upload_change}), "
        f"and quiz generation users are **{fmt_int(metrics['quiz_generated_users_current'])}** ({quiz_change})."
    )
    parts.append(
        f"The biggest operational question is whether traffic/acquisition has cooled down permanently or whether the recent drop is a temporary lull."
    )
    return ' '.join(parts)


def generate():
    summary = get_summary()

    weekly_rows = get_query("""
        SELECT toStartOfWeek(timestamp) AS week, event, count() AS events, count(distinct person_id) AS users
        FROM events
        WHERE timestamp > now() - interval 90 day
          AND event IN ('file_upload','quiz_generated','quiz_completed','user_logged_in','purchase','begin_checkout')
        GROUP BY week, event
        ORDER BY week, event
    """)

    pageview_rows = get_query("""
        SELECT toStartOfWeek(timestamp) AS week, count(distinct person_id) AS users
        FROM events
        WHERE timestamp > now() - interval 90 day
          AND event = '$pageview'
        GROUP BY week
        ORDER BY week
    """)

    revenue_rows = get_query("""
        SELECT toStartOfWeek(timestamp) AS week, event, count(distinct person_id) AS users,
               sum(ifNull(properties.value, 0)) AS value_sum,
               sum(ifNull(properties.amount, 0)) AS amount_sum
        FROM events
        WHERE timestamp > now() - interval 90 day
          AND event IN ('purchase','subscription_renewed','begin_checkout')
        GROUP BY week, event
        ORDER BY week, event
    """)

    weekly = {}
    for week, event, events, users in weekly_rows:
        weekly.setdefault(week, {})[event] = {'events': events, 'users': users}
    for week, users in pageview_rows:
        weekly.setdefault(week, {})['$pageview'] = {'events': None, 'users': users}
    for week, event, users, value_sum, amount_sum in revenue_rows:
        weekly.setdefault(week, {})[event] = {
            **weekly.setdefault(week, {}).get(event, {}),
            'users': users,
            'value_sum': value_sum or 0,
            'amount_sum': amount_sum or 0,
        }

    weeks = sorted(weekly.keys())

    now_local = datetime.now(TZ)
    # Match PostHog's observed week buckets here (Sunday-start weeks).
    days_since_sunday = (now_local.weekday() + 1) % 7
    current_week_start = now_local.date().fromordinal(now_local.date().toordinal() - days_since_sunday)
    complete_weeks = [w for w in weeks if datetime.fromisoformat(str(w)).date() < current_week_start]
    report_weeks = complete_weeks if len(complete_weeks) >= 2 else weeks

    latest_week = report_weeks[-1]
    prev_week = report_weeks[-2] if len(report_weeks) > 1 else None

    def get_week_metric(week, event, field='users'):
        if not week:
            return 0
        return weekly.get(week, {}).get(event, {}).get(field, 0) or 0

    metrics = {
        'wau_current': get_week_metric(latest_week, '$pageview', 'users'),
        'wau_previous': get_week_metric(prev_week, '$pageview', 'users'),
        'file_upload_users_current': get_week_metric(latest_week, 'file_upload', 'users'),
        'file_upload_users_previous': get_week_metric(prev_week, 'file_upload', 'users'),
        'quiz_generated_users_current': get_week_metric(latest_week, 'quiz_generated', 'users'),
        'quiz_generated_users_previous': get_week_metric(prev_week, 'quiz_generated', 'users'),
        'quiz_completed_users_current': get_week_metric(latest_week, 'quiz_completed', 'users'),
        'quiz_completed_users_previous': get_week_metric(prev_week, 'quiz_completed', 'users'),
        'logins_current': get_week_metric(latest_week, 'user_logged_in', 'users'),
        'logins_previous': get_week_metric(prev_week, 'user_logged_in', 'users'),
        'checkouts_current': get_week_metric(latest_week, 'begin_checkout', 'users'),
        'purchases_current': get_week_metric(latest_week, 'purchase', 'users'),
        'new_revenue_current': get_week_metric(latest_week, 'purchase', 'value_sum'),
        'new_revenue_previous': get_week_metric(prev_week, 'purchase', 'value_sum'),
        'renewal_revenue_current': get_week_metric(latest_week, 'subscription_renewed', 'value_sum'),
        'renewal_revenue_previous': get_week_metric(prev_week, 'subscription_renewed', 'value_sum'),
        'checkout_value_current': get_week_metric(latest_week, 'begin_checkout', 'amount_sum'),
        'checkout_value_previous': get_week_metric(prev_week, 'begin_checkout', 'amount_sum'),
    }
    metrics['wau_change'] = pct_change(metrics['wau_current'], metrics['wau_previous'])
    metrics['file_upload_users_change'] = pct_change(metrics['file_upload_users_current'], metrics['file_upload_users_previous'])
    metrics['quiz_generated_users_change'] = pct_change(metrics['quiz_generated_users_current'], metrics['quiz_generated_users_previous'])
    metrics['quiz_completed_users_change'] = pct_change(metrics['quiz_completed_users_current'], metrics['quiz_completed_users_previous'])
    metrics['new_revenue_change'] = pct_change(metrics['new_revenue_current'], metrics['new_revenue_previous'])
    metrics['renewal_revenue_change'] = pct_change(metrics['renewal_revenue_current'], metrics['renewal_revenue_previous'])
    metrics['checkout_value_change'] = pct_change(metrics['checkout_value_current'], metrics['checkout_value_previous'])
    metrics['total_revenue_current'] = metrics['new_revenue_current'] + metrics['renewal_revenue_current']
    metrics['total_revenue_previous'] = metrics['new_revenue_previous'] + metrics['renewal_revenue_previous']
    metrics['total_revenue_change'] = pct_change(metrics['total_revenue_current'], metrics['total_revenue_previous'])
    metrics['quiz_completion_rate'] = (
        metrics['quiz_completed_users_current'] / metrics['quiz_generated_users_current']
        if metrics['quiz_generated_users_current'] else 0
    )
    metrics['checkout_rate'] = (
        metrics['checkouts_current'] / metrics['quiz_generated_users_current']
        if metrics['quiz_generated_users_current'] else 0
    )
    metrics['purchase_rate'] = (
        metrics['purchases_current'] / metrics['checkouts_current']
        if metrics['checkouts_current'] else 0
    )

    assessment, issues = build_assessment(metrics)
    summary_text = build_summary_text(metrics, assessment)
    currency = 'GBP'

    top_pages = top_dict(summary['top_pages'], 8)
    traffic_sources = top_dict(summary['traffic_sources'], 8)

    recommendations = []
    if metrics['wau_change'] is not None and metrics['wau_change'] <= -20:
        recommendations.append('Acquisition: identify what drove the February spike and whether that channel has gone quiet.')
    if metrics['quiz_completion_rate'] < 0.3:
        recommendations.append('Activation: inspect the drop from quiz generated to quiz completed; this is the clearest product funnel leak.')
    if metrics['checkout_rate'] < 0.05:
        recommendations.append('Monetization: the pricing/paywall path is underperforming relative to product usage; review offer timing and pricing page exposure.')
    if not recommendations:
        recommendations.append('Keep monitoring week-over-week changes and validate that the current event set still reflects the real user journey.')

    chart_source_weeks = report_weeks[-8:] if len(report_weeks) >= 2 else weeks[-8:]
    chart_weeks = [str(w) for w in chart_source_weeks]
    series = {
        'wau': [get_week_metric(w, '$pageview', 'users') for w in chart_source_weeks],
        'uploads': [get_week_metric(w, 'file_upload', 'users') for w in chart_source_weeks],
        'quizGenerated': [get_week_metric(w, 'quiz_generated', 'users') for w in chart_source_weeks],
        'quizCompleted': [get_week_metric(w, 'quiz_completed', 'users') for w in chart_source_weeks],
        'checkouts': [get_week_metric(w, 'begin_checkout', 'users') for w in chart_source_weeks],
        'purchases': [get_week_metric(w, 'purchase', 'users') for w in chart_source_weeks],
        'revenue': [get_week_metric(w, 'purchase', 'value_sum') + get_week_metric(w, 'subscription_renewed', 'value_sum') for w in chart_source_weeks],
    }

    payload = {
        'project': PROJECT_NAME,
        'project_id': PROJECT_ID,
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'generated_at_local': fmt_dt(None),
        'latest_week': str(latest_week),
        'previous_week': str(prev_week) if prev_week else None,
        'metrics': metrics,
        'assessment': assessment,
        'summary_text': summary_text,
        'recommendations': recommendations,
        'issues': issues,
        'top_pages': top_pages,
        'traffic_sources': traffic_sources,
        'top_events': top_dict(summary['top_events'], 10),
        'custom_events': [
            {'label': label, 'events': events, 'users': users}
            for label, events, users in summary['custom_events'][:10]
        ],
        'charts': {
            'weeks': chart_weeks,
            'series': series,
        },
    }

    OUT_JSON.write_text(json.dumps(payload, indent=2))

    def metric_card(title, value, delta, hint, tone=None):
        tone = tone or classify(delta)
        return f'''
        <div class="card metric {tone}">
          <div class="label">{title}</div>
          <div class="value">{value}</div>
          <div class="delta">{fmt_pct(delta)}</div>
          <div class="hint">{hint}</div>
        </div>
        '''

    def rows(items, value_key='value'):
        html = []
        for item in items:
            val = item[value_key]
            html.append(f"<tr><td>{item['label']}</td><td class='num'>{fmt_int(val)}</td></tr>")
        return '\n'.join(html)

    html = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Cuiz AI Dashboard</title>
  <style>
    :root {{
      --bg: #0b1020;
      --panel: #131a2e;
      --muted: #91a0c0;
      --text: #eef3ff;
      --good: #1f9d68;
      --warn: #d19a00;
      --bad: #cf4b64;
      --line1: #6ea8fe;
      --line2: #63e6be;
      --line3: #f7b955;
      --line4: #ff7b72;
      --line5: #c77dff;
      --border: rgba(255,255,255,.08);
    }}
    * {{ box-sizing: border-box; }}
    body {{ margin: 0; font-family: Inter, ui-sans-serif, system-ui, -apple-system, sans-serif; background: linear-gradient(180deg, #0b1020, #0f1630 35%, #0a1122); color: var(--text); }}
    .wrap {{ max-width: 1280px; margin: 0 auto; padding: 28px; }}
    .header {{ display:flex; justify-content:space-between; gap:16px; align-items:flex-end; flex-wrap:wrap; margin-bottom: 22px; }}
    h1 {{ margin:0; font-size: 34px; }}
    .sub {{ color: var(--muted); font-size: 14px; line-height: 1.5; }}
    .grid {{ display:grid; gap:16px; }}
    .metrics {{ grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); margin-bottom: 16px; }}
    .cols {{ grid-template-columns: 1.3fr .9fr; align-items:start; }}
    .bottom {{ grid-template-columns: 1fr 1fr; align-items:start; }}
    .card {{ background: rgba(19,26,46,.92); border: 1px solid var(--border); border-radius: 18px; padding: 18px; box-shadow: 0 8px 28px rgba(0,0,0,.2); }}
    .metric .label {{ color: var(--muted); font-size: 12px; text-transform: uppercase; letter-spacing: .08em; }}
    .metric .value {{ font-size: 34px; font-weight: 700; margin-top: 8px; }}
    .metric .delta {{ margin-top: 8px; font-size: 14px; font-weight: 700; }}
    .metric.good .delta {{ color: #70e1a1; }}
    .metric.warn .delta {{ color: #ffd166; }}
    .metric.bad .delta {{ color: #ff8fa3; }}
    .metric.neutral .delta {{ color: var(--muted); }}
    .metric .hint {{ color: var(--muted); font-size: 13px; margin-top: 6px; }}
    h2 {{ margin: 0 0 14px; font-size: 18px; }}
    p {{ margin: 0; line-height: 1.6; }}
    ul {{ margin: 0; padding-left: 18px; color: var(--text); line-height: 1.7; }}
    .pill {{ display:inline-block; padding: 6px 10px; border-radius: 999px; font-size: 12px; font-weight: 700; border:1px solid var(--border); background: rgba(255,255,255,.04); margin-bottom: 12px; }}
    .pill.bad {{ color: #ff9fb0; }} .pill.warn {{ color: #ffd166; }} .pill.good {{ color: #70e1a1; }} .pill.neutral {{ color: #c2cbe2; }}
    .chart {{ width:100%; height:320px; }}
    table {{ width:100%; border-collapse: collapse; }}
    th, td {{ padding: 10px 0; border-bottom: 1px solid rgba(255,255,255,.06); font-size: 14px; }}
    th {{ color: var(--muted); text-align:left; font-weight:600; }}
    .num {{ text-align:right; font-variant-numeric: tabular-nums; }}
    .small {{ color: var(--muted); font-size: 13px; }}
    .kpis {{ display:grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 12px; margin-top: 14px; }}
    .mini {{ padding: 14px; border-radius: 14px; background: rgba(255,255,255,.03); border:1px solid rgba(255,255,255,.05); }}
    .mini .t {{ color: var(--muted); font-size:12px; text-transform:uppercase; letter-spacing:.08em; }}
    .mini .v {{ margin-top: 6px; font-size: 22px; font-weight: 700; }}
    @media (max-width: 980px) {{ .cols, .bottom {{ grid-template-columns: 1fr; }} .kpis {{ grid-template-columns: 1fr; }} }}
  </style>
</head>
<body>
  <div class="wrap">
    <div class="header">
      <div>
        <h1>Cuiz AI dashboard</h1>
        <div class="sub">Weekly snapshot for the metrics that matter. Updated: {payload['generated_at_local']} · Latest completed week: {payload['latest_week']}</div>
      </div>
      <div class="sub">Project ID {PROJECT_ID} · Source: PostHog</div>
    </div>

    <div class="grid metrics">
      {metric_card('Weekly active users', fmt_int(metrics['wau_current']), metrics['wau_change'], 'Distinct users with pageviews this week')}
      {metric_card('Upload users', fmt_int(metrics['file_upload_users_current']), metrics['file_upload_users_change'], 'Users who uploaded content')}
      {metric_card('Quiz generation users', fmt_int(metrics['quiz_generated_users_current']), metrics['quiz_generated_users_change'], 'Users who generated quizzes')}
      {metric_card('Quiz completion users', fmt_int(metrics['quiz_completed_users_current']), metrics['quiz_completed_users_change'], 'Users who completed a quiz')}
      {metric_card('Total revenue', fmt_money(metrics['total_revenue_current'], currency), metrics['total_revenue_change'], 'Purchases + renewals in latest completed week')}
      {metric_card('Checkout value', fmt_money(metrics['checkout_value_current'], currency), metrics['checkout_value_change'], 'Tracked amount on checkout starts')}
    </div>

    <div class="grid cols">
      <div class="card">
        <h2>Main trend</h2>
        <svg id="trendChart" class="chart" viewBox="0 0 900 320" preserveAspectRatio="none"></svg>
        <div class="small">Blue = WAU · Green = Upload users · Yellow = Quiz generation users · Red = Quiz completion users</div>
      </div>
      <div class="card">
        <div class="pill {classify(metrics['wau_change'])}">{assessment}</div>
        <h2>Summary</h2>
        <p>{summary_text}</p>
        <div class="kpis">
          <div class="mini"><div class="t">Quiz completion rate</div><div class="v">{metrics['quiz_completion_rate'] * 100:.1f}%</div></div>
          <div class="mini"><div class="t">Checkout rate</div><div class="v">{metrics['checkout_rate'] * 100:.1f}%</div></div>
          <div class="mini"><div class="t">Purchase / checkout</div><div class="v">{metrics['purchase_rate'] * 100:.1f}%</div></div>
          <div class="mini"><div class="t">New revenue</div><div class="v">{fmt_money(metrics['new_revenue_current'], currency)}</div></div>
          <div class="mini"><div class="t">Renewal revenue</div><div class="v">{fmt_money(metrics['renewal_revenue_current'], currency)}</div></div>
          <div class="mini"><div class="t">Revenue / active user</div><div class="v">{fmt_money((metrics['total_revenue_current'] / metrics['wau_current']) if metrics['wau_current'] else 0, currency, 2)}</div></div>
        </div>
      </div>
    </div>

    <div class="grid bottom" style="margin-top:16px;">
      <div class="card">
        <h2>Main points to improve</h2>
        <ul>{''.join(f'<li>{item}</li>' for item in recommendations)}</ul>
      </div>
      <div class="card">
        <h2>Assessment</h2>
        <ul>{''.join(f'<li>{item}</li>' for item in issues)}</ul>
      </div>
    </div>

    <div class="grid bottom" style="margin-top:16px;">
      <div class="card">
        <h2>Top traffic sources (90d)</h2>
        <table>
          <thead><tr><th>Source</th><th class="num">Users</th></tr></thead>
          <tbody>{rows(traffic_sources)}</tbody>
        </table>
      </div>
      <div class="card">
        <h2>Top pages (90d)</h2>
        <table>
          <thead><tr><th>Page</th><th class="num">Views</th></tr></thead>
          <tbody>{rows(top_pages)}</tbody>
        </table>
      </div>
    </div>
  </div>

  <script>
    const weeks = {json.dumps(chart_weeks)};
    const series = {json.dumps(series)};
    const palette = {{ wau: '#6ea8fe', uploads: '#63e6be', quizGenerated: '#f7b955', quizCompleted: '#ff7b72' }};

    function drawChart() {{
      const svg = document.getElementById('trendChart');
      const width = 900, height = 320;
      const pad = {{ top: 20, right: 16, bottom: 36, left: 42 }};
      const keys = ['wau', 'uploads', 'quizGenerated', 'quizCompleted'];
      const values = keys.flatMap(k => series[k]);
      const max = Math.max(...values, 1);
      const xStep = (width - pad.left - pad.right) / Math.max(weeks.length - 1, 1);
      const y = v => height - pad.bottom - (v / max) * (height - pad.top - pad.bottom);
      const x = i => pad.left + i * xStep;

      const grid = [];
      for (let i = 0; i < 5; i++) {{
        const val = Math.round(max * i / 4);
        const gy = y(val);
        grid.push(`<line x1="${{pad.left}}" y1="${{gy}}" x2="${{width - pad.right}}" y2="${{gy}}" stroke="rgba(255,255,255,.08)" />`);
        grid.push(`<text x="8" y="${{gy + 4}}" fill="rgba(255,255,255,.55)" font-size="11">${{val}}</text>`);
      }}

      const labels = weeks.map((w, i) => `<text x="${{x(i)}}" y="${{height - 12}}" text-anchor="middle" fill="rgba(255,255,255,.55)" font-size="11">${{w.slice(5)}}</text>`);

      const paths = keys.map(key => {{
        const pts = series[key].map((v, i) => `${{x(i)}},${{y(v)}}`).join(' ');
        const dots = series[key].map((v, i) => `<circle cx="${{x(i)}}" cy="${{y(v)}}" r="3.5" fill="${{palette[key]}}" />`).join('');
        return `<polyline fill="none" stroke="${{palette[key]}}" stroke-width="3" points="${{pts}}" stroke-linejoin="round" stroke-linecap="round" />${{dots}}`;
      }}).join('');

      svg.innerHTML = `${{grid.join('')}}${{labels.join('')}}${{paths}}`;
    }}
    drawChart();
  </script>
</body>
</html>
'''

    OUT_HTML.write_text(html)
    print(json.dumps({
        'html': str(OUT_HTML),
        'json': str(OUT_JSON),
        'assessment': assessment,
        'generated_at_local': payload['generated_at_local']
    }, indent=2))


if __name__ == '__main__':
    generate()
