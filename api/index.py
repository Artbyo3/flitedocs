"""
Vercel entry point for Flitedocs
This is a thin wrapper that imports and exports the Flask app for Vercel deployment.
"""

import os
import sys

# Debug: Print current working directory and Python path
print(f"Current working directory: {os.getcwd()}")
print(f"Python path: {sys.path}")

try:
    from app import create_app
    print("✅ Successfully imported create_app")
    
    # Create Flask app instance for Vercel
    app = create_app()
    print("✅ Successfully created Flask app")
    
    # Export the WSGI application for Vercel
    handler = app
    print("✅ Successfully exported handler")
    
except Exception as e:
    print(f"❌ Error during app creation: {str(e)}")
    print(f"❌ Error type: {type(e).__name__}")
    import traceback
    traceback.print_exc()
    
    # Create a minimal error handler
    from flask import Flask
    error_app = Flask(__name__)
    
    @error_app.route('/')
    def error_route():
        return f"Error: {str(e)}", 500
    
    handler = error_app
