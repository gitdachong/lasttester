#coding:utf-8
import types
from . import factory, built_in
import re
from urllib.parse import quote

import requests
DELAY_VARIABLE_PATTERN = re.compile(r"\$\{(\w+)\}")
DELAY_FUNCTION_PATTERN = re.compile(r"\$\{(\w+)\(([\s\S]*)\)\}")
DELAY_QUOTATION_PATTERN = re.compile(r"\'([\s\S]*?)\'|\"([\s\S]*?)\"")
DELAY_STR_PATTERN = re.compile(r"\$\{(\w+)(|\([^\{\}]*\))\}")

def is_lazy_load_string(source):
    if not isinstance(source, str):
        return False
    if DELAY_STR_PATTERN.search(source):
        return True
    return False

class Context(object):


    def __init__(self):
        self.__global_objects = {
            "variables": {},
            "functions": {},
            "configurers": [],
            "http_session":{
                "session":requests.Session()
            }

        }
        self.__register('functions', built_in.built_in_functions)
        self.__register('variables', built_in.built_in_variables)



    def __del__(self):
        for _configurer in self.__global_objects.get('configurers'):
            _configurer.close()

    def __register(self,_key,values):

        if _key not in self.__global_objects:
            self.__global_objects[_key] = values
        elif isinstance(values, list):
            self.__global_objects[_key].extend(values)
        elif isinstance(values, dict):
            self.__global_objects[_key].update(values)
        else:
            self.__global_objects[_key] = values

    def load_configs(self,configs):
        if not isinstance(configs,list):
            return
        for _config in configs:
            _configurer = factory.load_configurer(_config.get('type','base'),_config)
            self.__register('configurers', [_configurer])
            parse_results = _configurer.parse()
            for _config_key, _config_values in parse_results:
                self.__register(_config_key, _config_values)

        for _key,values in self.__global_objects.items():
            self.__global_objects[_key] = self.parse_lazy_load_to_object(values)


    def update_variables(self,variables):
        if isinstance(variables,list):
            for variable in variables:
                if isinstance(variable,dict):
                    self.__global_objects['variables'].update(variable)
        elif isinstance(variables,dict):
            self.__global_objects['variables'].update(variables)
        else:
            raise Exception('function update_variables only accept parameters of types(list,dict)')

    def update_functions(self,functions):
        if isinstance(functions,list):
            for _function in functions:
                if isinstance(_function,dict):
                    self.__global_objects['functions'].update(_function)
        elif isinstance(functions,dict):
            self.__global_objects['functions'].update(functions)
        else:
            raise Exception('function update_variables only accept parameters of types(list,dict)')

    def get_variables(self,name = None):
        if not name:
            return self.__global_objects['variables']
        _value = self.__global_objects['variables'].get(name)
        if isinstance(_value,types.FunctionType):
            _value = _value()
        return _value

    def get_functions(self,name = None):
        if not name:
            return self.__global_objects['functions']
        return self.__global_objects['functions'].get(name)

    def get_objects(self,name):
        return self.__global_objects.get(name,{})

    def update_objects(self,name,values):
        self.__global_objects[name] = values

    def parse_lazy_load_to_object(self,source):
        if isinstance(source, list):
            source = [self.parse_lazy_load_to_object(_item,) for _item in source]
        elif isinstance(source, set):
            source = set([self.parse_lazy_load_to_object(_item,) for _item in source])
        elif isinstance(source, dict):
            source = {
                self.parse_lazy_load_to_object(_key): self.parse_lazy_load_to_object(_value) for _key, _value in
            source.items()
            }
        elif isinstance(source, str):
            source = self.parse_object_impl(source)
        return source

    def parse_object_impl(self,content):

        _parsed_value = content
        while (is_lazy_load_string(_parsed_value)):
            _parsed_value_pre = _parsed_value
            start_index = _parsed_value.find('$')
            while (start_index != -1):
                _parsed_value = self.parse_variable_object(_parsed_value,start_index)
                if not isinstance(_parsed_value, str):
                    break
                _parsed_value = self.parse_function_object(_parsed_value,start_index )
                if not isinstance(_parsed_value, str):
                    break
                start_index = _parsed_value.find('$',start_index+1)

            if _parsed_value_pre == _parsed_value:
                break
        return _parsed_value


    def parse_variable_object(self,content,start_index=0):
        _matched_variable = DELAY_VARIABLE_PATTERN.match(content, start_index)
        if not _matched_variable:
            return content
        _parsed_value = self.get_variables(_matched_variable.group(1))
        content_length =len(content)
        _matched_length = len(_matched_variable.group())

        if  content_length== _matched_length:
            return _parsed_value
        return content[:start_index] + str(_parsed_value) + content[start_index + _matched_length :]

    def parse_function_object(self,content,start_index=0):
        _matched_function = DELAY_FUNCTION_PATTERN.match(content, start_index)
        if not _matched_function:
            return content
        _function_name = self.parse_object_impl(_matched_function.group(1))
        _function = self.get_functions(_function_name)
        if not _function:
            return content
        _function_params = _matched_function.group(2)
        _function_params_parsed = []
        if _function_params:
            _function_params = _function_params.split(',')
            for _function_param in _function_params:
                _function_params_parsed.append(self.parse_object_impl(_function_param))
        _parsed_value = _function(*_function_params_parsed)
        content_length = len(content)
        _matched_length = len(_matched_function.group())
        if content_length == _matched_length:
            return _parsed_value
        return content[:start_index] + str(_parsed_value) + content[start_index + _matched_length:]

    def __format_string_quotation(self,source):

        def _parse_sub_str(matched):
            return '"{}"'.format(quote(matched.group(1)))

        source = DELAY_QUOTATION_PATTERN.sub(_parse_sub_str,source)
        return source