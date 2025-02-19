import os
from pathlib import Path
from decouple import config


# Base directory path
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
CONTACT_EMAIL = config('CONTACT_EMAIL')

# Security settings
SECRET_KEY = 'django-insecure-o8rf%xt$i8)om80tv48q*$o-70h*##_1h&=((#!40j1y#0bkz0'
DEBUG = True
ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home_page',
    'accounts',
    'about_us',
    'contact_us',
    'favorites',
    'recipes_combined',
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
ROOT_URLCONF = 'recipes.urls'

# Template settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
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
WSGI_APPLICATION = 'recipes.wsgi.application'

# Database settings
DATABASES = {
    'default': {
        'ENGINE': os.environ.get("MONGO_ENGINE", 'djongo'),
        'NAME': os.environ.get("MONGO_DATABASE_NAME", 'all_recipes'),
        'CLIENT': {
            'host': os.environ.get("MONGO_HOST", 'localhost'),
            'port': os.environ.get("MONGO_PORT", 27017),
            'username': os.environ.get("MONGO_USER", 'aymansalman'),
            'password': os.environ.get("MONGO_PASSWORD", 'ayman123$'),
            'authSource': os.environ.get("MONGO_AUTH_SOURCE", 'admin'),
        }
    }
}
print("Database settings:", DATABASES)

# Password validation
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = 'static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'assets'),)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Email configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'morphisec.testmail@gmail.com'
EMAIL_HOST_PASSWORD = 'yjvy qduo kuip oxhu' # instead of Testmail@