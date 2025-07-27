#!/usr/bin/env python3
"""
Copper UI Launcher

This script starts the Copper Streamlit application with proper configuration.
"""

import subprocess
import sys
from pathlib import Path

def main():
    """Start the Copper UI."""
    ui_dir = Path(__file__).parent / "ui"
    app_file = ui_dir / "app.py"
    
    if not app_file.exists():
        print(f"❌ Error: {app_file} not found")
        sys.exit(1)
    
    print("🚀 Starting Copper Data Explorer...")
    print(f"📁 UI Directory: {ui_dir}")
    print(f"📄 App File: {app_file}")
    print("🌐 The app will open in your browser at http://localhost:8501")
    print("⏹️  Press Ctrl+C to stop the server")
    print("-" * 50)
    
    try:
        # Run streamlit with proper configuration
        subprocess.run([
            "uv", "run", "streamlit", "run", str(app_file),
            "--server.port", "8501",
            "--server.address", "localhost",
            "--browser.gatherUsageStats", "false",
            "--logger.level", "info"
        ], check=True)
    except KeyboardInterrupt:
        print("\n⏹️  Stopping Copper UI...")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error starting UI: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()