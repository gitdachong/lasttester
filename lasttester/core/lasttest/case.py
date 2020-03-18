#coding:utf-8
import time
from .. import factory,constants
from ...utils import formater,capturer,util
class TestCase(object):

    def __init__(self,context,test_data):
        self._context = context
        self._test_data = test_data
        self._name = ''
        self._sampler = None
        self._request_type = ''
        self._result = {
            "name":"",
            "type": "",
            "sampler":"",
            "result": False,
            "status_code": 0,
            "start_time": 0,
            "end_time": 0,
            "request": '',
            "response": "",
            "extractors": [],
            "asserters": [],
            "pre_processors": [],
            "post_processors": []
        }
        self._asserters = []
        self._extractors = []


    @property
    def result(self):
        self._result['asserters'] = self._asserters
        self._result['extractors'] = self._extractors
        if self._sampler:
            self._result.update({
                'sampler':self._sampler.sampler_name,
                'status_code':self._sampler.response['status_code'],
                'request':self._sampler.request,
                'response':self._sampler.response,
            })
        else:
            self._result['status_code'] = 0

        return self._result

    def __load_extra_datas(self,sampler_type,instance_name):
        extra_data = self._context.get_objects(sampler_type)
        if instance_name:
            extra_data['instance'] = self._context.get_objects(constants.KEY_CONFIGURER_INSTANCES).get(instance_name)
        return extra_data



    def runTest(self):
        configs = self._test_data.pop('configs', [])
        self._context.load_configs(configs)
        parsed_test_data = self._context.parse_lazy_load_to_object(self._test_data)
        self._result['type']= self._test_data.get('type', 'http')
        extra_data = self.__load_extra_datas(self._result['type'],self._test_data.get('instance'))
        self._sampler = factory.load_sampler(self._result['type'], parsed_test_data, **extra_data)
        resp = self._sampler.run()
        extractors = self._test_data.get("extract", {})
        extracted_variables_mapping = self._extract_all(resp, extractors)
        self._context.update_variables(extracted_variables_mapping)
        self._result['result'] = self.validate(self._test_data.get("validators") or [])

    def _extract_all(self,resp,extracts):
        results = {}
        if not extracts:
            return results
        elif isinstance(extracts, dict):
            extracter = factory.load_extracter(extracts.get('type','base'),resp, extracts)
            extracts['extract_result'] = extracter.extract()
            results.update(extracts['extract_result'])
            self._extractors.append(extracts)
        elif isinstance(extracts, list):
            for _extract in extracts:
                extracter = factory.load_extracter(_extract.get('type','base'),resp, _extract)
                _extract['extract_result'] = extracter.extract()
                results.update(_extract['extract_result'])
                self._extractors.append(_extract)
        return results

    def validate(self,asserters):
        if not asserters:
            return True
        rules_results = []
        for _asserter in asserters:
            extracter  = factory.load_extracter(_asserter.get('type','base'),self.content,_asserter)
            rule = _asserter.get('rules')
            symbol = _asserter.get('symbol','and')
            rule_results = []
            _asserter['asserts'] = []
            for field,expect_value in rule.items():
                if isinstance(expect_value,list) and len(expect_value >=2):
                    comparator = expect_value[0]
                    expect_value = expect_value[1]
                else:
                    comparator = 'equals'
                fact_value = extracter.extract_value(field)
                rule_result = self._comparator.compare(expect_value,fact_value,comparator)
                rule_results.append(True if rule_result else False )
                _asserter['assert_details'].append({
                    'field':field,
                    'expect_value':expect_value,
                    'fact_value':fact_value,
                    'comparator':comparator,
                    'result':rule_result
                })
            _asserter['assert_result'] = self.__assemble_result(rule_results,symbol)
            rules_results.append(_asserter['assert_result'])
            self._asserters.append(_asserter)

        return self.__assemble_result(rules_results)



    def __assemble_result(self,results,symbol = 'and'):
        if not results:
            return True
        if symbol =='and':
            if False in results:
                return False
        elif symbol =='or':
            if not True in results:
                return False
        return True

    def __repr__(self):
        return self._name

    def __call__(self, *args, **kwds):
        return self.run(*args, **kwds)

    def run(self, result=None):
        outcome = capturer.Capturer()
        try:
            self._outcome = outcome
            with outcome.catch():
                self._setUp()
            with outcome.catch():
                self.runTest()
            with outcome.catch():
                self._tearDown()

            result.add_test_result(self,outcome.success,outcome.get_parsed_errors())
            return result
        finally:
            result.stopTest(self)
            outcome.errors.clear()
            self._outcome = None

    def _setUp(self):
        self._result['start_time'] = util.get_current_timestamp_13()

    def _tearDown(self):
        self._result['end_time'] = util.get_current_timestamp_13()