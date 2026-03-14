#!/bin/bash
# Security Audit Script for Mac mini (Nelson)

echo "=== OUTBOUND TCP CONNECTIONS ==="
lsof -i TCP -sTCP:ESTABLISHED -n -P 2>/dev/null | grep -v "COMMAND" | grep -v "localhost" | grep -v "127.0.0.1" | grep -v "::1" | awk '{print $1, $9}'

echo ""
echo "=== NON-STANDARD PORT CONNECTIONS ==="
lsof -i TCP -sTCP:ESTABLISHED -n -P 2>/dev/null | grep -v "COMMAND" | grep -v "localhost" | grep -v "127.0.0.1" | grep -v "::1" | awk '{print $1, $9}' | while read proc port; do
  port_num=$(echo "$port" | grep -oE '[0-9]+$' | head -1)
  case "$port_num" in
    80|443|8080|11434|18789|53|123|5223|5228) ;;
    *) echo "$proc -> $port" ;;
  esac
done

echo ""
echo "=== LISTENING PORTS (non-standard) ==="
netstat -anp tcp 2>/dev/null | grep LISTEN | grep -v "127.0.0.1" | grep -v "::1" | grep -vE ".*\.(22|80|443|88|5900)"

echo ""
echo "=== FULL LISTENING PORTS (for context) ==="
netstat -anp tcp 2>/dev/null | grep LISTEN | grep -v "127.0.0.1" | grep -v "::1"
