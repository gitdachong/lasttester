#coding:utf-8
class Extracter(object):

    def __init__(self,extract_content,extract_config):
        self.extract_content = extract_content
        self.extract_config = extract_config
        self.extract_results = {}
        self.target_filed = self.extract_config.get('target','text')
        self.search_content = self.__get_extract_content()


    def extract(self):
        return {}

    def __get_extract_content(self):
        if not self.target_filed:
            return self.extract_content.get('text')
        return str(self.extract_content.get(self.target_filed))