from .base import *


DEBUG = False
SECRET_KEY = 'django-insecure-$ov&emfc3p_6_%9e%%0*7@0^eb65)3*aq+5pp9l)rck#@=^9mm'


DATABASES = {
  "default": {
    "ENGINE": "django.db.backends.postgresql",
    "NAME": "blogclase",
    "USER":  "adminblog",
    "PASSWORD":"password",
    "HOST": "localhost",
    "PORT": "5432",
  }
}

# ARREGLAR
ALLOWED_HOSTS = ['*'] 
try:
    from .local import *
except ImportError:
    pass
