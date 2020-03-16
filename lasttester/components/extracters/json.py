#coding:utf-8
from . import base
from ...utils.parser import parser_string_to_dict

class Extracter(base.Extracter):
    def __init__(self, extract_content,extract_config):
        super().__init__(extract_content,extract_config)
        self.parsed_content = self.extract_content.get('content_json') if self.extract_content.get('content_json') else parser_string_to_dict(self.extract_content)


    def extract(self):
        extract_rule = self.extract_config.get('rules','')
        if isinstance(extract_rule,list):
            for rule in self.extract_rules:
                self.extract_results[rule['output_key']] = self.extract_value(rule.get('rule'))
        elif isinstance(extract_rule,str):
            self.extract_results[self.extract_config['output_key']] = self.extract_value(extract_rule)
        return self.extract_results

    def extract_value(self,rule):
        extract_content = self.parsed_content
        if not rule:
            return ''
        try:
            for key in rule.split('.'):
                if isinstance(extract_content, (list, str)):
                    extract_content = extract_content[int(key)]
                elif isinstance(extract_content, dict):
                    extract_content = extract_content[key]
        except Exception as e:
            extract_content = ''
        return extract_content


