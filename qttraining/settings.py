"""
Django settings for qttraining project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z1=uw3r$8$qemar4ijn(2ra-(r3kf+1hds1b-=wfxkg#f7_xpe'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mongoengine.django.mongo_auth',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'qttraining.urls'

WSGI_APPLICATION = 'qttraining.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.dummy',
    }
}

MONGODB_DATABASES = {
    'default': {'name': 'mongoengine'}
}


from mongoengine import connect
connect("qttraining")
#connect("whoclouder")
#mongo ds043220.mongolab.com:43220/whoclouder -u <dbuser> -p <dbpassword>
#connect("whoclouder", host="ds043220.mongolab.com", port=43220, username='whoclouder', password='test')
#connect("ahmad88me_whoclouder", host="mongodb-ahmad88me.alwaysdata.net", username="ahmad88me", password="000000")
#mongodb-ahmad88me.alwaysdata.net/ahmad88me_whoclouder -u ahmad88me@gmail.com -p 000000


AUTHENTICATION_BACKENDS = (
    'mongoengine.django.auth.MongoEngineBackend',
)

AUTH_USER_MODEL = 'mongo_auth.MongoUser'
SESSION_ENGINE = 'mongoengine.django.sessions'
MONGOENGINE_USER_DOCUMENT = 'mongoengine.django.auth.User'
SESSION_SERIALIZER = 'mongoengine.django.sessions.BSONSerializer'


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
