from pathlib import Path
import os
from datetime import timedelta

# env
from dotenv import load_dotenv

# load env
load_dotenv()

# dir
DJANGO_BASE_DIR = Path(__file__).resolve().parent.parent.parent

# secrate key for signiture
DJANGO_SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

# debug mode
DJANGO_DEBUG = os.getenv("DJANGO_DEBUG")

# allowed hosts
DJANGO_ALLOWED_HOSTS = ["*"]

# local apps
DJANGO_INHOUSE_APPS = ["apps.base", "apps.authentication", "apps.expense_tracker"]

# external apps
DJANGO_THIRDPARTY_APPS = [
    "rest_framework",
    "corsheaders",
    "drf_spectacular",
]

# internal middlewares
DJANGO_INHOUSE_MIDDLEWARE = []

# external middlewares
DJANGO_THIRDPARTY_MIDDLEWARES = [
    "corsheaders.middleware.CorsMiddleware",
]

# cors whitelisted origins
DJANGO_CORS_ORIGIN_WHITELIST = [
    "http://localhost:3000",
]

# cors allowed origins
DJANGO_CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]

X_FRAME_OPTIONS = "DENY"

DJANGO_DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB"),
        "USER": os.getenv("POSTGRES_USER"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
        "HOST": os.getenv("POSTGRES_HOST"),
        "PORT": os.getenv("POSTGRES_PORT"),
    }
}

# Swagger config
DJANGO_REST_FRAMEWORK_CONF = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        # '',
    ),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

SWAGGER_CONF = {
    "TITLE": "POCKET SENSE",
    "DESCRIPTION": "POCKET SENSE",
}

# # simple jwt conf
# DJANGO_SIMPLE_JWT = {
#     "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
#     "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
#     "ROTATE_REFRESH_TOKENS": False,
#     "BLACKLIST_AFTER_ROTATION": False,
#     "ALGORITHM": "HS256",
#     "SIGNING_KEY": DJANGO_SECRET_KEY,
#     "AUTH_HEADER_TYPES": ("Bearer",),
#     'USER_ID_FIELD': 'id',  
# }

# Application configuration
DJANGO_URLBASE = os.getenv("URLBASE")
DJANGO_APP_VERSION = os.getenv("APP_VERSION")

# Django media configurations
# media dir
DJANGO_MEDIA_URL = "/media/"

# to save in my root file
DJANGO_MEDIA_ROOT = os.path.join(DJANGO_BASE_DIR, "media")


DJANGO_LANGUAGE_CODE = "en-us"

DJANGO_TIME_ZONE = os.getenv("time_zone")

DJANGO_USE_i18 = True

USE_TZ = True

# jwt token
DJANGO_JWT_SECRET = os.getenv("JWT_SECRET")

# email smtp configurations
DJANGO_EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DJANGO_EMAIL_HOST = 'smtp.gmail.com'
DJANGO_EMAIL_PORT = 587
DJANGO_EMAIL_USE_TLS = True
DJANGO_EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
DJANGO_EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
