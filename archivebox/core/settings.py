__package__ = 'archivebox.core'

import os
import sys

SECRET_KEY = '---------------- not a valid secret key ! ----------------'
DEBUG = True
ALLOWED_HOSTS = ['*']

REPO_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), os.path.pardir, os.path.pardir))
OUTPUT_DIR = os.path.abspath(os.getenv('OUTPUT_DIR', os.curdir))
DATABASE_FILE = os.path.join(OUTPUT_DIR, 'index.sqlite3')

ACTIVE_THEME = 'default'

IS_SHELL = 'shell' in sys.argv[:3] or 'shell_plus' in sys.argv[:3]

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    # 'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.staticfiles',

    'core',

    'django_extensions',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(REPO_DIR, 'themes', ACTIVE_THEME),
            os.path.join(REPO_DIR, 'themes', 'default'),
            os.path.join(REPO_DIR, 'themes'),
        ],
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

WSGI_APPLICATION = 'core.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': DATABASE_FILE,
    }
}

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

################################################################################
### Security Settings
################################################################################
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_DOMAIN = None
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_SAVE_EVERY_REQUEST = True
SESSION_COOKIE_AGE = 1209600  # 2 weeks
LOGIN_URL = '/accounts/login/'
LOGOUT_REDIRECT_URL = '/'
PASSWORD_RESET_URL = '/accounts/password_reset/'


SHELL_PLUS = 'ipython'
SHELL_PLUS_PRINT_SQL = False
IPYTHON_ARGUMENTS = ['--no-confirm-exit', '--no-banner']
IPYTHON_KERNEL_DISPLAY_NAME = 'ArchiveBox Django Shell'
if IS_SHELL:
    os.environ['PYTHONSTARTUP'] = os.path.join(REPO_DIR, 'core', 'welcome_message.py')


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = False


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(REPO_DIR, 'themes', ACTIVE_THEME, 'static'),
    os.path.join(REPO_DIR, 'themes', 'default', 'static'),
    os.path.join(REPO_DIR, 'themes', 'static'),
]

SERVE_STATIC = True

