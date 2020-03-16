#coding:utf-8
class Extracter(object):

    def __init__(self,extract_content,extract_config):
        self.extract_content = extract_content
        self.extract_config = extract_config
        self.extract_results = {}
        target_filed = self.extract_config.get('target','content')
        self.search_content = self.extract_content.get(target_filed)

    def extract(self):
        return {}