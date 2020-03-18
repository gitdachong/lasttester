#coding:utf-8
from . import base
ALLOED_FILE_TYPES = ['normal']

class Configurer(base.Configurer):

    def __init__(self,config):
        self._config = config
        self._key = '__lasttester_configurers'
        self._results = {}

    def parse(self):
        file_type = self._config.get('file_type','normal')
        if file_type not in ALLOED_FILE_TYPES:
            file_type = 'normal'

        if file_type == 'normal':
            self.instance = open(self._config['config_body'].get('path'), self._config['config_body'].get('mode','ab+'))

        self._results[self._config.get('name')] = self
        return [(self._key,self._results)]

    def close(self):
        if self.instance:
            self.instance.close()




