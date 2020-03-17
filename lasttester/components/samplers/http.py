#coding:utf-8
from . import base
from ...utils import parser
import requests
ALLOWED_METHOD = ["GET", "HEAD", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"]

class Sampler(base.Sampler):


    def __init__(self,test_content,**kwargs):
        super().__init__(test_content)
        self.sampler_name = 'http'
        if 'session' in kwargs:
            self.session = kwargs.get('session')
        else:
            self.session = requests.Session()

    def run(self):
        req = self.test_content.pop('request',{})
        method = req.pop('method', 'GET')
        if method.upper() not in ALLOWED_METHOD:
            raise Exception('Http(s)Sampler do not allow {} method'.format(method))

        url = req.pop('url')
        common_http_request = self.test_content.get('common_http_request',{})
        parsed_url = parser.parser_http_url_complete(common_http_request.get('base_url'), url)
        self.request['text'] = parser.object_to_string(req.get('data'))
        self.request.update(req)
        resp = self.session.request(
            method,
            parsed_url,
            **req
        )
        self.response =self.__parsed_response(resp)
        return self.response

    def __parsed_response(self,resp):
        _response = {}
        _response['text'] = resp.text
        _response['headers'] = dict(resp.headers)
        _response['cookies'] = requests.utils.dict_from_cookiejar(resp.cookies)
        _response['status_code'] = resp.status_code
        if resp.headers.get('Content-Type') == "application/json":
            _response['json'] = resp.json()
        return _response




