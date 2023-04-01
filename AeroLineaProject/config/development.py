from .base import *
#Esta configuracion debe cambiarse dependiendo si es produccion y desarrollo
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-tj_3^!anyoyw^cerm7!_kej1kqs%qd@s5+16w+yzwh)aq7x14h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True #false si es para production

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'