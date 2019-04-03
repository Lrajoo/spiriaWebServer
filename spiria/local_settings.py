SECRET_KEY = '%_wo&kmd!-wfx&v08sgo1i%elu(rre3x)^+5z$at%tsz11mgsk'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['134.209.70.57']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'spiriadb',
        'USER': 'dbadmin',
        'PASSWORD': '123456',
        'HOST': 'localhost'
    }
}
