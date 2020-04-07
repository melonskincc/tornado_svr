import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)
SETTINGS = {
    'debug': True,
    'cookie_secret': 'abc'
}
DB = {
    'user': 'root',
    'password': 'Goodj@b!1',
    'port': 3306,
    'db': 'testa'
}

REDIS_ADDR = 'redis://127.0.0.1:6379/0'
HOST = '127.0.0.1'
PORT = 9090
# log日志
BASE_LOG_DIR = os.path.join(BASE_DIR, 'log')

if not os.path.exists(BASE_LOG_DIR):
    os.makedirs(BASE_LOG_DIR)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '[%(levelname)s][%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d] %(message)s'
        },
        'simple': {
            'format': '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d] %(message)s'
        },
        'collect': {
            'format': '%(message)s'
        }
    },
    'handlers': {
        'default': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(BASE_LOG_DIR, 'info.log'),
            'when': 'midnight',
            'backupCount': 5,
            'interval': 1,
            'formatter': 'simple',
            'encoding': 'utf-8'
        },
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(BASE_LOG_DIR, 'error.log'),
            'when': 'midnight',
            'backupCount': 5,
            'interval': 1,
            'formatter': 'standard',
            'encoding': 'utf-8'
        },
        'abc': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(BASE_LOG_DIR, 'abc.log'),
            'when': 'midnight',
            'backupCount': 5,
            'interval': 1,
            'formatter': 'simple',
            'encoding': 'utf-8'
        },
        # 'console': {
        #     'level': 'DEBUG',
        #     'class': 'logging.StreamHandler',
        # },
    },
    'loggers': {
        'tornado': {
            'handlers': ['default', 'error'],
            'level': 'INFO',
            'propagate': True
        },
        'abc': {
            'handlers': ['abc'],
            'level': 'INFO',
            'propagate': True
        }
    }
}
