"""
Run script for Flitedocs
"""

import os
from flask import Flask, render_template

# Crear la aplicación Flask directamente
app = Flask(__name__, 
           static_folder='app/static',
           template_folder='app/templates')

# Configurar la app
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

# Importar y registrar blueprints
from app.routes import main_bp
app.register_blueprint(main_bp)

# Exportar para Vercel (REQUERIDO)
handler = app

if __name__ == '__main__':
    import sys
    
    # Parse command line arguments
    host = '127.0.0.1'
    port = 5000
    debug = False
    
    if '--host' in sys.argv:
        host = sys.argv[sys.argv.index('--host') + 1]
    if '--port' in sys.argv:
        port = int(sys.argv[sys.argv.index('--port') + 1])
    if '--debug' in sys.argv:
        debug = True
    
    app.run(host=host, port=port, debug=debug)
