"""
Django settings for ecourseapiv1 project.

Generated by 'django-admin startproject' using Django 4.2.11.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

MEDIA_ROOT = '%s/courses/static/' % BASE_DIR
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-f78@(q)48(i)2z*^0gci@v5ift8@nw7fk3^+9t@1j_%k0fp8&x"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition
import pymysql

pymysql.install_as_MySQLdb()

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "courses",
    'ckeditor',
    'ckeditor_uploader',
    'rest_framework',
    'drf_yasg',
    'oauth2_provider'
]

REST_FRAMEWORK = {
'DEFAULT_AUTHENTICATION_CLASSES': ('oauth2_provider.contrib.rest_framework.OAuth2Authentication',)
}

CKEDITOR_UPLOAD_PATH = "/ckeditors/images/"
AUTH_USER_MODEL = 'courses.User'

import cloudinary

cloudinary.config(
    cloud_name="dstatzhgd",
    api_key="998995365372546",
    api_secret="bA9rjeupCc71tjfiqsOy1OoA9hY"
)
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "ecourseapiv1.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "ecourseapiv1.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'K21coursedb',
        'USER': 'root',
        'PASSWORD': 'Admin@123',
        'HOST': ''  # mặc định localhost
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator", },
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator", },
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator", },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CLIENT_ID = 'X1Vtk4kY8UFciSMNogKKfxcKyWcLnnN8chlYmDOa'
CLIENT_SECRET = 'Jp6HmTWWjwMJmghmI5A5rfJjhV3SE148ZVeqJ8fZk29LVYR0LTY660rgVGC93VyCvpKmGgJzDLKtBEtsvIzluXZB0YWh4HWqtKSu3W52r7PKuzewY2bnhQJLuuBl9whT'