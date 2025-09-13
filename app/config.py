"""
Configuration settings for Flitedocs
Supports both local .env files and Vercel environment variables
"""

import os
from dotenv import load_dotenv

# Get the directory containing this file
basedir = os.path.abspath(os.path.dirname(__file__))

# Load .env file only if it exists (for local development)
env_path = os.path.join(basedir, '..', '.env')
if os.path.exists(env_path):
    load_dotenv(env_path)

class Config:
    """Base configuration class"""
    # Flask settings
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'change-this-in-production'
    
    # Database settings (if needed in the future)
    DATABASE_URL = os.environ.get('DATABASE_URL')
    
    # Vercel specific settings
    VERCEL = os.environ.get('VERCEL') == '1'
    
    # Static and template folders (Flask will use these automatically)
    STATIC_FOLDER = 'static'
    TEMPLATE_FOLDER = 'templates'

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    ENV = 'development'

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    ENV = 'production'

class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
    DEBUG = True

def get_config():
    """Get configuration based on environment"""
    if os.environ.get('VERCEL') == '1':
        return ProductionConfig
    elif os.environ.get('FLASK_ENV') == 'production':
        return ProductionConfig
    elif os.environ.get('FLASK_ENV') == 'testing':
        return TestingConfig
    else:
        return DevelopmentConfig

# Configuration dictionary for easy access
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': get_config()
}
