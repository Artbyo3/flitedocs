import sys
import os

# Agregar la raíz del proyecto al path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app

# Crear la aplicación Flask
app = create_app()

# Exportar para Vercel (REQUERIDO)
handler = app

# Configurar para desarrollo local
if __name__ == '__main__':
    app.run(debug=True)
