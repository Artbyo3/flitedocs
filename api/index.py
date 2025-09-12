import os
import sys
from flask import Flask

# Agregar el directorio padre al path para importar módulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Crear la aplicación Flask
app = Flask(__name__)

# Configurar la app
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

# Configurar rutas de archivos estáticos y templates
# En Vercel, el directorio de trabajo es la raíz del proyecto
app.static_folder = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'app', 'static')
app.template_folder = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'app', 'templates')

# Importar y registrar blueprints
from app.routes import main_bp
app.register_blueprint(main_bp)

# Exportar para Vercel - según la documentación, debe ser 'handler' para WSGI
handler = app.wsgi_app
