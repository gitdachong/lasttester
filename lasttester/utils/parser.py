#coding:utf-8
import json
import ast
import re
absolute_http_url_regexp = re.compile(r"^https?://", re.I)

def parser_string_to_dict(origin_str = '',**kwargs):
    content_list = {}
    if isinstance(origin_str,dict):
        return origin_str
    try:
        content_list = json.loads(origin_str,**kwargs)
    except Exception:
        try:
            content_list = ast.literal_eval('(' + str(origin_str) + ')')
        except Exception:
            pass
    return content_list


def dict_to_json(origin_dict = {},**kwargs):
    result = ''
    try:
        result = json.dumps(origin_dict, indent=4, separators=(',', ': '), ensure_ascii=False,**kwargs)
    except:
        pass
    return result


def parser_http_url_complete(base_url,url):
    if not url:
        url = ''
    if absolute_http_url_regexp.match(url):
        return url
    elif base_url:
        return "{}/{}".format(base_url.rstrip("/"), url.lstrip("/"))
    else:
        raise Exception("url error!")


def parser_dict_keys_lower(source):
    target = {}
    if not isinstance(source,dict):
        return target
    target = {
        key.lower() : value if not isinstance(value,dict) else parser_dict_keys_lower(value) for key,value in source.items()
    }
    return target

def object_to_string(obj):
    result = ''
    if isinstance(obj,str):
        result = obj
    elif isinstance(obj,(list,set,tuple)):
        result = str([object_to_string(_item) for _item in obj])
    elif isinstance(obj,dict):
        result = dict_to_json(obj)
    else:
        try:
            result = str(result)
        except:
            pass
    return result

