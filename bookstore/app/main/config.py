import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = False


class DevelopmentConfig(Config):
    FLASK_ENV = 'dev'
    DEBUG = True
    TESTING = True


class TestingConfig(Config):
    FLASK_ENV = 'test'
    DEBUG = True
    TESTING = True


class ProductionConfig(Config):
    FLASK_ENV = 'prod'
    DEBUG = False
    TESTING = False


config_envs = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
