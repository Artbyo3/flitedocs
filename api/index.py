"""
Vercel entry point for Flitedocs
"""

from flask import Flask, render_template

# Create a simple Flask app directly
app = Flask(__name__, 
            template_folder='../app/templates',
            static_folder='../app/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/docs')
def docs():
    return render_template('docs.html')

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Export for Vercel
handler = app
