"""
Flitedocs - Flask Application
"""

from flask import Flask, render_template
import os
from dotenv import load_dotenv

# Load environment variables from config.env (if present)
load_dotenv('config.env')


def create_app(config_class=None):
    """Application factory pattern"""
    # Create app with explicit template/static folders so Vercel works
    basedir = os.path.abspath(os.path.dirname(__file__))
    app = Flask(__name__,
                template_folder=os.path.join(basedir, 'templates'),
                static_folder=os.path.join(basedir, 'static'))

    # Configuration from environment or provided config_class
    if config_class is not None:
        app.config.from_object(config_class)
    else:
        # Minimal required settings similar to the working example
        app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
        if not app.config['SECRET_KEY']:
            raise ValueError("SECRET_KEY environment variable is required")

        app.config['DEBUG'] = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'

    # Routes (simple inline routes like the working example)
    @app.route('/')
    def index():
        """Home page"""
        return render_template('index.html')

    @app.route('/about')
    def about():
        """About page"""
        return render_template('about.html')

    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def internal_error(error):
        return render_template('500.html'), 500

    return app

