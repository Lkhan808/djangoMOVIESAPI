import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'django123-insecure-@xww&n@zay80d&3-&$_dspfz*pb+%(8oi4q4p0j!56l#l_(%*u)'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '138.197.185.196']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'movie',
        # 'USER': 'user_db',
        # 'PASSWORD': '123456',
        # 'HOST': 'localhost',
        # 'PORT': '5432'
    }
}

#STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
#STATICFILES_DIRS = [STATIC_DIR]