from flask import Flask, jsonify
from flask_cors import CORS
from config.settings import Config
from config.logging_config import configure_logging
from api.public_api import public_api_bp
from api.traffic_data_api import traffic_data_api_bp
from iot.traffic_sensors import initialize_sensors, get_sensor_data
from ai.traffic_prediction import TrafficPredictor
from ai.accident_detection import AccidentDetector
import logging

def create_app():
    # Initialize the Flask application
    app = Flask(__name__)
    
    # Enable CORS for all routes
    CORS(app)
    
    # Load configuration
    app.config.from_object(Config)

    # Configure logging
    configure_logging()

    # Register API Blueprints
    app.register_blueprint(public_api_bp, url_prefix='/api/public')
    app.register_blueprint(traffic_data_api_bp, url_prefix='/api/traffic')

    # Initialize IoT components
    initialize_sensors()
    
    # Initialize AI models
    traffic_predictor = TrafficPredictor()
    accident_detector = AccidentDetector()

    # Error Handling
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({'message': 'Not Found', 'error': str(error)}), 404

    @app.errorhandler(500)
    def internal_error(error):
        logging.error(f'Internal Server Error: {error}')
        return jsonify({'message': 'Internal Server Error', 'error': str(error)}), 500

    # Example Route for AI Predictions
    @app.route('/api/predict/traffic', methods=['POST'])
    def predict_traffic():
        data = request.get_json()
        prediction = traffic_predictor.predict(data)
        return jsonify(prediction)

    # Example Route for Accident Detection
    @app.route('/api/detect/accident', methods=['POST'])
    def detect_accident():
        data = request.get_json()
        result = accident_detector.detect(data)
        return jsonify(result)

    # Example Route for IoT Data
    @app.route('/api/iot/sensors', methods=['GET'])
    def sensor_data():
        data = get_sensor_data()
        return jsonify(data)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000)
