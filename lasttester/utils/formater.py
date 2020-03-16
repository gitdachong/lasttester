#coding;utf-8
import requests

STANDARD_OUTPUT_FROMAT = {
    "response":'',
    "response_json":{},
    "headers":{},
    "cookies":{},
    "status_code":0

}

STANDARD_TEST_RESULT_FORMAT = lambda :{
    "name":"",
    "type": "",
    "sampler":"",
    "result": False,
    "status_code": 0,
    "start_time": 0,
    "end_time": 0,
    "request": '',
    "request_parsed": {},
    "response": "",
    "response_parsed": {},
    "extractors": [],
    "asserters": [],
    "pre_processors": [],
    "post_processors": []
}

def formater_from_requests_response(response):
    result = STANDARD_OUTPUT_FROMAT
    result['response'] = response.text
    result['headers'] = dict(response.headers)
    result['cookies'] = requests.utils.dict_from_cookiejar(response.cookies)
    result['status_code'] = response.status_code
    if response.headers.get('Content-Type')=="application/json":
        result['response_json'] = response.json()
    return result



