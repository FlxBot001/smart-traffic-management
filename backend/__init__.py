from flask import Flask
from flask_cors import CORS
from config.settings import Config
from config.logging_config import configure_logging
from api.public_api import public_api_bp
from api.traffic_data_api import traffic_data_api_bp
from iot.traffic_sensors import initialize_sensors
from ai.traffic_prediction import TrafficPredictor
from ai.accident_detection import AccidentDetector

def create_app():
    app = Flask(__name__)
    
    # Enable Cross-Origin Resource Sharing (CORS)
    CORS(app)
    
    # Load application configurations
    app.config.from_object(Config)
    
    # Configure application logging
    configure_logging()

    # Register API Blueprints
    app.register_blueprint(public_api_bp, url_prefix='/api/public')
    app.register_blueprint(traffic_data_api_bp, url_prefix='/api/traffic')

    # Initialize IoT systems (traffic sensors, etc.)
    initialize_sensors()

    # Initialize AI models
    app.traffic_predictor = TrafficPredictor()
    app.accident_detector = AccidentDetector()

    return app
