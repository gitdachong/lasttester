#coding:utf-8
ALLOED_FILE_TYPES = ['normal']
class Configurer(object):

    def __init__(self,config):
        self._config = config
        self._key = 'instances'
        self._results = {}
        self._instance = None

    def parse(self):
        file_type = self._config.get('file_type','normal')
        if file_type not in ALLOED_FILE_TYPES:
            file_type = 'normal'

        if file_type == 'normal':
            self._instance = open(self._config['config_body'].get('path'), self._config['config_body'].get('mode','ab+'))

        self._results[self._config.get('name')] = self._instance
        return [(self._key,self._results)]

    def close(self):
        if self._instance:
            self._instance.close()




