#!/usr/bin/env python3
"""
Create .env file with safe port assignments
Checks for port conflicts and suggests alternatives
"""
import socket
import os
from pathlib import Path

def check_port(port):
    """Check if a port is available"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex(('127.0.0.1', port))
    sock.close()
    return result != 0

def find_available_port(start_port, max_attempts=10):
    """Find an available port starting from start_port"""
    for i in range(max_attempts):
        port = start_port + i
        if check_port(port):
            return port
    return None

def main():
    """Create .env file with safe ports"""
    print("=" * 60)
    print("Creating .env file with safe port assignments")
    print("=" * 60)
    print()
    
    # Check default ports
    default_ports = {
        'API_PORT': 8000,
        'FRONTEND_PORT': 8501,
        'PROMETHEUS_PORT': 9091,
        'GRAFANA_PORT': 3000
    }
    
    safe_ports = {}
    conflicts = []
    
    print("[INFO] Checking port availability...")
    for name, port in default_ports.items():
        if check_port(port):
            safe_ports[name] = port
            print(f"  [OK] Port {port} ({name}) is available")
        else:
            alt_port = find_available_port(port)
            if alt_port:
                safe_ports[name] = alt_port
                conflicts.append((name, port, alt_port))
                print(f"  [WARN] Port {port} ({name}) is in use, using {alt_port} instead")
            else:
                safe_ports[name] = port
                print(f"  [WARN] Port {port} ({name}) is in use, but no alternative found")
    
    print()
    
    # Read template
    template_path = Path("env.example")
    if not template_path.exists():
        print("[ERROR] env.example not found!")
        return 1
    
    # Create .env content
    env_content = template_path.read_text()
    
    # Replace port values
    for name, port in safe_ports.items():
        # Find the line and replace
        lines = env_content.split('\n')
        new_lines = []
        for line in lines:
            if line.startswith(f"{name}="):
                new_lines.append(f"{name}={port}")
            else:
                new_lines.append(line)
        env_content = '\n'.join(new_lines)
    
    # Write .env file
    env_path = Path(".env")
    if env_path.exists():
        try:
            response = input(f"[WARN] .env already exists. Overwrite? (y/n): ").lower().strip()
            if response != 'y':
                print("[INFO] Cancelled. Using existing .env file.")
                return 0
        except (EOFError, KeyboardInterrupt):
            # Non-interactive mode - create backup and overwrite
            backup_path = Path(".env.backup")
            if not backup_path.exists():
                backup_path.write_text(env_path.read_text())
                print(f"[INFO] Backed up existing .env to .env.backup")
            print("[INFO] Non-interactive mode - overwriting .env")
    
    env_path.write_text(env_content)
    
    print("[SUCCESS] Created .env file with the following ports:")
    for name, port in safe_ports.items():
        print(f"  {name}={port}")
    
    if conflicts:
        print()
        print("[INFO] Port changes made due to conflicts:")
        for name, old_port, new_port in conflicts:
            print(f"  {name}: {old_port} -> {new_port}")
        print()
        print("[INFO] Update your bookmarks:")
        print(f"  - API: http://localhost:{safe_ports['API_PORT']}")
        print(f"  - Frontend: http://localhost:{safe_ports['FRONTEND_PORT']}")
        print(f"  - Prometheus: http://localhost:{safe_ports['PROMETHEUS_PORT']}")
        print(f"  - Grafana: http://localhost:{safe_ports['GRAFANA_PORT']}")
    
    print()
    print("[INFO] Don't forget to add your Supabase credentials to .env")
    print("=" * 60)
    
    return 0

if __name__ == "__main__":
    exit(main())

