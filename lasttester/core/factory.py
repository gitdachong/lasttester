#coding:utf-8
import importlib

def load_configurer(config_type,config):
    try:
        module = importlib.import_module('.{}'.format(config_type),'lasttester.components.configs')
    except ModuleNotFoundError:
        module = importlib.import_module('.base', 'lasttester.components.configs')
    return module.Configurer(config)

def load_sampler(sampler_type,request,**kwargs):
    try:
        module = importlib.import_module('.{}'.format(sampler_type.lower()),'lasttester.components.samplers')
    except ModuleNotFoundError:
        module = importlib.import_module('.base', 'lasttester.components.samplers')
    return module.Sampler(request,**kwargs)


def load_extracter(extract_type,resp,extract_config,**kwargs):
    try:
        module = importlib.import_module('.{}'.format(extract_type),'lasttester.components.extracters')
    except ModuleNotFoundError:
        module = importlib.import_module('.base', 'lasttester.components.extracters')
    return module.Extracter(resp,extract_config,**kwargs)