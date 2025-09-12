import os
import sys

# Agregar el directorio padre al path para importar módulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Usar el Application Factory
from app import create_app

# Crear la aplicación Flask usando el factory
app = create_app()

# Exportar para Vercel - según la documentación, debe ser 'handler' para WSGI
handler = app.wsgi_app