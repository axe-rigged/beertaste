"""
Django settings for beertaste project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
# Should just add huge if DEBUG and then settings different

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
if DEBUG:
    with(open("/etc/secretkey.txt") as x):
        SECRET_KEY = x.read().strip()
else:
    SECRET_KEY = os.environ.get('DJANGO_SECRET')

# Host can be domain name or IP
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
# CORS maybe needed

# Application definition

INSTALLED_APPS = [
    'tailwind',
    'theme',
    'django_browser_reload',
    'sites.apps.SitesConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    "django_browser_reload.middleware.BrowserReloadMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'beertaste.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "beertaste/templates",],
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

WSGI_APPLICATION = 'beertaste.wsgi.application'

#Develpoment server for tailwind
TAILWIND_APP_NAME = "theme"
INTERNAL_IPS = ["127.0.0.1",]

# Access from other origins
# CSRF_TRUSTED_ORIGINS = ["http://127.0.0.1", "http://127.0.0.1"]

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
# Maybe create databases to /var/www/beer/media and /static for nginx
# Make mariadb that can be used later with container or have ready to go option.
if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ.get('DATABASE_NAME'),
            'USER': os.environ.get('DATABAE_USER'),
            'PASSWORD': os.environ.get('DATABAE_PASS'),
            'HOST': 'database',
            'PORT': 5432
        }
    }

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# We need to have https for this to work
# CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
# /var/www/beer/media+/images, statics
# You can change MEDIA_root directory somewhere else but make sure that nginx has rights to write there
STATICFILES_DIRS = [
        BASE_DIR / "beertaste/static/",
        BASE_DIR / "sites/static/",
        BASE_DIR / "theme/static/",
        ]
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
#Tarkista tarvitseeko olla os.path.join vai uudella 4.0 tavalla(taita jokin 3.0)
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
