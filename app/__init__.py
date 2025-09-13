"""
Flitedocs - Flask Application
"""

from flask import Flask, render_template
from app.config import get_config
import os

def create_app(config_class=None):
    """Application factory pattern"""
    # Get the directory containing this file
    basedir = os.path.abspath(os.path.dirname(__file__))
    
    app = Flask(__name__, 
                template_folder=os.path.join(basedir, 'templates'),
                static_folder=os.path.join(basedir, 'static'))
    
    # Use provided config or auto-detect
    if config_class is None:
        config_class = get_config()
    
    app.config.from_object(config_class)
    
    # Register blueprints
    from app.routes import main_bp
    app.register_blueprint(main_bp)
    
    # Register error handlers
    @app.errorhandler(404)
    def not_found(error):
        """404 error handler - works both locally and on Vercel"""
        return render_template('404.html'), 404
    
    return app

