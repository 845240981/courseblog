# -*- coding: UTF-8 -*-
"""
Django settings for courseblog project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0,os.path.join(BASE_DIR,'apps'))
sys.path.insert(0,os.path.join(BASE_DIR,'extra_apps'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9(jkzyucmlne)c=q8qb)(gg^^@mfa_0s%%908%-8x7^^pmles%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []



USE_TZ = True
# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'courses',
    'organization',
    'operation',
    'xadmin',
    'crispy_forms',
    'captcha',
'pure_pagination',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

#在暗中，Django维护一个”authentication backends”的列表用来测试认证。当某人调用 django.contrib.auth.authenticate() — 上面提到的”如何登录一个用户” — Django将尝试所有的认证后端。如果第一个认证方法失败了，Django将会继续尝试第二个，直到所有的都被尝试过。

#认证后端的列表在 AUTHENTICATION_BACKENDS 设置。内容应该是包含Python路径的元组。
#自定义认证后端
AUTHENTICATION_BACKENDS=(
    'users.views.DefineBackend',
)
AUTH_USER_MODEL = 'users.Userprofile'
#自定义userprofile来覆盖默认user表

ROOT_URLCONF = 'courseblog.urls'


WSGI_APPLICATION = 'courseblog.wsgi.application'


# Databasem
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'coursedatabase',
        'USER': 'root',
        'PASSWORD':'pk123456',
        'HOST':'127.0.0.1',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_PATH =os.path.join(BASE_DIR,'static')
STATIC_URL = '/static/'

STATICFILES_DIRS =(


    STATIC_PATH,


)
#TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')

#TEMPLATE_DIRS = (TEMPLATE_PATH,)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.qq.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = '845240981@qq.com'
EMAIL_HOST_PASSWORD = 'wbawkelpssoubahd'
EMAIL_FROM= '845240981@qq.com'
EMAIL_USE_TLS = True


MEDIA_URI = '/media/'
MEDIA_ROOT= os.path.join(BASE_DIR,'media')


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
                'django.core.context_processors.media',##is for template {{media url}}
            ],
        },
    },
]
