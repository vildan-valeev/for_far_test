from src.settings.components import config

REDIS_HOST = config("REDIS_HOST")
REDIS_PORT = config("REDIS_PORT",)

RQ_QUEUES = {
    'default': {
        'HOST': REDIS_HOST,
        'PORT':  REDIS_PORT,
        'DB': 0,
        'DEFAULT_TIMEOUT': 360,
    },

}
