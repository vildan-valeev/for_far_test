from decouple import Csv

from src.settings.components import config

print('DEVELOPMENT SETTINGS!!!!')
DEBUG = True

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv(), default=config('DOMAIN'))
