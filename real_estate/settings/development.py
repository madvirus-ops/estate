from .base import *



DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

DATABASES = {
    'default':{
    'ENGINE':'django.db.backends.postgresql',
    'NAME': env('DB_NAME'),
    'USER': env('DB_USER'),
    'HOST': env('DB_HOST'),
    'PORT': env('DB_PORT'),
    'PASSWORD': env('DB_PASSWORD'),
    }
}
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'madvirus@madvirus.io'
DOMAIN = env("DOMAIN")
SITE_NAME = "Zenon Real Estate"
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
EMAIL_PORT = env("EMAIL_PORT")