from pathlib import Path
from .config import (
    DJANGO_BASE_DIR,
    DJANGO_SECRET_KEY,
    DJANGO_DEBUG,
    DJANGO_ALLOWED_HOSTS,
    DJANGO_INHOUSE_APPS,
    DJANGO_THIRDPARTY_APPS,
    DJANGO_INHOUSE_MIDDLEWARE,
    DJANGO_THIRDPARTY_MIDDLEWARES,
    DJANGO_DATABASES,
    DJANGO_CORS_ALLOWED_ORIGINS,
    DJANGO_CORS_ORIGIN_WHITELIST,
    DJANGO_REST_FRAMEWORK_CONF,
    SWAGGER_CONF,
    DJANGO_MEDIA_URL,
    DJANGO_MEDIA_ROOT,
    DJANGO_LANGUAGE_CODE,
    DJANGO_TIME_ZONE,
    DJANGO_USE_i18,
    USE_TZ,
    DJANGO_URLBASE,
    DJANGO_APP_VERSION,
    DJANGO_SIMPLE_JWT,
    # DJANGO_JWT_SECRET,
    DJANGO_EMAIL_BACKEND,
    DJANGO_EMAIL_HOST,
    DJANGO_EMAIL_PORT,
    DJANGO_EMAIL_USE_TLS,
    DJANGO_EMAIL_HOST_USER,
    DJANGO_EMAIL_HOST_PASSWORD,
    DJANGO_AUTH_USER_MODEL,

)
from corsheaders.defaults import default_headers

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = DJANGO_BASE_DIR


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = DJANGO_SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = DJANGO_DEBUG

ALLOWED_HOSTS = DJANGO_ALLOWED_HOSTS

# cors origin
CORS_ORIGIN_WHITELIST = DJANGO_CORS_ORIGIN_WHITELIST

CORS_ALLOWED_ORIGINS = DJANGO_CORS_ALLOWED_ORIGINS

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = [*default_headers, "Cookie-Tracker-Id"]

# inhouse internal apps
INHOUSE_APPS = DJANGO_INHOUSE_APPS

# thirdparty apps
THIRDPARTY_APPS = DJANGO_THIRDPARTY_APPS


# Application definition
INSTALLED_APPS = (
    [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
    ]
    + DJANGO_INHOUSE_APPS
    + THIRDPARTY_APPS
)

# internal middlewares
INHOUSE_MIDDLEWARE = DJANGO_INHOUSE_MIDDLEWARE

# thirdparty middlewares
THIRDPARTY_MIDDLEWARES = DJANGO_THIRDPARTY_MIDDLEWARES


MIDDLEWARE = (
    [
        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
    ]
    + INHOUSE_MIDDLEWARE
    + THIRDPARTY_MIDDLEWARES
)

ROOT_URLCONF = "pocket_sense.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "pocket_sense.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = DJANGO_DATABASES


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = DJANGO_LANGUAGE_CODE

TIME_ZONE = DJANGO_TIME_ZONE

USE_I18N = DJANGO_USE_i18

USE_TZ = USE_TZ


# REST_FRAMEWORK Config
REST_FRAMEWORK = DJANGO_REST_FRAMEWORK_CONF

# Django auth model
AUTH_USER_MODEL = DJANGO_AUTH_USER_MODEL


# simple jwt conf
SIMPLE_JWT = DJANGO_SIMPLE_JWT

# SPECTACULAR_SETTINGS config
SPECTACULAR_SETTINGS = SWAGGER_CONF


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"

# media configuration

# Dajno media
MEDIA_URL = DJANGO_MEDIA_URL


# to save in my root file
MEDIA_ROOT = DJANGO_MEDIA_ROOT

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# vesion and url conf
URLBASE = DJANGO_URLBASE
APP_VERSION = DJANGO_APP_VERSION

# jwt settings config
# JWT_SECRET =DJANGO_JWT_SECRET

# smpt conf
EMAIL_BACKEND = DJANGO_EMAIL_BACKEND
EMAIL_HOST = DJANGO_EMAIL_HOST
EMAIL_PORT = DJANGO_EMAIL_PORT
EMAIL_USE_TLS = DJANGO_EMAIL_USE_TLS
EMAIL_HOST_USER = DJANGO_EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = DJANGO_EMAIL_HOST_PASSWORD
