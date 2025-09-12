"""
Vercel entry point for Flitedocs
This is a thin wrapper that imports and exports the Flask app for Vercel deployment.
"""

import os
import sys

# Add project root to Python path for imports
current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.insert(0, project_dir)

from app import create_app

# Create Flask app instance for Vercel
app = create_app()

# Export the WSGI application for Vercel
handler = app
