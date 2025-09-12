"""
Vercel entry point for Flitedocs Flask application
"""
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app

# Create Flask app instance
app = create_app()

# Export the app for Vercel
handler = app
