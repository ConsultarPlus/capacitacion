"""
Django settings for formula project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os, ssl
from pathlib import Path
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-*j)f4!r#ayh$b19kfhme3w&i-398da9py7$bjgf(=dndwst_uv'

test = False  # Esto sirve para poder hacer pruebas con DEBUG = False cargando configuraciones de prueba
DEBUG = True

if not DEBUG and not test:
    BASE_DIR = '/var/www/formula'
    archivo_conf = '/var/www/formula/conf_produccion.txt'
else:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # During development only
    archivo_conf = 'conf_debug.txt'

if not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
    ssl._create_default_https_context = ssl._create_unverified_context

txt = open(archivo_conf, 'r')
conf = txt.read()
conf = eval(conf)

SECRET_KEY = conf['SECRET_KEY']
DB = conf['DB']
USER = conf['USER']
PASSWORD = conf['PASSWORD']
HOST = conf['HOST']
PORT = conf['PORT']
EMAIL_HOST = conf['EMAIL_HOST']
EMAIL_PORT = conf['EMAIL_PORT']
EMAIL_HOST_USER = conf['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = conf['EMAIL_HOST_PASSWORD']
EMAIL_USE_TLS = conf['EMAIL_USE_TLS']
EMAIL_USE_SSL = conf['EMAIL_USE_SSL']

ALLOWED_HOSTS = ['127.0.0.1', '192.168.1.32', '190.193.200.120']


# Application definition
PROJECT_APPS = [
    'tabla',
    'menu',
    'documentos',
    'numeradores',
    'perfiles',
    'mensajes',
    'administracion',
    'localidades',
    'contabilidad',
    'finanzas'
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'axes',
    'tinymce',
    'crispy_forms',
] + PROJECT_APPS

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django_session_timeout.middleware.SessionTimeoutMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'axes.middleware.AxesMiddleware',
]

# https://pypi.org/project/django-session-timeout/
SESSION_EXPIRE_SECONDS = 3600  # 3600 = 1 hora
SESSION_EXPIRE_AFTER_LAST_ACTIVITY = True
SESSION_COOKIE_AGE = 43200  # 12 hs
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
CSRF_COOKIE_SECURE = True
# Handle session is not Json Serializable
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

ROOT_URLCONF = 'capacitacion.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'menu.context_processors.menu_processor',
            ],
        },
    },
]

WSGI_APPLICATION = 'capacitacion.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DB,
        'USER': USER,
        'PASSWORD': PASSWORD,
        'HOST': HOST,
        'PORT': PORT
    }

}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TIME_ZONE = 'America/Buenos_Aires'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
if not DEBUG and not test:
    STATIC_ROOT = '/var/www/formula/static/'
else:
    STATIC_ROOT = os.path.join(BASE_DIR, "root")
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

# '/var/www/static/',

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

# Add to your settings file
CONTENT_TYPES = ['image', 'video', 'pdf', 'doc', 'vnd.ms-excel', 'ods', 'odt', 'png', 'jpeg']
# 2.5MB - 2621440
# 5MB - 5242880
# 10MB - 10485760
# 20MB - 20971520
# 50MB - 5242880
# 100MB 104857600
# 250MB - 214958080
# 500MB - 429916160
MAX_UPLOAD_SIZE = "5242880"

# setting: APPEND_SLASH

# LOGIN_REDIRECT_URL = 'menu'
LOGIN_URL = 'ingresar'
LOGIN_REDIRECT_URL = 'menu'
DATE_INPUT_FORMATS = ('%d-%m-%Y', '%Y-%m-%d')
DATE_OUTPUT_FORMATS = ('%d-%m-%Y', '%Y-%m-%d')

# Configuración de tinyMCE
# Ver https://www.tiny.cloud/docs/plugins/
# Ver http://romanvm.github.io/django-tinymce4-lite/configuration.html
TINYMCE_DEFAULT_CONFIG = {'selector': 'textarea',
                          'branding': False,
                          'theme': 'modern',
                          'plugins': 'link image preview codesample contextmenu table code lists hr '
                                     'fullscreen textcolor',
                          'toolbar1': 'formatselect | bold italic underline forecolor backcolor | '
                                      'alignleft aligncenter alignright alignjustify | bullist numlist | '
                                      'outdent indent | table | link image | '
                                      'codesample | preview code | hr | save',
                          'contextmenu': 'formats | link image | fullscreen',
                          'menubar': "view",
                          'inline': False,
                          'statusbar': True,
                          'width': 'auto',
                          'height': 180,
                          'relative_urls': False,
                          'remove_script_host': False,
                          'convert_urls': True,
                          }

AUTHENTICATION_BACKENDS = [
    # AxesBackend should be the first backend in the AUTHENTICATION_BACKENDS list.
    'axes.backends.AxesBackend',

    # Django ModelBackend is the default authentication backend.
    'django.contrib.auth.backends.ModelBackend',
]


# Control de acceso (https://django-axes.readthedocs.io/)
AXES_ENABLED = True
AXES_FAILURE_LIMIT = 6
AXES_LOCK_OUT_AT_FAILURE = True
AXES_ONLY_USER_FAILURES = True
if not DEBUG:
    AXES_COOLOFF_TIME = timedelta(days=0, hours=0, minutes=1)
AXES_LOCKOUT_TEMPLATE = os.path.join(BASE_DIR, 'templates') + '/registration/lockout.html'
AXES_IP_BLACKLIST = None  # Ejemplo ['192.168.1.10']
AXES_IP_WHITELIST = None  # Ejemplo ['192.168.1.10']
AXES_RESET_ON_SUCCESS = True

GRAPH_MODELS = {
  'all_applications': True,
  'group_models': True,
}