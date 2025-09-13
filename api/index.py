"""
Vercel entry point for Flitedocs
"""

from flask import Flask, render_template
import os

# Create Flask app with absolute paths
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__, 
            template_folder=os.path.join(basedir, '..', 'app', 'templates'),
            static_folder=os.path.join(basedir, '..', 'app', 'static'))

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
