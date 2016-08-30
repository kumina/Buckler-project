from .django_base import *  # NOQA
import crypt

# Sample / default config

def hash_passwd(s):
    return crypt.crypt(s, '$1$xyz')

CONFIG = {'ivo': {'password': hash_passwd('1v0'),
                  'indexes': ('logstash-ivo-*',),
                  'userdata_index': 'ivo'},
          'test': {'password': hash_passwd('t3st'),
                   'indexes': ('accounts', ),
                   'userdata_index': 'test'},
          'superuser': {'password': hash_passwd('geheim'),
                        'indexes': ('accounts', 'logstash-*',
                                    'logstash-ivo-*'),
                        'userdata_index': 'superuser'},
          }

KIBANA_UPSTREAM = "http://kibana:5601"
ES_UPSTREAM = "http://es:9200"
ES_USERDATA_PREFIX = '.kibana'

try:
    from .config import *  # NOQA
except ImportError:
    pass
