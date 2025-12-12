@echo off
REM Install dependencies for Windows with better error handling

echo ========================================
echo Installing FCEWO Dependencies (Windows)
echo ========================================
echo.

echo [INFO] Installing packages that don't require compilation first...
pip install --upgrade pip setuptools wheel

echo.
echo [INFO] Installing backend dependencies (without ML packages first)...
pip install fastapi uvicorn pydantic pydantic-settings supabase postgrest yfinance requests python-dotenv prometheus-client python-multipart aiohttp

echo.
echo [INFO] Attempting to install ML packages...
echo [WARN] These may require Visual C++ Build Tools on Windows
pip install scikit-learn joblib
if errorlevel 1 (
    echo [WARN] scikit-learn installation failed - ML features will be limited
    echo [INFO] You can install Visual C++ Build Tools from:
    echo        https://visualstudio.microsoft.com/visual-cpp-build-tools/
)

echo.
echo [INFO] Installing frontend dependencies...
pip install streamlit plotly
if errorlevel 1 (
    echo [ERROR] Failed to install frontend dependencies
    pause
    exit /b 1
)

echo.
echo [INFO] Installing pandas and numpy (may take a while)...
pip install pandas numpy
if errorlevel 1 (
    echo [ERROR] Failed to install pandas/numpy
    echo [INFO] Try installing Visual C++ Build Tools or use Docker instead
    pause
    exit /b 1
)

echo.
echo ========================================
echo [SUCCESS] Dependencies installed!
echo ========================================
echo.
echo [NOTE] If some packages failed, consider using Docker instead:
echo        docker-compose up --build
echo.
pause

