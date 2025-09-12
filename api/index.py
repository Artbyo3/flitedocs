import os
import sys
from flask import Flask

# Agregar el directorio padre al path para importar módulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Crear la aplicación Flask
app = Flask(__name__)

# Configurar la app
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

# Configurar rutas de archivos estáticos y templates (relativas al directorio base del proyecto)
app.static_folder = 'app/static'
app.template_folder = 'app/templates'

# Importar y registrar blueprints
from app.routes import main_bp
app.register_blueprint(main_bp)

# Exportar para Vercel - según la documentación, debe ser 'app' para WSGI
