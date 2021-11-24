"""
custom settings not versioned settings
"""

from .settings import DEBUG


# use mysql so we test database transactions correctly
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_oscar',
        'USER': 'django',
        'PASSWORD': 'django',
        'HOST': '',
        'PORT': '',
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'requests': {
            'handlers': ['console'],
            'level': 'DEBUG' if DEBUG is True else 'INFO',
            'propagate': True,
        },
        'oscar': {
            'handlers': ['console'],
            'level': 'DEBUG' if DEBUG is True else 'INFO',
        },
        'tropipay': {
            'handlers': ['console'],
            'level': 'DEBUG' if DEBUG is True else 'INFO',
        },
    },
}
