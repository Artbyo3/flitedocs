"""
Flitedocs - Flask Application
"""

from flask import Flask
from config import get_config

def create_app(config_class=None):
    """Application factory pattern"""
    app = Flask(__name__)
    
    # Use provided config or auto-detect
    if config_class is None:
        config_class = get_config()
    
    app.config.from_object(config_class)
    
    # Register blueprints
    from app.routes import main_bp
    app.register_blueprint(main_bp)
    
    return app

# Create app instance for direct imports
app = create_app()
