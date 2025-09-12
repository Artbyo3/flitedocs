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
    
    # Configurar rutas de archivos estáticos y templates para Vercel
    import os
    if os.environ.get('VERCEL') == '1':
        # En Vercel, el directorio de trabajo es la raíz del proyecto
        app.static_folder = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'app', 'static')
        app.template_folder = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'app', 'templates')
    
    # Register blueprints
    from app.routes import main_bp
    app.register_blueprint(main_bp)
    
    return app

app = create_app()
