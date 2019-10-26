from os import getenv

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = getenv('DATABASE_URL')

MAIL_SERVER = getenv('MAIL_SERVER')
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = getenv('MAIL_USERNAME')
MAIL_PASSWORD = getenv('MAIL_PASSWORD')
MAIL_DEFAULT_SENDER = ('南苑聚合', MAIL_USERNAME)
