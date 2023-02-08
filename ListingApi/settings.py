
from pathlib import Path
import datetime


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@3(zi6(i@@sa7=7&5tw5vi4i4yyztl^(&&^wnf6oi%^%!!s_$^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['10.0.3.2','127.0.0.1', 'openport.io']

CORS_ORGIN_ALLOW_ALL=True

CORS_ALLOW_METHODS = [
'DELETE',
'GET',
'OPTIONS',
'PATCH',
'POST',
'PUT',
]


CORS_ALLOW_HEADERS = [
'accept',
'accept-encoding',
'authorization',
'content-type',
'dnt',
'origin',
'user-agent',
'x-csrftoken',
'x-requested-with',
]

CORS_ORGIN_ALLOW_ALL=True
FILE_UPLOAD_PERMISSIONS=0O640


# Application definition

INSTALLED_APPS = [
    'bootstrap4',
    'ckeditor',
    'ckeditor_uploader',
    'crispy_forms',
    'admin_volt.apps.AdminVoltConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',



    'order',
    'accounts',
    'realtors',
    'listings',
    'favorites',
    'subscriber'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ListingApi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'ListingApi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }



DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'houserental',
        'USER': 'tinsae',
        'PASSWORD': 'TESIha1817!?',
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


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/




# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
          'rest_framework_simplejwt.authentication.JWTAuthentication',  # <-- And here
    ],
    'DEFAULT_PAGINATION_CLASS':'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 4
  
    
}

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA':datetime.timedelta(days=3),
    'JWT_ALLOW_REFRESH':True
}




# STATICFILES_DIRS = [
#     BASE_DIR / "static"
# ]



CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"
CKEDITOR_UPLOAD_PATH = "uploads/"


STATIC_ROOT = BASE_DIR / 'static'
STATIC_URL = 'static/'
MEDIA_URL = '/media/'

MEDIA_ROOT =  BASE_DIR / 'media'


AUTH_USER_MODEL = 'accounts.UserAccount'


# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_USE_TLS = True
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = 'tinsingjobs2k@gmail.com'
# EMAIL_HOST_PASSWORD = 'TESIha1817!?'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
CRISPY_TEMPLATE_PACK = 'bootstrap4'



#...
SITE_ID = 1

####################################
    ##  CKEDITOR CONFIGURATION ##
####################################



