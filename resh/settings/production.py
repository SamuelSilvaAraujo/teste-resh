from decouple import config
from dj_database_url import parse as dburl

from .base import *  # noqa

SECRET_KEY = config("SECRET_KEY")
DEBUG = False
CSRF_TRUSTED_ORIGINS = config("CSRF_TRUSTED_ORIGINS", cast=Csv())

DATABASES = {"default": config("DATABASE_URL", cast=dburl)}
