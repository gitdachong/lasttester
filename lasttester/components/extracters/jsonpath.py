#coding:utf-8
from . import base
from ...utils.parser import parser_string_to_dict

class Extracter(base.Extracter):
    def __init__(self, extract_content,extract_config):
        super().__init__(extract_content,extract_config)
        if self.target_filed in ['text','json']:
            self.search_content = self.extract_content.get('json') if self.extract_content.get('json') else parser_string_to_dict(self.search_content)
        else:
            self.search_content = parser_string_to_dict(self.search_content)

    def extract(self):
        extract_rule = self.extract_config.get('rules','')
        if isinstance(extract_rule,list):
            for rule in self.extract_rules:
                self.extract_results[rule['output_key']] = self.extract_value(rule.get('rule'))
        elif isinstance(extract_rule,str):
            self.extract_results[self.extract_config['output_key']] = self.extract_value(extract_rule)
        return self.extract_results

    def extract_value(self,rule):
        if not rule:
            return ''
        import jsonpath
        try:
            _result = jsonpath.jsonpath(self.search_content,rule)
        except:
            _result = ''
        return _result


