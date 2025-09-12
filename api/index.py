import os
import sys

# Asegurar que el directorio raíz del proyecto esté en sys.path para importar el paquete 'app'
current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.insert(0, project_dir)

from app import create_app

app = create_app()
handler = app  # Exportar directamente la aplicación Flask como callable WSGI
