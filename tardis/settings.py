DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
  ('Nelly Hateva', 'nelly.hateva@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/home/nelly/University/Python/tardis/db'
    }
}

ALLOWED_HOSTS = []

TIME_ZONE = 'Europe/Sofia'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = False
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = ''
MEDIA_URL = ''
STATIC_ROOT = ''
STATIC_URL = '/static/'

STATICFILES_DIRS = (
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = '*ym-24e%#ey2s^azcj#n#o05zc@1nw+vx(gy7^thi8-ekk614@'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'tardis.urls'

WSGI_APPLICATION = 'tardis.wsgi.application'

TEMPLATE_DIRS = (
    '/home/nelly/University/Python/tardis/templates'
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'projects'
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
