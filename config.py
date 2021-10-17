from environs import Env

env = Env()
env.read_env()

class Config:
    # General Config
    # FLASK_APP = env('FLASK_APP')

    # Database
    PG_HOST = env("PG_HOST")
    PG_USER = env("PG_USER")
    PG_PASSWORD = env("PG_PASSWORD")
    DATABASE = env("DATABASE")

    SQLALCHEMY_DATABASE_URI = f'postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}/{DATABASE}'
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
