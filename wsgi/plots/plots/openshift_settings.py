"""
Django settings for plots project.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
DJ_PROJECT_DIR = os.path.dirname(__file__)
BASE_DIR = os.path.dirname(DJ_PROJECT_DIR)
WSGI_DIR = os.path.dirname(BASE_DIR)
REPO_DIR = os.path.dirname(WSGI_DIR)
DATA_DIR = os.environ.get('OPENSHIFT_DATA_DIR', BASE_DIR)

import sys
sys.path.append(os.path.join(REPO_DIR, 'libs'))
import secrets
SECRETS = secrets.getter(os.path.join(DATA_DIR, 'secrets.json'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SECRETS['secret_key']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
if os.environ.get('DEBUG') is not None:
    DEBUG = os.environ.get('DEBUG') == 'True'

from socket import gethostname
ALLOWED_HOSTS = [
    gethostname(),  # For internal OpenShift load balancer security purposes.
    # Dynamically map to the OpenShift gear name.
    os.environ.get('OPENSHIFT_APP_DNS'),
    #'example.com', # First DNS alias (set up in the app)
    #'www.example.com', # Second DNS alias (set up in the app)
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'oauth2_provider',
    'rest_framework',
    'corsheaders',

    'user_auth',
    'frontend',
    'backend',
    'projects_api',
    'booking_api',
    'customer_api',
    'accounts_api',
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
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'plots.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates"), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                "django.core.context_processors.media",
                "django.core.context_processors.static",
            ],
        },
    },
]

WSGI_APPLICATION = 'plots.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'landworld',
        'USER': 'adminmVwr54P',
        'PASSWORD': 'ASm_4qe9vF3-',
        'HOST': os.environ.get('OPENSHIFT_DB_HOST'),   # Or an IP Address that your DB is hosted on
        'PORT': os.environ.get('OPENSHIFT_DB_PORT'),
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(WSGI_DIR, 'static')


AUTH_USER_MODEL = 'user_auth.User'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.ext.rest_framework.OAuth2Authentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'PAGE_SIZE': 10,
    'DATETIME_FORMAT': "%Y-%m-%d",
}

DATE_INPUT_FORMATS = "%Y-%m-%d"

CORS_ORIGIN_ALLOW_ALL = True

# OAUTH_DETAILS

CLIENT_ID = "3lyHq54PFy52dQL9455UVmSuAecL6Dl2yU3iE9jG"
CLIENT_SECRET = "WAWzw1nTFNPTGTWF6l8bxefPVQQU0S1Na1TWqyhYruwooe9ufGnpWLLsPPgs4lU8TDqYo2VAVbZlXKEdsz5Mj7TMhX3yize0pAtJxCV3kDzFHInRQkpNEwjid26h66jf"

SERVER_PROTOCOLS = "http://"

MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
MEDIA_URL = '/media/'
