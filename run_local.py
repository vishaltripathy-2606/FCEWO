#!/usr/bin/env python3
"""
Local development runner - runs services without Docker
Useful for development and testing
"""
import subprocess
import sys
import os
import time
from pathlib import Path

def check_env_file():
    """Check if .env file exists"""
    if not Path(".env").exists():
        print("[WARN] .env file not found!")
        print("[INFO] Creating .env from env.example...")
        if Path("env.example").exists():
            with open("env.example", "r") as f:
                content = f.read()
            with open(".env", "w") as f:
                f.write(content)
            print("[OK] Created .env file. Please edit it with your Supabase credentials.")
            return False
        else:
            print("[ERROR] env.example not found!")
            return False
    return True

def install_dependencies():
    """Install Python dependencies"""
    print("[INFO] Installing dependencies...")
    print("  This may take a few minutes...")
    
    # Backend dependencies
    print("  Installing backend dependencies...")
    result = subprocess.run(
        [sys.executable, "-m", "pip", "install", "-r", "backend/requirements.txt"],
        check=False,
        capture_output=True,
        text=True
    )
    if result.returncode != 0:
        print(f"  [WARN] Some backend dependencies may have failed: {result.stderr[:200]}")
    else:
        print("  [OK] Backend dependencies installed")
    
    # Frontend dependencies
    print("  Installing frontend dependencies...")
    result = subprocess.run(
        [sys.executable, "-m", "pip", "install", "-r", "frontend/requirements.txt"],
        check=False,
        capture_output=True,
        text=True
    )
    if result.returncode != 0:
        print(f"  [WARN] Some frontend dependencies may have failed: {result.stderr[:200]}")
    else:
        print("  [OK] Frontend dependencies installed")

def run_backend():
    """Run FastAPI backend"""
    print("[INFO] Starting FastAPI backend...")
    os.chdir("backend")
    subprocess.Popen([sys.executable, "-m", "uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"])
    os.chdir("..")

def run_frontend():
    """Run Streamlit frontend"""
    print("[INFO] Starting Streamlit frontend...")
    os.chdir("frontend")
    os.environ["API_URL"] = "http://localhost:8000"
    subprocess.Popen([sys.executable, "-m", "streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"])
    os.chdir("..")

def main():
    """Main function"""
    print("=" * 60)
    print("Financial Crisis Early-Warning Orchestrator")
    print("Local Development Mode")
    print("=" * 60)
    print()
    
    # Check environment
    if not check_env_file():
        print("\n[WARN] Please configure your .env file before continuing.")
        print("       Note: System can run without Supabase (limited features)")
        response = input("Continue anyway? (y/n): ").lower().strip()
        if response != 'y':
            return
    
    # Check if dependencies are installed
    try:
        import yfinance
        import streamlit
        print("[OK] Dependencies appear to be installed")
    except ImportError as e:
        print(f"[WARN] Missing dependencies: {e}")
        install = input("Install dependencies now? (y/n): ").lower().strip()
        if install == 'y':
            install_dependencies()
        else:
            print("[ERROR] Cannot run without dependencies. Please install them first:")
            print("  Windows: install_dependencies.bat")
            print("  Linux/Mac: ./install_dependencies.sh")
            print("  Or manually: pip install -r backend/requirements.txt && pip install -r frontend/requirements.txt")
            return
    
    print("\n[INFO] Starting services...")
    print("   Backend will be available at: http://localhost:8000")
    print("   Frontend will be available at: http://localhost:8501")
    print("   API Docs: http://localhost:8000/docs")
    print("\n[NOTE] If you see import errors, try:")
    print("   - Using Docker: docker-compose up --build")
    print("   - Or see SOLUTION_WINDOWS.md for help")
    print("\n   Press Ctrl+C to stop all services\n")
    
    try:
        # Start backend
        run_backend()
        time.sleep(3)  # Wait for backend to start
        
        # Start frontend
        run_frontend()
        
        # Keep running
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\n[INFO] Stopping services...")
        print("[OK] Services stopped")

if __name__ == "__main__":
    main()

