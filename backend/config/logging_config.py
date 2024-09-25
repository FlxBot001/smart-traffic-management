import logging
from logging.config import dictConfig

def configure_logging():
    """
    Configure application logging
    """
    log_config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'default': {
                'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
            },
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'default',
            },
            'file': {
                'class': 'logging.FileHandler',
                'filename': 'app.log',
                'formatter': 'default',
            },
        },
        'root': {
            'level': 'INFO',
            'handlers': ['console', 'file'],
        },
    }
    dictConfig(log_config)

    # Add logging for critical application areas
    logging.getLogger('werkzeug').setLevel(logging.WARNING)
