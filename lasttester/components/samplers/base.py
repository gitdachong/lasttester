#coding:utf-8

class Sampler(object):

    def __init__(self,test_data):
        self.test_content = test_data
        self.request = {}
        self.response = {}
        self.sampler_name = 'base'

    def run_test(self):
        pass