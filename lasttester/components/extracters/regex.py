#coding:utf-8
from . import base
import re

class Extracter(base.Extracter):
    def __init__(self, extract_content,extract_config):
        super().__init__(extract_content,extract_config)
    def extract(self):
        extract_rule = self.extract_config.get('rules','')
        if isinstance(extract_rule,list):
            for rule in self.extract_rules:
                self.extract_results[rule['output_key']] = self.extract_value(rule.get('rule'))
        elif isinstance(extract_rule,dict):
            self.extract_results[self.extract_config['output_key']] = self.extract_value(extract_rule)
        return self.extract_results

    def extract_value(self,rule):
        _result = re.search(rule.get('regex',''),self.search_content)
        if not _result:
            return ''
        _index = rule.get('index',0)
        return _result.group(_index)





