"""
Run script for Flitedocs static site
"""

from app import create_app

app = create_app()

# Export for Vercel
handler = app.wsgi_app

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
