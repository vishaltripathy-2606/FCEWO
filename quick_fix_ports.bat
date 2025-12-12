@echo off
REM Quick fix for port conflicts - updates .env file

echo [INFO] Fixing port conflicts in .env file...

REM Update API port to 8001 if 8000 is in use
powershell -Command "(Get-Content .env) -replace 'API_PORT=8000', 'API_PORT=8001' | Set-Content .env" 2>nul
if errorlevel 1 (
    REM Fallback for systems without PowerShell
    echo API_PORT=8001 > temp_env.txt
    findstr /V "API_PORT=" .env >> temp_env.txt
    move /Y temp_env.txt .env
)

REM Update Grafana port to 3001 if 3000 is in use  
powershell -Command "(Get-Content .env) -replace 'GRAFANA_PORT=3000', 'GRAFANA_PORT=3001' | Set-Content .env" 2>nul
if errorlevel 1 (
    echo GRAFANA_PORT=3001 >> .env
)

echo [OK] Updated .env file with alternative ports:
echo   API_PORT=8001
echo   GRAFANA_PORT=3001 (if needed)
echo.
echo [INFO] New access URLs:
echo   - API: http://localhost:8001
echo   - Frontend: http://localhost:8501
echo   - Prometheus: http://localhost:9091
echo   - Grafana: http://localhost:3001
echo.
echo [INFO] You can now run: docker-compose up --build
echo.
pause

