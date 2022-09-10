import os
basedir = os.path.abspath(os.path.dirname(__file__))

PROD = 'prod'
DEV = 'dev'
TEST = 'test'


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'E7173CE3CBFCEAF9C3E3C7261EC46'
    # SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class ProductionConfig(Config):
    DEBUG = False
    CONFIG = PROD
    POSTGRES = {
        'user': os.environ.get('pg_user') or 'tenant',
        'pwd': os.environ.get('pg_pwd') or 'tenant',
        'db': os.environ.get('pg_db') or 'tenants',
        'host': os.environ.get('pg_host') or 'localhost',
        'port': os.environ.get('pg_port') or '5432',
    }
    DEV_DB = {
        'user': os.environ.get('dev_db_user') or 'tenant',
        'pwd': os.environ.get('dev_db_pwd') or 'tenant',
        'db': os.environ.get('dev_db_db') or 'tenants',
        'host': os.environ.get('dev_db_host') or 'localhost',
        'port': os.environ.get('dev_db_port') or '5432',
    }


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    CONFIG = DEV
    POSTGRES = {
        'user': os.environ.get('pg_user') or 'tenant',
        'pwd': os.environ.get('pg_pwd') or 'tenant',
        'db': os.environ.get('pg_db') or 'tenants',
        'host': os.environ.get('pg_host') or 'localhost',
        'port': os.environ.get('pg_port') or '5432',
    }
    DEV_DB = {
        'user': os.environ.get('dev_db_user') or 'tenant',
        'pwd': os.environ.get('dev_db_pwd') or 'tenant',
        'db': os.environ.get('dev_db_db') or 'tenants',
        'host': os.environ.get('dev_db_host') or 'localhost',
        'port': os.environ.get('dev_db_port') or '5432'
    }


class TestingConfig(Config):
    TESTING = True
