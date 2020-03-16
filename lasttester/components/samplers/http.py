#coding:utf-8
from . import base
from ...utils import parser
from lasttester.utils.formater import formater_from_requests_response
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
        self.request_parsed = req
        self.request = parser.object_to_string(req.get('data'))
        resp = self.session.request(
            method,
            parsed_url,
            **req
        )

        self.response_parsed = formater_from_requests_response(resp)
        self.response =self.response_parsed.get('response')
        self.status_code = self.response_parsed.get('status_code')
        return self.response_parsed

