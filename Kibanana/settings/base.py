from .django_base import *

## Sample / default config

CONFIG = { 'ivo': {'password':'1v0',
                   'indexes': ('logstash-ivo-*',)},
           'test': {'password': 't3st',
                    'indexes': ('accounts', )},
           'superuser': {'password': 'geheim',
                         'indexes':('accounts', 'logstash-*', 'logstash-ivo-*')}
         }

KIBANA_UPSTREAM = "http://kibana:5601"
ES_UPSTREAM = "http://es:9200"

try:
    from .config import *
except ImportError:
    pass

