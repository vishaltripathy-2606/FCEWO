@echo off
REM Find what's using a specific port on Windows

echo [INFO] Finding what's using port 8000...
echo.

netstat -ano | findstr :8000

echo.
echo [INFO] To kill a process, use:
echo taskkill /PID <PID> /F
echo.
echo Or change the port in .env file:
echo API_PORT=8001
echo.
pause

