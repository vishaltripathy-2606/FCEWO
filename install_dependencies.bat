@echo off
REM Install all Python dependencies for FCEWO

echo ========================================
echo Installing FCEWO Dependencies
echo ========================================
echo.

echo [1/2] Installing backend dependencies...
pip install -r backend/requirements.txt
if errorlevel 1 (
    echo [ERROR] Failed to install backend dependencies
    pause
    exit /b 1
)

echo.
echo [2/2] Installing frontend dependencies...
pip install -r frontend/requirements.txt
if errorlevel 1 (
    echo [ERROR] Failed to install frontend dependencies
    pause
    exit /b 1
)

echo.
echo ========================================
echo [SUCCESS] All dependencies installed!
echo ========================================
echo.
pause

