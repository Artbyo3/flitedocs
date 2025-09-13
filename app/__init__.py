"""
Flitedocs - Simple Static Site
"""

from flask import Flask, render_template
import os

def create_app():
    """Create Flask app for static site"""
    # Create app with explicit template/static folders
    basedir = os.path.abspath(os.path.dirname(__file__))
    app = Flask(__name__,
                template_folder=os.path.join(basedir, 'templates'),
                static_folder=os.path.join(basedir, 'static'))

    # Simple configuration for static site
    app.config['SECRET_KEY'] = 'static-site-no-secret-needed'
    app.config['DEBUG'] = True

    # Routes
    @app.route('/')
    def index():
        """Home page"""
        return render_template('index.html')

    @app.route('/docs')
    def docs():
        """Documentation page"""
        return render_template('docs.html')

    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        return render_template('404.html'), 404

    return app

