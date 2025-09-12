"""
Main routes for Flitedocs
"""

from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
@main_bp.route('/api/')
def index():
    """Home page - works both locally and on Vercel"""
    return render_template('index.html')

@main_bp.route('/docs')
@main_bp.route('/api/docs')
def docs():
    """Documentation page - works both locally and on Vercel"""
    return render_template('docs.html')