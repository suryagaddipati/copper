#!/usr/bin/env python3
"""
Copper UI Launcher

Quick launcher script for the Copper data exploration UI.
Usage: python run_ui.py
"""

import subprocess
import sys
from pathlib import Path

def main():
    """Launch the Streamlit app."""
    ui_dir = Path(__file__).parent / "ui"
    app_file = ui_dir / "app.py"
    
    if not app_file.exists():
        print(f"Error: App file not found at {app_file}")
        sys.exit(1)
    
    print("🚀 Starting Copper Data Explorer...")
    print(f"📂 App location: {app_file}")
    print("🌐 Opening in your default browser...")
    print("\n" + "="*50)
    print("Press Ctrl+C to stop the server")
    print("="*50 + "\n")
    
    try:
        # Use uv to run streamlit in the right environment
        subprocess.run([
            "uv", "run", "streamlit", "run", str(app_file),
            "--theme.base", "light",
            "--theme.primaryColor", "#ff6b35",
            "--theme.backgroundColor", "#ffffff",
            "--theme.secondaryBackgroundColor", "#f0f2f6"
        ])
    except KeyboardInterrupt:
        print("\n👋 Shutting down Copper Data Explorer...")
    except Exception as e:
        print(f"❌ Error starting app: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()