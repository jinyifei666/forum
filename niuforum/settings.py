"""
Django settings for niuforum project.

Generated by 'django-admin startproject' using Django 1.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(ROOT_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#8x8t+9cq#7d(fhj5f7nl8$b#kes4o-b2*7lk%#p_05+569u@v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost',
                 '127.0.0.1',]


# Application definition

INSTALLED_APPS = [
    'niuauth',
    'forum',
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.google',
]




MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'niuforum.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
                 os.path.join(BASE_DIR, 'templates', 'allauth'),
                 os.path.join(BASE_DIR, 'templates'),
                 ],
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

WSGI_APPLICATION = 'niuforum.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'niuforum.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'zh_CN'
# LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

USE_TZ = True

INTERNAL_IPS = (
    '0.0.0.0',
    '127.0.0.1',
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

LOGIN_REDIRECT_URL = '/'

SITE_ID = 1

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format' : '[%(asctime)s] %(levelname)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'request': {
            'format' : '[%(asctime)s] %(levelname)s %(module)s %(process)d %(thread)d %(status_code)s %(request)s %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level':'INFO',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, "logs", "niutool.log"),
            'maxBytes': 1024*1024*5, # 5 MB
            'backupCount': 10,
            'formatter':'standard',
        },  
        'request_handler': {
            'level':'INFO',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, "logs", "request.log"),
            'maxBytes': 1024*1024*5, # 5 MB
            'backupCount': 10,
            'formatter':'request',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['default'],
            'propagate': True
        },
        'django.request': {
            'handlers': ['request_handler'],
            'propagate': False
        },
    },
}

ACCOUNT_EMAIL_REQUIRED = True
SOCIALACCOUNT_QUERY_EMAIL = False
SOCIALACCOUNT_EMAIL_REQUIRED = False
SOCIALACCOUNT_AUTO_SIGNUP = False

#电子邮件

ACCOUNT_ACTIVATION_DAYS=7

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST='smtp.sina.com'                   #SMTP地址

EMAIL_PORT='587'

EMAIL_HOST_USER='jinyifei1020@sina.com'

EMAIL_HOST_PASSWORD='******'

EMAIL_USE_TLS=True

DEFAULT_FROM_EMAIL='jinyifei1020@sina.com'

#管理员站点

SERVER_EMAIL = 'jinyifei1020@sina.com'

REP_USER_INIT = 1
REP_TOPIC_REPLY = 2
REP_TOPIC_LIKE = 3
REP_TOPIC_STAR = 4
REP_SPAM = 5

REP_GET_SETTING = {
    REP_USER_INIT: 10,
    REP_TOPIC_REPLY: 2,
    REP_TOPIC_LIKE: 5,
    REP_TOPIC_STAR: 10,
    REP_SPAM: -100
}

USER_CREATE_TOPIC = 1
REP_NEED_SETTING = {
    USER_CREATE_TOPIC: 10,
}
