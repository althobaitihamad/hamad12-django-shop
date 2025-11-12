from pathlib import Path
import os
import cloudinary
import cloudinary.uploader
import cloudinary.api
from dotenv import load_dotenv

# ===========================
# 🔒 تحميل المتغيرات من ملف .env
# ===========================
load_dotenv()

# ===========================
# 🧭 المسارات الأساسية
# ===========================
BASE_DIR = Path(__file__).resolve().parent.parent


# ===========================
# 🔐 مفاتيح الأمان والإعدادات العامة
# ===========================
SECRET_KEY = os.getenv('SECRET_KEY', 'fallback-secret-key')
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')


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

ROOT_URLCONF = 'hamad12.urls'


# ===========================
# 🌐 إعدادات القوالب
# ===========================
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
# 🗃️ إعداد قاعدة البيانات
# ===========================
if DEBUG:
    # 🧪 قاعدة بيانات التطوير (محلية)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    # 🚀 قاعدة بيانات الإنتاج (PostgreSQL)
    DATABASES = {
        'default': {
            'ENGINE': os.getenv('DB_ENGINE'),
            'NAME': os.getenv('DB_NAME'),
            'USER': os.getenv('DB_USER'),
            'PASSWORD': os.getenv('DB_PASSWORD'),
            'HOST': os.getenv('DB_HOST'),
            'PORT': os.getenv('DB_PORT'),
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
# 🎨 الملفات الثابتة والإعلامية
# ===========================
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'


# 🌩️ إعدادات Cloudinary
cloudinary.config(
    cloud_name=os.getenv('CLOUD_NAME'),
    api_key=os.getenv('API_KEY'),
    api_secret=os.getenv('API_SECRET'),
    secure=True
)


# ===========================
# 🔒 إعدادات الأمان للإنتاج
# ===========================
if not DEBUG:
    # فرض HTTPS
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_REDIRECT = True

    # ملفات الكوكيز الآمنة
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

    # منع تضمين الموقع داخل iframe
    X_FRAME_OPTIONS = 'DENY'

    # منع تصفح محتوى الملفات
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_BROWSER_XSS_FILTER = True

# ===========================
# ⚙️ الإعداد الافتراضي للحقول
# ===========================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
