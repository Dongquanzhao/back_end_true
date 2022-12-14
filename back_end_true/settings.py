"""
Django settings for back_end_true project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
import sys
import datetime

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
sys.path.insert(0, os.path.join(BASE_DIR, 'extra_apps'))


ALLOWED_HOSTS = []

AUTH_USER_MODEL = 'users.UserProfile'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$x6nq41sx^5w*o-=(f6#&2xoqu4+gst2vn8c(w2%)b&7_ik0*-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True



# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.users.apps.UsersConfig',
    'goods.apps.GoodsConfig',
    'trade.apps.TradeConfig',
    'user_operation.apps.UserOperationConfig',
    'DjangoUeditor',
    'xadmin',
    'crispy_forms',
    'django.contrib.admin',
    'rest_framework',
    'django_filters',
    'corsheaders',
    'rest_framework.authtoken',
    'social_django'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'back_end_true.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # ?????????????????????
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'back_end_true.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'game_mall', # ???????????????
#         'USER': 'root',
#         'PASSWORD': '2298315584',
#         'HOST': '127.0.0.1', # ??????
#         'PORT': 3306,
#         'OPTIONS': {'init_command': 'SET default_storage_engine=INNODB;'}
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'fruitshop', # ???????????????
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '192.168.56.10', # ??????
        'PORT': 3306,
        'OPTIONS': {'init_command': 'SET default_storage_engine=INNODB;'}
    }
}



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

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# # DRF??????
# REST_FRAMEWORK = {
#     'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
#     'PAGE_SIZE': 10,
# }

# DRF??????
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    # 'DEFAULT_THROTTLE_CLASSES': [
    #     'rest_framework.throttling.AnonRateThrottle',
    #     'rest_framework.throttling.UserRateThrottle'
    # ],
    # 'DEFAULT_THROTTLE_RATES': {
    #     'anon': '2/minute',
    #     'user': '3/minite'
    # }
}


# ???????????????????????????
AUTHENTICATION_BACKENDS = [
    'users.views.CustomBackend',
    'social_core.backends.weibo.WeiboOAuth2',       # ????????????
    'social_core.backends.qq.QQOAuth2',             # QQ??????
    'social_core.backends.weixin.WeixinOAuth2',     # ????????????
    'django.contrib.auth.backends.ModelBackend',
]

# JWT??????
JWT_AUTH = {
    # ????????????
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=7),
    # ??????????????????
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=30),
    # ???????????????
    'JWT_AUTH_HEADER_PREFIX': 'JWT',
}

# ??????????????????
CORS_ORIGIN_ALLOW_ALL = True

# ?????????????????????????????????
REGEX_MOBILE = '^1[35789]\d{9}$|^147\d{8}$'

# ?????????APIKEY
APIKEY = 'edf71361381f31b3957beda37f20xxxx'

# ?????????????????????
app_private_key_path = os.path.join(BASE_DIR, 'apps/trade/keys/app_private.txt')
alipay_public_key_path = os.path.join(BASE_DIR, 'apps/trade/keys/ali_public.txt')
ali_app_id = "2021000116666333"
return_url = 'http://127.0.0.1:8000/alipay/return/'
notify_url = 'http://127.0.0.1:8000/alipay/return/'

# # drf-extensions??????
# REST_FRAMEWORK_EXTENSIONS = {
#     'DEFAULT_CACHE_RESPONSE_TIMEOUT': 5
# }

# Redis????????????
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://192.168.56.10:6379",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}


# ???????????????????????????????????????????????????????????????
SOCIAL_AUTH_WEIBO_KEY = 'xxxxxxx'
SOCIAL_AUTH_WEIBO_SECRET = 'xxxxxx'

SOCIAL_AUTH_QQ_KEY = 'xxxxxxx'
SOCIAL_AUTH_QQ_SECRET = 'xxxxxxx'

SOCIAL_AUTH_WEIXIN_KEY = 'xxxxxxx'
SOCIAL_AUTH_WEIXIN_SECRET = 'xxxxxxx'

# ??????????????????????????????
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/index/'