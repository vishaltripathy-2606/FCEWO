@echo off
REM Fix port conflicts by checking and suggesting alternatives

echo [INFO] Checking port availability...
python check_ports.py

echo.
echo [INFO] If ports are in use, you can:
echo 1. Edit .env file and change the port numbers
echo 2. Or stop the service using the port
echo.
pause

