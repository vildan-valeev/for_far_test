from src.settings.components import config

DEBUG = False

ALLOWED_HOSTS = [
    config('DOMAIN'),
    'localhost',
]


