"""
Vercel entry point for Flitedocs
This is a thin wrapper that imports and exports the Flask app for Vercel deployment.
"""

from app import create_app

# Create Flask app instance for Vercel
app = create_app()

# Export the WSGI application for Vercel
handler = app
