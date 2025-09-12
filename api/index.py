import os
import sys
from flask import Flask

# Agregar el directorio raíz al path para importar módulos
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
sys.path.insert(0, root_dir)

# Crear la aplicación Flask directamente
app = Flask(__name__)

# Configurar la app
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

# Configurar rutas de archivos estáticos y templates para Vercel
app.static_folder = os.path.join(root_dir, 'app', 'static')
app.template_folder = os.path.join(root_dir, 'app', 'templates')

# Importar y registrar blueprints
from app.routes import main_bp
app.register_blueprint(main_bp)

# Exportar para Vercel - según la documentación, debe ser 'handler' para WSGI
handler = app.wsgi_app
