from envparse import env

DEBUG = env.str('DEBUG')

REDIS_HOST = env.str('REDIS_HOST')
REDIS_PORT = env.int('REDIS_PORT')
REDIS_PASSWORD = env.str('REDIS_PASSWORD')