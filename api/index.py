"""
Vercel entry point for Flitedocs Flask application
"""
import sys
import os

# Add the parent directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

# Import Flask and create app directly
from flask import Flask, render_template

# Create Flask app
app = Flask(__name__, 
           static_folder='../app/static',
           template_folder='../app/templates')

# Configure app
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')

# Import and register blueprints
from app.routes import main_bp
app.register_blueprint(main_bp)

# Export for Vercel
handler = app
