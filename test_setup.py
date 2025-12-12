#!/usr/bin/env python3
"""
Test script to verify FCEWO setup
"""
import sys
import os
from pathlib import Path

def test_imports():
    """Test if all required packages can be imported"""
    print("[*] Testing Python package imports...")
    errors = []
    
    try:
        import fastapi
        print("  [OK] fastapi")
    except ImportError as e:
        errors.append(f"fastapi: {e}")
        print(f"  [FAIL] fastapi: {e}")
    
    try:
        import streamlit
        print("  [OK] streamlit")
    except ImportError as e:
        errors.append(f"streamlit: {e}")
        print(f"  [FAIL] streamlit: {e}")
    
    try:
        import supabase
        print("  [OK] supabase")
    except ImportError as e:
        errors.append(f"supabase: {e}")
        print(f"  [FAIL] supabase: {e}")
    
    try:
        import yfinance
        print("  [OK] yfinance")
    except ImportError as e:
        errors.append(f"yfinance: {e}")
        print(f"  [FAIL] yfinance: {e}")
    
    try:
        import sklearn
        print("  [OK] scikit-learn")
    except ImportError as e:
        errors.append(f"scikit-learn: {e}")
        print(f"  [FAIL] scikit-learn: {e}")
    
    try:
        import pandas
        print("  [OK] pandas")
    except ImportError as e:
        errors.append(f"pandas: {e}")
        print(f"  [FAIL] pandas: {e}")
    
    try:
        import plotly
        print("  [OK] plotly")
    except ImportError as e:
        errors.append(f"plotly: {e}")
        print(f"  [FAIL] plotly: {e}")
    
    try:
        import prometheus_client
        print("  [OK] prometheus-client")
    except ImportError as e:
        errors.append(f"prometheus-client: {e}")
        print(f"  [FAIL] prometheus-client: {e}")
    
    return len(errors) == 0, errors

def test_files():
    """Test if all required files exist"""
    print("\n[*] Testing file structure...")
    required_files = [
        "backend/main.py",
        "backend/app/config.py",
        "backend/app/database.py",
        "backend/app/ml/early_warning.py",
        "backend/requirements.txt",
        "frontend/app.py",
        "frontend/requirements.txt",
        "docker-compose.yml",
        "supabase/schema.sql"
    ]
    
    missing = []
    for file in required_files:
        if Path(file).exists():
            print(f"  [OK] {file}")
        else:
            missing.append(file)
            print(f"  [FAIL] {file} - MISSING")
    
    return len(missing) == 0, missing

def test_env():
    """Test environment configuration"""
    print("\n[*] Testing environment configuration...")
    
    if not Path(".env").exists():
        print("  [WARN] .env file not found (using env.example as template)")
        if Path("env.example").exists():
            print("  [OK] env.example exists")
            return False, ["Create .env from env.example"]
        else:
            print("  [FAIL] env.example also missing!")
            return False, ["Create .env file"]
    
    print("  [OK] .env file exists")
    
    # Check if Supabase credentials are set
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        print("  [WARN] python-dotenv not installed, checking environment variables...")
    
    supabase_url = os.getenv("SUPABASE_URL", "")
    supabase_key = os.getenv("SUPABASE_KEY", "")
    
    if not supabase_url or supabase_url == "your_supabase_url_here":
        print("  [WARN] SUPABASE_URL not configured")
        return False, ["Configure SUPABASE_URL in .env"]
    
    if not supabase_key or supabase_key == "your_supabase_key_here":
        print("  [WARN] SUPABASE_KEY not configured")
        return False, ["Configure SUPABASE_KEY in .env"]
    
    print("  [OK] Supabase credentials configured")
    return True, []

def test_docker():
    """Test if Docker is available"""
    print("\n[*] Testing Docker...")
    import subprocess
    try:
        result = subprocess.run(["docker", "--version"], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"  [OK] Docker installed: {result.stdout.strip()}")
            
            # Test docker-compose
            result = subprocess.run(["docker-compose", "--version"], capture_output=True, text=True)
            if result.returncode == 0:
                print(f"  [OK] Docker Compose installed: {result.stdout.strip()}")
                return True, []
            else:
                return False, ["Docker Compose not found"]
        else:
            return False, ["Docker not working"]
    except FileNotFoundError:
        print("  [WARN] Docker not found (optional for local development)")
        return False, ["Docker not installed"]

def main():
    """Main test function"""
    print("=" * 60)
    print("FCEWO Setup Verification")
    print("=" * 60)
    print()
    
    all_passed = True
    issues = []
    
    # Test imports
    imports_ok, import_errors = test_imports()
    if not imports_ok:
        all_passed = False
        issues.extend(import_errors)
    
    # Test files
    files_ok, missing_files = test_files()
    if not files_ok:
        all_passed = False
        issues.extend([f"Missing: {f}" for f in missing_files])
    
    # Test environment
    env_ok, env_issues = test_env()
    if not env_ok:
        all_passed = False
        issues.extend(env_issues)
    
    # Test Docker (optional)
    docker_ok, docker_issues = test_docker()
    if not docker_ok:
        print("  ℹ️  Docker is optional - you can run locally with run_local.py")
    
    # Summary
    print("\n" + "=" * 60)
    if all_passed:
        print("[SUCCESS] All checks passed! System is ready to run.")
        print("\nTo start:")
        print("  - With Docker: docker-compose up --build")
        print("  - Local dev: python run_local.py")
    else:
        print("[WARNING] Some issues found:")
        for issue in issues:
            print(f"  - {issue}")
        print("\nPlease fix the issues above before running.")
        print("\nNote: Supabase is optional - system can run without it (limited features)")
    print("=" * 60)

if __name__ == "__main__":
    main()

