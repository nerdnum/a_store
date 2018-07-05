from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY', default='yop7dn&n0mu$esd8s^t3$@fstk#7dxj@%qq(rxov8h^&3g)erd')


DEBUG = env.bool('DJANGO_DEBUG', default=True)