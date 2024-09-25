# config/settings.py

import os
import yaml

class Config:
    """Base configuration"""
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default-secret-key')
    DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///db.sqlite3')
    AI_MODEL_PATH = os.path.join(os.path.dirname(__file__), '../ai/models/')
    IOT_SENSORS = os.environ.get('IOT_SENSORS', 'enabled')

    # Load additional secrets from YAML file
    with open(os.path.join(os.path.dirname(__file__), 'secrets.yaml'), 'r') as file:
        secrets = yaml.safe_load(file)

    # Example of loading credentials from the secrets file
    API_KEY = secrets.get('API_KEY', 'default-api-key')

class DevelopmentConfig(Config):
    """Development environment configuration"""
    DEBUG = True
    DATABASE_URL = os.environ.get('DEV_DATABASE_URL', 'sqlite:///dev_db.sqlite3')

class TestingConfig(Config):
    """Testing environment configuration"""
    TESTING = True
    DATABASE_URL = os.environ.get('TEST_DATABASE_URL', 'sqlite:///test_db.sqlite3')

class ProductionConfig(Config):
    """Production environment configuration"""
    DEBUG = False
    DATABASE_URL = os.environ.get('PROD_DATABASE_URL', 'postgresql://user@localhost/prod_db')