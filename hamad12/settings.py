from pathlib import Path
import os
import cloudinary
import cloudinary.uploader
import cloudinary.api

# ===========================
# 🧭 المسارات الأساسية
# ===========================
BASE_DIR = Path(__file__).resolve().parent.parent


# ===========================
# 🔐 مفاتيح الأمان والإعدادات العامة
# ===========================
SECRET_KEY = 'django-insecure-6#zt7)7o3sh9-k)1g6iq1s0&*e7pfhk*#umd-hoik8vs9o*12^'
DEBUG = True
ALLOWED_HOSTS = []


# ===========================
# ⚙️ التطبيقات المثبتة
# ===========================
INSTALLED_APPS = [
    # تطبيقات Django الافتراضية
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # تطبيقات المشروع
    'core',
    'store',
    'orders',

    # 🌩️ مكتبة Cloudinary
    'cloudinary',
    'cloudinary_storage',
]


# ===========================
# 🧩 الميدلوير (Middleware)
# ===========================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ===========================
# 🌐 إعدادات القوالب
# ===========================
ROOT_URLCONF = 'hamad12.urls'

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

WSGI_APPLICATION = 'hamad12.wsgi.application'


# ===========================
# 🗃️ قاعدة البيانات
# ===========================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ===========================
# 🔑 التحقق من كلمات المرور
# ===========================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# ===========================
# 🌍 اللغة والمنطقة الزمنية
# ===========================
LANGUAGE_CODE = 'ar'
TIME_ZONE = 'Asia/Riyadh'
USE_I18N = True
USE_TZ = True


# ===========================
# 🎨 الملفات الثابتة
# ===========================
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'


# ===========================
# 🖼️ الملفات الإعلامية (Cloudinary)
# ===========================
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'

# 🌩️ إعدادات Cloudinary
cloudinary.config(
    cloud_name='dnvdipjtp',
    api_key='783998442557899',
    api_secret='ayR4ieuNGOk3ztqEn1_PfB25bQY',
    secure=True
)


# ===========================
# ⚙️ الإعداد الافتراضي للحقول
# ===========================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
