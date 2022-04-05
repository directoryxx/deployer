from os import environ, path,getcwd
from dotenv import load_dotenv


BASE_DIR = path.abspath(path.dirname(__file__))

load_dotenv()

# config class
class Config(object):
    """set Flask configuration variables from .env file."""

    # general
    DEBUG = environ.get('DEBUG')
    SECRET_KEY = environ.get('SECRET_KEY')
    HOST = environ.get('HOST')
    PORT = environ.get('PORT')
    APP_ENV = environ.get('APP_ENV')
    environ['FLASK_ENV'] = APP_ENV

    # Google
    PROJECT = environ.get('PROJECT')
    ZONE = environ.get('ZONE')
    cwd = getcwd()
    environ['GOOGLE_APPLICATION_CREDENTIALS'] = cwd+'/credentials.json'

    # Slack
    WEBHOOK_URL = environ.get('WEBHOOK')
    CHANNEL_NAME = environ.get('CHANNEL_NAME')
    TOKEN = environ.get('TOKEN')
    SUNNY = ':sunny:'
    RAIN = ':thunder_cloud_and_rain:'

    #SSH
    SSH_KEY = cwd+'/id_rsa'
    ROOTUSER = environ.get('ROOTUSER')

    # sqlalchemy
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI') or 'sqlite:///' + path.join(BASE_DIR, 'db.sqlite') # if you do not create an environment file then it will create a sqlite database
    SQLALCHEMY_TRACK_MODIFICATIONS = environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')