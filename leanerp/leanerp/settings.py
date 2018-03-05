"""
Django settings for leanerp project.

Generated by 'django-admin startproject' using Django 1.11.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')^^5bh)gx%e*bo4&br9iu62pq(l91ac#^cdx8l1kv5ss))n8un'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 3rd party
    'rest_framework',
    'notifications',
    # erp modules
    'erpadmin',
    'storehouse',
    'helpdesk',
    'maintenance_mgmt',
    'advertisement_mgmt',
    'inventorycheck',
    'customer_mgmt',
    'api_v1'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'leanerp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, os.sep.join(['leanerp', 'templates'])).replace('\\', '/')],
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

WSGI_APPLICATION = 'leanerp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, os.sep.join(['leanerp', 'static'])).replace('\\', '/'),
    os.path.join(BASE_DIR, os.sep.join(['leanerp', 'leanerp', 'static'])).replace('\\', '/'),
    os.path.join(BASE_DIR, os.sep.join(['leanerp', 'erpadmin', 'static'])).replace('\\', '/'),
    os.path.join(BASE_DIR, os.sep.join(['leanerp', 'inventorycheck', 'static'])).replace('\\', '/'),
    os.path.join(BASE_DIR, os.sep.join(['leanerp', 'maintenance_mgmt', 'static'])).replace('\\', '/'),
    os.path.join(BASE_DIR, os.sep.join(['leanerp', 'advertisement_mgmt', 'static'])).replace('\\', '/'),
    ]

# Setting for Django Notification to allow additional data attached
NOTIFICATIONS_USE_JSONFIELD = True

# Allows multiple projects to share a single database
# * required by helpdesk
SITE_ID = 1

# Django Helpdesk settings
# * overwrites the HELPDESK_DEFAULT_SETTINGS in helpdesk/settings.py
HELPDESK_DEFAULT_SETTINGS = {
        'use_email_as_submitter': False,
        'email_on_ticket_assign': False,
        'email_on_ticket_change': False,
        'login_view_ticketlist': True,
        'tickets_per_page': 25
        }

# Django-dbbackup settings
DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
DBBACKUP_STORAGE_OPTIONS = {'location': './sqlite_backups'}

# Static file
MEDIA_ROOT = 'media'
MEDIA_URL = '/media/'