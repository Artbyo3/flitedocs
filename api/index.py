from app import create_app

app = create_app()
handler = app.wsgi_app
