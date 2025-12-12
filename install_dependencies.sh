#!/bin/bash
# Install all Python dependencies for FCEWO

echo "========================================"
echo "Installing FCEWO Dependencies"
echo "========================================"
echo ""

echo "[1/2] Installing backend dependencies..."
pip3 install -r backend/requirements.txt
if [ $? -ne 0 ]; then
    echo "[ERROR] Failed to install backend dependencies"
    exit 1
fi

echo ""
echo "[2/2] Installing frontend dependencies..."
pip3 install -r frontend/requirements.txt
if [ $? -ne 0 ]; then
    echo "[ERROR] Failed to install frontend dependencies"
    exit 1
fi

echo ""
echo "========================================"
echo "[SUCCESS] All dependencies installed!"
echo "========================================"
echo ""

