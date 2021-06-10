from .base import *


ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'sold_goods',
        'USER': 'root',
        'PASSWORD': '1111',
        'HOST': 'localhost',
        'PORT': 5432
    }
}
