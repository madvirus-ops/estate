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