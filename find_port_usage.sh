#!/bin/bash
# Find what's using a specific port on Linux/Mac

echo "[INFO] Finding what's using port 8000..."
echo ""

if command -v lsof &> /dev/null; then
    lsof -i :8000
elif command -v netstat &> /dev/null; then
    netstat -tulpn | grep :8000
else
    echo "[ERROR] Neither lsof nor netstat is available"
    exit 1
fi

echo ""
echo "[INFO] To kill a process, use:"
echo "kill -9 <PID>"
echo ""
echo "Or change the port in .env file:"
echo "API_PORT=8001"
echo ""

