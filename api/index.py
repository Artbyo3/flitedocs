import os
from flask import Flask, render_template

# Crear la aplicación Flask directamente
app = Flask(__name__, 
           static_folder='../app/static',
           template_folder='../app/templates')

# Configurar la app
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

# Importar y registrar blueprints
from app.routes import main_bp
app.register_blueprint(main_bp)

# Exportar para Vercel (REQUERIDO)
handler = app

# Configurar para desarrollo local
if __name__ == '__main__':
    app.run(debug=True)
