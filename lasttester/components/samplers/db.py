#coding:utf-8
from . import base
class Sampler(base.Sampler):


    def __init__(self,test_content,**kwargs):
        super().__init__(test_content,**kwargs)
        self.sampler_name = 'db'



    def run(self):
        self.request = self.test_content.get('request')
        if not isinstance(self.request,str):
            return
        self.request = self.request.lower().strip()
        if self.request.startswith('select'):
            resp = self.instance.executeSql(self.request)
        else:
            resp = self.instance.executeCommit(self.request)

        self.response['text'] = resp
        self.response['json'] = str(resp)
        self.response['status_code'] = 200
        return self.response

