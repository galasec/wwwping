from os import environ


class Config:
    DEBUG = bool(int(environ.get("WWWPING_API_DEBUG", "0")))
    TESTING = DEBUG
    SECRET_KEY = environ.get("WWWPING_API_SECRET_KEY", "secretkey")
