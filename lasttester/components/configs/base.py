#coding:utf-8

class Configurer(object):

    def __init__(self,config):
        self._config = config
        self._key = self._config.get('type','common')

    def parse(self):
        return [(self._key,self._config.get('config_body'))]

    def close(self):
        pass


