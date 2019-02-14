import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kbj19x!%9-l$c2$b861a^^e(t$+4ff%6h74g!*+hr628ky$0-m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# 注册app
SYS_APPS = ['django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.sites',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',

            ]
# 第三方的模块注册
EXT_APPS = [
    'xadmin',
    'crispy_forms',
    'reversion',
    'haystack',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.baidu',

]
SITE_ID = 1
LOGIN_REDIRECT_URL = '/'

# 自定义功能模块注册
CUSTOM_APPS = [
    'apps.user_account',
    'apps.index',
    'apps.detail',
    'apps.order',
    'apps.search',
    'apps.car',
]

INSTALLED_APPS = SYS_APPS + EXT_APPS + CUSTOM_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'group.urls'

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
                'apps.user_account.context_processors.shop_count',
            ],
        },
    },
]

WSGI_APPLICATION = 'group.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'lingshi',
        'USER': 'root',
        'PASSWORD': 'root',
        'PORT': '3306',
        'HOST': '127.0.0.1',
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

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
# 静态文件目录配置
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'apps/user_account/static'),
)
# 配置访问多媒体的路径
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 全局登录配置
LOGIN_URL = '/user_account/login/'

# 指定用户模型
AUTH_USER_MODEL = 'index.User'

# ==============邮件配置=============
# 发送邮件的服务器地址
EMAIL_HOST = 'smtp.163.com'
# 发送邮件端口
EMAIL_PORT = 25
# 发送邮件默认的名称
EMAIL_HOST_USER = '13821671776@163.com'
# 授权码
EMAIL_HOST_PASSWORD = 'qwe123'
# 是否启用tls安全协议
EMAIL_USE_TLS = True

# 是否启用SSL安全协议
# EMAIL_USE_SSL = True
# 发送超时时间
# EMAIL_TIMEOUT =


# =============缓存配置==============
CACHES = {
    'default': {
        # 使用redis做缓存
        'BACKEND': 'django_redis.cache.RedisCache',
        # 将缓存的数据保存在该目录下
        # 缓存的地址
        'LOCATION': 'redis://127.0.0.1/1',
        # rediss: //[:password]@localhost:6379 / 0
        'TIMEOUT': 300,
        'OPTIONS': {
            # "PASSWORD": ""
            # 是否压缩缓存数据
            # "COMPRESSOR": "django_redis.compressors.zlib.ZlibCompressor",
            # 配置连接池
            "CONNECTION_POOL_KWARGS": {"max_connections": 100, "retry_on_timeout": True}
        }
    },
    'session': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1/2',
        'TIMEOUT': 300,
        'OPTIONS': {
            "CONNECTION_POOL_KWARGS": {"max_connections": 100, "retry_on_timeout": True}
        }

    }
}
# ==========session缓存配置============
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "session"
# session失效的时间 7天
SESSION_COOKIE_AGE = 7 * 24 * 60 * 60  # Session的cookie失效日期（2周） 默认1209600秒

# ==========haystack缓存配置============
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'apps.index.whoosh_cn_backend.WhooshEngine',
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
    },
}
# 自动更新索引
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor' \
 \
    # ==========支付宝相关配置============
# 注册应用时支付宝生成 app_id
APP_ID = "2016092200568044"

# 支付网关
ALT_PAY_DEV_URL = 'https://openapi.alipaydev.com/gateway.do?'

# 生产支付环境
ALI_PAY_URL = ''

# 网站私钥文件路径
APP_PRIVATE_KEY_PATH = os.path.join(BASE_DIR, 'key/app_private_key.pem')

# 支付宝公钥文件路径
ALIPAY_PUBLIC_KEY_PATH = os.path.join(BASE_DIR, 'key/alipay_public_key.pem')
# =================支付宝配置相关 end=============


# ===============
# SHOP_PRICE = 0
# ORDER_ID = ''
PAY_LIST=[]
