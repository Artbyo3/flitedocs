from app import create_app
import os

# Crear la aplicación Flask
app = create_app()

# Exportar para Vercel (REQUERIDO)
handler = app

# Configurar para desarrollo local
if __name__ == '__main__':
    app.run(debug=True)
