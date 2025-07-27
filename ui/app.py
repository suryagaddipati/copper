"""
Main Streamlit App Entry Point

Run with: streamlit run ui/app.py
"""

import streamlit as st
import sys
from pathlib import Path

# Add src to path for imports
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from dashboard import CopperDashboard

def main():
    st.set_page_config(
        page_title="Copper Data Explorer",
        page_icon="☄️",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    st.title("☄️ Copper Data Explorer")
    st.markdown("*Define Once. Run Anywhere. Explore Everywhere.*")
    
    # Initialize dashboard
    dashboard = CopperDashboard()
    dashboard.render()

if __name__ == "__main__":
    main()