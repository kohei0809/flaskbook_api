from flaskbook_api.api.config.base import Config


class LocalCOnfig(Config):
    TESTING = True
    DEBUG = True
