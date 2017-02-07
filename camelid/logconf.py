# -*- coding: utf-8 -*-
"""Logging configuration."""

from __future__ import unicode_literals

import sys
import logging
import logging.config

CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(asctime)s %(name)s %(levelname)s %(message)s',
            'style': '%'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'default',
            'stream': sys.stdout
        }
    },
    'loggers': {
        'camelid': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False
        },
        # 'camelid.googlesheet': {
        #     'level': 'DEBUG',
        #     'handlers': ['console'],
        #     'propagate': False
        # },
        # 'camelid.cmgroup': {
        #     'level': 'DEBUG',
        #     'handlers': ['console'],
        #     'propagate': False
        # },
        # 'camelid.pubchemutils': {
        #     'level': 'DEBUG',
        #     'handlers': ['console'],
        #     'propagate': False
        # },
        'pubchempy': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False
        }
    },
    'root': {
        'level': 'DEBUG',
        'handlers': []
    }
}

logging.config.dictConfig(CONFIG)
