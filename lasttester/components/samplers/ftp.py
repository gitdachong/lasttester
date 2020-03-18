#coding:utf-8
from . import base
ALLOWED_METHOD = ['upload','download','delete']
class Sampler(base.Sampler):


    def __init__(self,test_content,**kwargs):
        super().__init__(test_content,**kwargs)
        self.sampler_name = 'ftp'
        if not self.instance:
            raise Exception("instance doesn't exists")

    def run(self):
        self.request = self.test_content.get('request',{})
        self.request['text'] = str(self.request)
        _method_name = self.request.get('method','').lower()
        if _method_name not in ALLOWED_METHOD:
            raise Exception('Fto Sampler do not allow {} method'.format(_method_name))
        _method = getattr(self.instance, _method_name)
        args = self.request.get('args', [])
        kwargs = self.request.get('kwargs', {})
        if _method:
            self.response['json'] = _method(*args, **kwargs)
            self.response['text'] = str(self.response['json'])
        self.response['status_code'] = 200
        return self.response





