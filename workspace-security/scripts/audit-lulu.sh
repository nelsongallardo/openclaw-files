#!/bin/bash
# Security Audit Script for Mac mini (Nelson)
# Collects connection data AND investigation context so the agent can self-assess

echo "=== OUTBOUND TCP CONNECTIONS ==="
lsof -i TCP -sTCP:ESTABLISHED -n -P 2>/dev/null | grep -v "COMMAND" | grep -v "localhost" | grep -v "127.0.0.1" | grep -v "::1" | awk '{print $1, $2, $9}'

echo ""
echo "=== NON-STANDARD PORT CONNECTIONS (with process details) ==="
lsof -i TCP -sTCP:ESTABLISHED -n -P 2>/dev/null | grep -v "COMMAND" | grep -v "localhost" | grep -v "127.0.0.1" | grep -v "::1" | awk '{print $1, $2, $9}' | while read proc pid addr; do
  port_num=$(echo "$addr" | grep -oE '[0-9]+$' | head -1)
  case "$port_num" in
    80|443|8080|11434|18789|53|123|5223|5228) ;;
    *)
      echo "--- FLAGGED: $proc (PID $pid) -> $addr ---"
      # Process details
      ps -p "$pid" -o pid,ppid,user,command 2>/dev/null | tail -1
      # What files/ports this PID has open
      lsof -p "$pid" -i -n -P 2>/dev/null | head -10
      echo ""
      ;;
  esac
done

echo ""
echo "=== UNKNOWN IPs (reverse DNS) ==="
# Extract unique remote IPs and resolve them
lsof -i TCP -sTCP:ESTABLISHED -n -P 2>/dev/null | grep -v "COMMAND" | grep -v "localhost" | grep -v "127.0.0.1" | grep -v "::1" | awk '{print $9}' | grep -oE '[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+' | sort -u | while read ip; do
  # Skip well-known ranges (Apple 17.x, Google 142.250/172.217, Cloudflare 162.159, Telegram 149.154, GitHub 140.82, private 10./192.168/100.64)
  case "$ip" in
    17.*|142.250.*|172.217.*|162.159.*|149.154.*|140.82.*|10.*|192.168.*|100.64.*) continue ;;
  esac
  rdns=$(host "$ip" 2>/dev/null | grep "domain name pointer" | head -1 | awk '{print $NF}')
  whois_org=$(whois "$ip" 2>/dev/null | grep -iE "^(OrgName|org-name|Organization):" | head -1 | sed 's/^[^:]*://' | xargs)
  echo "$ip -> rDNS: ${rdns:-none} | Org: ${whois_org:-unknown}"
done

echo ""
echo "=== LISTENING PORTS (with process identification) ==="
# Show all non-localhost listening ports with the process that owns them
lsof -i TCP -sTCP:LISTEN -n -P 2>/dev/null | grep -v "127.0.0.1" | grep -v "::1" | grep -v "localhost" | awk '{print $1, $2, $9}' | sort -u | while read proc pid addr; do
  echo "$proc (PID $pid) listening on $addr"
done

echo ""
echo "=== FULL LISTENING PORTS (raw) ==="
netstat -anp tcp 2>/dev/null | grep LISTEN | grep -v "127.0.0.1" | grep -v "::1"
