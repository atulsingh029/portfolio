import os

SECRET_KEY = ''

ALLOW_HOSTS = []

DEBUG = True

DB_NAME = ''
DB_USER = ''
DB_PASSWORD = ''
DB_HOST = ''
DB_POST = ''

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'atul.auth@gmail.com'
EMAIL_HOST_PASSWORD = os.environ.get('pwd')
EMAIL_PORT= 587
