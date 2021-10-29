from environs import Env

env = Env()
env.read_env()

class Config:
    SECRET_KEY = env('SECRET_KEY')

    # Database
    DATABASE_URL = env("DATABASE_URL")
    if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # ADMIN
    FLASK_ADMIN_SWATCH = 'lux'

    # BasicAuth
    BASIC_AUTH_USERNAME = env("BASIC_AUTH_USERNAME")
    BASIC_AUTH_PASSWORD = env("BASIC_AUTH_PASSWORD")
