from os import environ


class Config:
    DEBUG = bool(int(environ.get("WWWPING_API_DEBUG", "0")))
    TESTING = DEBUG
    SECRET_KEY = environ.get("WWWPING_API_SECRET_KEY", "secretkey")

    SQLALCHEMY_DATABASE_URI = environ.get("WWWPING_API_DATABASE_URI", None)
    SQLALCHEMY_ECHO = DEBUG
    SQLALCHEMY_RECORD_QUERIES = DEBUG
    SQLALCHEMY_TRACK_MODIFICATIONS = DEBUG
