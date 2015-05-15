"""
Django settings for snippod boilerplate project.

This is a base starter for snippod.

For more information on this file, see
https://github.com/shalomeir/snippod-boilerplate

"""
from snippod_boilerplate.settings.common import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$6(x*g_2g9l_*g8peb-@anl5^*8q!1w)k&e&2!i)t6$s8kia93'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', True)

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS += (
    'debug_toolbar',
)

# MIDDLEWARE_CLASSES += (
# )


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
DATABASE_OPTIONS = {'charset': 'utf8'}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
# STATIC_URL = '/static/'
#
# STATICFILES_DIRS = (
#     # os.path.join(BASE_DIR, 'snippod_webapp/.tmp'), # grunt serve
#     os.path.join(BASE_DIR, 'snippod_webapp/dist/client'), #grunt
#     # os.path.join(BASE_DIR, 'static'),
# )
#
# COMPRESS_ENABLED = os.environ.get('COMPRESS_ENABLED', False)

AWS_HEADERS = {  # see http://developer.yahoo.com/performance/rules.html#expires
                 'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
                 'Cache-Control': 'max-age=94608000',
                 }

AWS_STORAGE_BUCKET_NAME = "s3.snipod-boilerplate.com"
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']

STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
S3_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
STATIC_URL = S3_URL

#MEDIA FILE (user uploaded files)

# TEMPLATE_DIRS = (
#     os.path.join(BASE_DIR, 'djangoapps/templates'),
# )
