@echo off
REM Fix port conflicts automatically

echo ========================================
echo FCEWO - Port Conflict Fixer
echo ========================================
echo.

echo [INFO] Checking for port conflicts...
python create_env_safe.py

echo.
echo [INFO] If you want to manually change ports, edit .env file:
echo   API_PORT=8001
echo   FRONTEND_PORT=8502
echo   PROMETHEUS_PORT=9092
echo   GRAFANA_PORT=3001
echo.
echo [INFO] To find what's using a port:
echo   python find_port_usage.bat
echo.
pause

