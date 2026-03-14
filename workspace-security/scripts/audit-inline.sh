#!/bin/bash
# Inline security audit - no approval needed for these system commands

echo "=== OUTBOUND TCP CONNECTIONS ==="
OUTBOUND=$(lsof -i TCP -sTCP:ESTABLISHED -n -P 2>/dev/null | grep -v "COMMAND" | grep -v "localhost" | grep -v "127.0.0.1" | grep -v "::1" | awk '{print $1, $9}')
if [ -n "$OUTBOUND" ]; then
    echo "$OUTBOUND"
else
    echo "(No outbound TCP connections found)"
fi

echo ""
echo "=== NON-STANDARD PORT CONNECTIONS ==="
NONSTD=$(echo "$OUTBOUND" | while read proc port; do
  port_num=$(echo "$port" | grep -oE '[0-9]+$' | head -1)
  case "$port_num" in
    80|443|8080|11434|18789|53|123|5223|5228) ;;
    *) echo "$proc -> $port" ;;
  esac
done)
if [ -n "$NONSTD" ]; then
    echo "$NONSTD"
else
    echo "(All connections are on standard ports)"
fi

echo ""
echo "=== LISTENING PORTS (non-standard, excluding 22/80/443/88/5900) ==="
LISTEN=$(netstat -anp tcp 2>/dev/null | grep LISTEN | grep -v "127.0.0.1" | grep -v "::1" | grep -vE ".*\.(22|80|443|88|5900)")
if [ -n "$LISTEN" ]; then
    echo "$LISTEN"
else
    echo "(No non-standard listening ports)"
fi

echo ""
echo "=== FULL LISTENING PORTS ==="
netstat -anp tcp 2>/dev/null | grep LISTEN | grep -v "127.0.0.1" | grep -v "::1"
