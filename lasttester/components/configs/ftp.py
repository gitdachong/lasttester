#coding:utf-8
import ftplib
import sys
class Configurer(object):

    def __init__(self,config):
        self._config = config
        self._key = 'instances'
        self._results = {}
        self._instance = ftplib.FTP()

    def connect(self,_config):
        _result = self._instance.connect(_config.get('host'),int(_config.get('port',21)))
        _pasv_mode =True if _config.get('mode') ==1 else False
        self._instance.set_pasv(_pasv_mode)
        _result = self._instance.login(_config.get('username'),_config.get('password'))

    def parse(self):
        _config = self._config.get('config_body')
        self.connect(_config)
        self._results[self._config.get('name')] = self._instance
        return [(self._key,self._results)]

    def close(self):
        if self._instance:
            self._instance.quit()

    def upload(self,remotepath, localpath):
        bufsize = 1024
        fp = open(localpath, 'rb')
        _result = self._instance.storbinary('STOR ' + remotepath, fp, bufsize)
        self._instance.set_debuglevel(0)
        fp.close()

    def download(self,remotepath, localpath):
        bufsize = 1024
        fp = open(localpath, 'wb')
        self._instance.retrbinary('RETR ' + remotepath, fp.write, bufsize)
        self._instance.set_debuglevel(0)
        fp.close()



