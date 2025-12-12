@echo off
REM FCEWO Startup Script for Windows

echo 🚀 Starting Financial Crisis Early-Warning Orchestrator...

REM Check if .env file exists
if not exist .env (
    echo ⚠️  .env file not found. Please copy env.example to .env and configure it.
    exit /b 1
)

REM Start Docker Compose
echo 📦 Starting Docker containers...
docker-compose up --build -d

echo ✅ Services started!
echo.
echo 📍 Access points:
echo    - Frontend: http://localhost:8501
echo    - API: http://localhost:8000
echo    - API Docs: http://localhost:8000/docs
echo    - Prometheus: http://localhost:9091
echo    - Grafana: http://localhost:3000 (admin/admin)
echo.
echo To view logs: docker-compose logs -f
echo To stop: docker-compose down

pause

