import os

SECRET_KEY = 'tester'

ALLOW_HOSTS = ['*']

DEBUG = True

DB_NAME = 'portfolio'
DB_USER = 'root'
DB_PASSWORD = ''
DB_HOST = ''
DB_POST = ''

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'atul.auth@gmail.com'
EMAIL_HOST_PASSWORD = os.environ.get('pwd')
EMAIL_PORT= 587
