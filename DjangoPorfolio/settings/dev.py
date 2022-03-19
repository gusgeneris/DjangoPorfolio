from .base import *
from decouple import config

SECRET_KEY = config('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = ['*']

STATIC_URL = 'static/'

#STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'staticfiles'),
)




MEDIA_URL = 'media/'

MEDIA_ROOT = BASE_DIR / 'media'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}