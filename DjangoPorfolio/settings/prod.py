#  import django_on_heroku
from decouple import config

from .base import *

SECRET_KEY = config('SECRET_KEY')

# ROOT_URLCONF = 'DjangoPorfolio.urls'
# print(ROOT_URLCONF)
DEBUG = False

ALLOWED_HOSTS = ['djangoporfolio.onrender.com','guss.website', 'www.guss.website']
# mysql -hmonorail.proxy.rlwy.net -uroot -p51hfAgB416EcfH2BdF2GHbgb-f2Cbhbh --port 57839 --protocol=TCP railway

# DATABASES = {
#     'default': {
#         'ENGINE':'django.db.backends.mysql',
#         'NAME':'railway',
#         'USER':'root',
#         'PASSWORD':'51hfAgB416EcfH2BdF2GHbgb-f2Cbhbh',
#         'HOST':'hmonorail.proxy.rlwy.net',
#         'PORT':57839,
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'porfolio_wevg',
#         'USER': 'porfolio_wevg_user',
#         'PASSWORD': 'qc1bmYAMtW9MCAirNRcyQY1YJZFLjh32',
#         'HOST': 'dpg-cr3r11bqf0us73ecvao0-a',
#         'PORT': '5432',
#     }
# }

# Amazon S3 Settings

AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')

AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')

AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')

AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

# AWS_DEFAULT_ACL = 'public-read'

AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}

AWS_LOCATION = 'static'

AWS_QUERYSTRING_AUTH = False

AWS_HEADERS = {'Access-Control-Allow-Origin': '*'}

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_S3_FILE_OVERWRITE = False

STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'

MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]


# Heroku Logging

DEBUG_PROPAGATE_EXCEPTIONS = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'MYAPP': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    }
}

# Heroku Settings

COLLECTFAST_STRATEGY = "collectfast.strategies.boto3.Boto3Strategy"

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
    'collectfast': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'collectfast_cache',
        'TIMEOUT': 60,
        'OPTIONS': {
            'MAX_ENTRIES': 9999
        },
    },
}
COLLECTFAST_CACHE = 'collectfast'

# django_on_heroku.settings(locals(), staticfiles=False)
#del DATABASES['default']['OPTIONS']['sslmode']
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Ensure the `STATICFILES_DIRS` is properly set
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]