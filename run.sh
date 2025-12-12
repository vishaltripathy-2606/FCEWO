#!/bin/bash
# Simple runner for FCEWO - Linux/Mac

echo "========================================"
echo "FCEWO - Financial Crisis Early Warning"
echo "========================================"
echo ""

# Check if .env exists
if [ ! -f .env ]; then
    echo "[INFO] Creating .env with safe port assignments..."
    python3 create_env_safe.py
    echo ""
    echo "Note: System can run without Supabase (limited features)"
    echo ""
    read -p "Press Enter to continue..."
fi

# Check if dependencies are installed
python3 -c "import yfinance, streamlit" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "[WARN] Dependencies not installed!"
    echo ""
    read -p "Install dependencies now? (y/n): " install
    if [ "$install" == "y" ]; then
        chmod +x install_dependencies.sh
        ./install_dependencies.sh
    else
        echo "[ERROR] Cannot continue without dependencies"
        exit 1
    fi
fi

# Check ports first
echo "[INFO] Checking port availability..."
python3 check_ports.py
echo ""
read -p "Press Enter to continue or Ctrl+C to exit..."

# Test setup first
echo "[INFO] Testing setup..."
python3 test_setup.py
echo ""
read -p "Press Enter to continue or Ctrl+C to exit..."

# Ask how to run
echo ""
echo "How would you like to run?"
echo "1. Docker (recommended)"
echo "2. Local development"
echo ""
read -p "Enter choice (1 or 2): " choice

if [ "$choice" == "1" ]; then
    echo ""
    echo "[INFO] Starting with Docker..."
    docker-compose up --build
elif [ "$choice" == "2" ]; then
    echo ""
    echo "[INFO] Starting local development..."
    python3 run_local.py
else
    echo "[ERROR] Invalid choice"
    exit 1
fi

