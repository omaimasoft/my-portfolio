
# =====================================================
# BASE
# =====================================================

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("mm3cnyv1!mm_j!50!z^65hbkfntvkk*d%@=vug!!17cc%t4=3%")
DEBUG = os.environ.get("DJANGO_DEBUG", "True") == "True"

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    "192.168.31.144",
    "omaimasoft.com",
    "www.omaimasoft.com",
    "omaimaboustik.pythonanywhere.com",
]
# مهم لطلبات POST/CSRF على HTTPS
CSRF_TRUSTED_ORIGINS = [
    "https://omaimasoft.com",
    "https://www.omaimasoft.com",
    "https://omaimaboustik.pythonanywhere.com",
]

# PythonAnywhere proxy (مفيد مع HTTPS)
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# Cookies آمنة فالإنتاج
if not DEBUG:
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = "SAMEORIGIN"
    # إذا فعلتي Force HTTPS من PythonAnywhere، ما تحتاجيش Django يدير redirect
    # SECURE_SSL_REDIRECT = True  # اختياري إذا بغيتي من Django

# =====================================================
# APPS
# =====================================================
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "django.contrib.sitemaps",
    "django.contrib.sites",

    "projects",
    "designs",
    "printed",
]

SITE_ID = 1

# =====================================================
# MIDDLEWARE
# =====================================================
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# =====================================================
# URLS / WSGI
# =====================================================
ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"

# =====================================================
# TEMPLATES
# =====================================================
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",  # مهم للسيو/meta
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# =====================================================
# DATABASE
# =====================================================
# دابا SQLite مزيانة، تقدر تخليها فالأول على PythonAnywhere
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# =====================================================
# PASSWORD VALIDATION
# =====================================================
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# =====================================================
# INTERNATIONALIZATION
# =====================================================
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Africa/Casablanca"
USE_I18N = True
USE_TZ = True

# =====================================================
# STATIC / MEDIA
# =====================================================
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]   # الملفات الأصلية (css/js/images)
STATIC_ROOT = BASE_DIR / "staticfiles"     # collectstatic غادي يجمع هنا

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# =====================================================
# DEFAULT PK
# =====================================================
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"