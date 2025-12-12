#!/usr/bin/env python3
"""
Check if required ports are available
"""
import socket
import sys

def check_port(port, name):
    """Check if a port is available"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex(('127.0.0.1', port))
    sock.close()
    
    if result == 0:
        print(f"  [WARN] Port {port} ({name}) is already in use")
        return False
    else:
        print(f"  [OK] Port {port} ({name}) is available")
        return True

def main():
    """Check all required ports"""
    print("=" * 60)
    print("Port Availability Check")
    print("=" * 60)
    print()
    
    ports = {
        8000: "API (FastAPI)",
        8501: "Frontend (Streamlit)",
        9091: "Prometheus",
        3000: "Grafana"
    }
    
    all_available = True
    conflicts = []
    
    for port, name in ports.items():
        if not check_port(port, name):
            all_available = False
            conflicts.append((port, name))
    
    print()
    print("=" * 60)
    
    if all_available:
        print("[SUCCESS] All ports are available!")
        print("\nYou can start the system with:")
        print("  docker-compose up --build")
    else:
        print("[WARNING] Some ports are already in use:")
        for port, name in conflicts:
            print(f"  - Port {port} ({name})")
        print("\nOptions:")
        print("1. Stop the service using the port")
        print("2. Change the port in .env file:")
        for port, name in conflicts:
            if port == 8000:
                print(f"   API_PORT=8001")
            elif port == 8501:
                print(f"   FRONTEND_PORT=8502")
            elif port == 9091:
                print(f"   PROMETHEUS_PORT=9092")
            elif port == 3000:
                print(f"   GRAFANA_PORT=3001")
        print("\nThen update docker-compose.yml to use the new ports")
    
    print("=" * 60)
    
    return 0 if all_available else 1

if __name__ == "__main__":
    sys.exit(main())

