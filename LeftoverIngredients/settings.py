"""
Django settings for LeftoverIngredients project.

Generated by 'django-admin startproject' using Django 3.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
#import django_heroku
from pathlib import Path
import os
from pathlib import Path

<<<<<<< HEAD
=======
import dj_database_url

# import django_heroku

>>>>>>> 3e05ae341ef2088b62886df523f1be53c46302b2
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
<<<<<<< HEAD
SECRET_KEY = "django-insecure-u03fiiz(78g6^^+2eot5yml*&f#2g7z&1i7no_bxkw^05dk2!p"
=======
SECRET_KEY = os.environ.get("SECRET_KEY", "default-key-123")
>>>>>>> 3e05ae341ef2088b62886df523f1be53c46302b2

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG_VALUE") == "TRUE"
# If local runserver is not working
# DEBUG = True
# If deloy on heroku is not working
# DEBUG = False

<<<<<<< HEAD
ALLOWED_HOSTS = ['localhost', '.herokuapp.com']
=======
ALLOWED_HOSTS = ["fathomless-cliffs-95117.herokuapp.com", "127.0.0.1", "localhost"]

ADMINS = [
    ("Anthony", "acampan000@citymail.cuny.edu"),
    ("David", "dbalaba000@citymail.cuny.edu"),
    ("Nezar", "nezarv2k@gmail.com"),
    ("test", "tttesttting6@gmail.com"),
]

# Email Settings: Setting up the account that the application is going to use to send emails from
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_USE_TLS = True
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
>>>>>>> 3e05ae341ef2088b62886df523f1be53c46302b2


# Application definition
INSTALLED_APPS = [
    "recipeComments.apps.RecipecommentsConfig",
    "main.apps.MainConfig",
    "users.apps.UsersConfig",
    "recipe.apps.RecipeConfig",
    "crispy_forms",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
<<<<<<< HEAD
#django_heroku.settings(locals(), staticfiles=False)
=======
>>>>>>> 3e05ae341ef2088b62886df523f1be53c46302b2

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "LeftoverIngredients.urls"

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
            ]
        },
    }
]

WSGI_APPLICATION = "LeftoverIngredients.wsgi.application"

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
<<<<<<< HEAD
    #"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": BASE_DIR / "db.sqlite3"}
    "default": {
                "ENGINE": "django.db.backends.postgresql_psycopg2",
                "NAME": "d5gilrqcksk06t",
                "USER": "lvegmbacyhebqj",
                "PASSWORD":"608550963ee18f65f17a56145ea4231ad6ce73d7bc5d2a0a4852aea53f515b4a",
                "HOST": "ec2-44-198-236-169.compute-1.amazonaws.com",
                "PORT":"5432", 
    }
=======
    "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": BASE_DIR / "db.sqlite3"}
    #     "default": {
    #         "ENGINE": "django.db.backends.postgresql",
    #         "NAME": "DEMO_TEST",
    #         "USER": "postgres",
    #         "PASSWORD": "0564",
    #         "HOST": "localhost",
    #         "PORT": "5432",
    #     }
>>>>>>> 3e05ae341ef2088b62886df523f1be53c46302b2
}

# Overwites default database to Heroku postgresql db
db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES["default"].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
<<<<<<< HEAD
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = "/static/"

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
=======

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_URL = "/static/"

STATICFILE_DIRS = [os.path.join(BASE_DIR, "static")]
>>>>>>> 3e05ae341ef2088b62886df523f1be53c46302b2

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

<<<<<<< HEAD
API_KEY = "9f97e9f457aa4379ba2cb4c32072aec4"  # Spoonacular API key
=======
API_KEY = os.environ.get(
    "API_KEY_SPOONACULAR"
)  # Spoonacular API key from Heroku server
# API_KEY = "9f97e9f457aa4379ba2cb4c32072aec4"  # Spoonacular API key
>>>>>>> 3e05ae341ef2088b62886df523f1be53c46302b2

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CRISPY_TEMPLATE_PACK = "bootstrap4"

LOGIN_REDIRECT_URL = "main-home"

LOGIN_URL = "login"

<<<<<<< HEAD
#django_heroku.settings(locals())

#Define COOKIE AGE for Remember me section
SESSION_COOKIE_AGE = 60 * 60 * 24 * 30 * 12 # 12 Months (Months are 30days so 360 days in total)
=======
# Define COOKIE AGE for Remember me section
# SESSION_COOKIE_AGE = (
#     60 * 60 * 24 * 30 * 12
# )  # 12 Months (Months are 30days so 360 days in total)

# AWS
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")

AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None

AWS_S3_REGION_NAME = "us-east-2"
AWS_S3_SIGNATURE_VERSION = "s3v4"

DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
# Automatically put your static files in your bucket
STATICFILES_STORAGE = "storages.backends.s3boto3.S3StaticStorage"
>>>>>>> 3e05ae341ef2088b62886df523f1be53c46302b2
