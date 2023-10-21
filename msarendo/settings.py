from pathlib import Path
import os 
from dotenv import load_dotenv
import cloudinary
import django_heroku
import dj_database_url

env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = str(os.getenv('SECRET_KEY'))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DEBUG = True
MODE = 'dev'
ALLOWED_HOSTS = ['msarendo.herokuapp.com', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    "django.contrib.postgres", 
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'msarendo.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'msarendo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
if MODE == 'dev':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
                'NAME': str(os.getenv("NAME")),
                'USER': str(os.getenv("USER")),
                'PASSWORD': str(os.getenv("PASSWORD")),
                'HOST': str(os.getenv("HOST")),
                'PORT':os.getenv("PORT")
        }
    }
else:
    DATABASES = {
       'default': dj_database_url.config( default=str(os.getenv('DATABASE_URL')))
    }

db_from_env = dj_database_url.config(conn_max_age=0, ssl_require=False)
DATABASES['default'].update(db_from_env)


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

cloudinary.config( 
    cloud_name = str(os.getenv('CLOUD_NAME')),
    api_key = str(os.getenv('API_KEY')),
    api_secret = str(os.getenv('API_SECRET')),
)

EMAIL_USE_TLS = True
EMAIL_HOST= str(os.getenv('EMAIL_HOST'))
EMAIL_PORT= int(os.getenv('EMAIL_PORT'))
EMAIL_HOST_USER= str(os.getenv('EMAIL_HOST_USER'))
EMAIL_HOST_PASSWORD= str(os.getenv('EMAIL_HOST_PASSWORD'))

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

django_heroku.settings(locals() ,databases=False)