@echo off
REM Verify all setup is correct

echo ========================================
echo FCEWO - Setup Verification
echo ========================================
echo.

echo [1/4] Checking Python syntax...
python -m py_compile backend/main.py 2>nul
if errorlevel 1 (
    echo   [FAIL] Backend has syntax errors
) else (
    echo   [OK] Backend syntax is valid
)

python -m py_compile frontend/app.py 2>nul
if errorlevel 1 (
    echo   [FAIL] Frontend has syntax errors
) else (
    echo   [OK] Frontend syntax is valid
)

echo.
echo [2/4] Checking Docker Compose configuration...
docker-compose config --quiet >nul 2>&1
if errorlevel 1 (
    echo   [FAIL] Docker Compose configuration has errors
    docker-compose config 2>&1 | findstr /i "error"
) else (
    echo   [OK] Docker Compose configuration is valid
)

echo.
echo [3/4] Checking port availability...
python check_ports.py

echo.
echo [4/4] Checking .env file...
if exist .env (
    echo   [OK] .env file exists
    findstr "API_PORT" .env >nul
    if errorlevel 1 (
        echo   [WARN] API_PORT not found in .env
    ) else (
        echo   [OK] API_PORT configured
    )
) else (
    echo   [WARN] .env file not found - run create_env_safe.py
)

echo.
echo ========================================
echo Verification complete!
echo ========================================
echo.
pause

