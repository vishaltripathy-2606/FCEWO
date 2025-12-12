@echo off
REM Simple runner for FCEWO - Windows

echo ========================================
echo FCEWO - Financial Crisis Early Warning
echo ========================================
echo.

REM Check if .env exists
if not exist .env (
    echo [INFO] Creating .env with safe port assignments...
    python create_env_safe.py
    echo.
    echo Note: System can run without Supabase (limited features)
    echo.
    pause
)

REM Check if dependencies are installed
python -c "import yfinance, streamlit" 2>nul
if errorlevel 1 (
    echo [WARN] Dependencies not installed!
    echo.
    set /p install="Install dependencies now? (y/n): "
    if /i "%install%"=="y" (
        call install_dependencies.bat
    ) else (
        echo [ERROR] Cannot continue without dependencies
        pause
        exit /b 1
    )
)

REM Check ports first
echo [INFO] Checking port availability...
python check_ports.py
echo.
echo Press any key to continue or Ctrl+C to exit...
pause >nul

REM Test setup first
echo [INFO] Testing setup...
python test_setup.py
echo.
echo Press any key to continue or Ctrl+C to exit...
pause >nul

REM Ask how to run
echo.
echo How would you like to run?
echo 1. Docker (recommended)
echo 2. Local development
echo.
set /p choice="Enter choice (1 or 2): "

if "%choice%"=="1" (
    echo.
    echo [INFO] Starting with Docker...
    docker-compose up --build
) else if "%choice%"=="2" (
    echo.
    echo [INFO] Starting local development...
    python run_local.py
) else (
    echo [ERROR] Invalid choice
    pause
    exit /b 1
)

