#coding:utf-8
from . import base

class Sampler(base.Sampler):


    def __init__(self,test_content,**kwargs):
        super().__init__(test_content)
        self.sampler_name = 'db'
        if 'instance' in kwargs:
            self.__instance = kwargs.get('instance')
        if not self.__instance:
            raise Exception(r"Database instance {} doesn't exists".format(self.test_content.get('instance')))


    def run(self):
        self.request = self.test_content.get('request')
        if not isinstance(self.request,str):
            return
        self.request = self.request.lower().strip()
        if self.request.startswith('select'):
            resp = self.__instance.executeSql(self.request)
        else:
            resp = self.__instance.executeCommit(self.request)

        self.response['text'] = resp
        self.response['json'] = str(resp)
        self.response['status_code'] = 200
        return self.response

