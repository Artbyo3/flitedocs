"""
Main routes for Flitedocs
"""

from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """Home page"""
    return render_template('index.html')

@main_bp.route('/docs')
def docs():
    """Documentation page"""
    return render_template('docs.html')