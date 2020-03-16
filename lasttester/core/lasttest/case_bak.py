#coding:utf-8
import unittest
from .. import factory

def strclass(cls):
    return "%s.%s" % (cls.__module__, cls.__qualname__)

class TestCase(unittest.TestCase):
    """A test case that wraps a test function.

        This is useful for slipping pre-existing test functions into the
        unittest framework. Optionally, set-up and tidy-up functions can be
        supplied. As with TestCase, the tidy-up ('tearDown') function will
        always be called if the set-up ('setUp') function ran successfully.
        """

    def __init__(self, context,test_data):
        super(TestCase, self).__init__()
        self._context = context
        self._test_data = test_data
        self._result = {}

    @property
    def result(self):
        return self._result
    def setUp(self):
        print(self._test_data)

    def tearDown(self):
        print('my tearDown')

    def runTest(self):
        configs = self._test_data.pop('configs', [])
        self._context.load_configs(configs)
        parsed_test_data = self._context.parse_lazy_load_to_object(self._test_data)
        sampler = factory.load_sampler(self._test_data.get('type', 'http'), parsed_test_data)
        resp = sampler.run_test()
        print(resp)
        extractors = self._test_data.get("extract", {})
        extracted_variables_mapping = self._extract_all(resp, extractors)
        self._context.update_variables(extracted_variables_mapping)
        self.validate(self._test_data.get("validators") or [])
        self._result = resp


    def _extract_all(self,resp,extracts):
        results = {}
        if not extracts:
            return results
        elif isinstance(extracts, dict):
            extracter = factory.load_extracter(extracts.get('type','base'),resp, extracts)
            results.update(extracter.extract())
        elif isinstance(extracts, list):
            for _extract in extracts:
                extracter = factory.load_extracter(_extract.get('type','base'),resp, _extract)
                results.update(extracter.extract())
        return results


    def id(self):
        return self._name

    def __eq__(self, other):
        return True

    def __hash__(self):
        return ''

    def __str__(self):
        return ''

    def __repr__(self):
        return ''

    def shortDescription(self):

        return ''

    def validate(self,asserters):
        rules_results = []
        for _asserter in asserters:
            extracter  = factory.load_extracter(_asserter.get('type','base'),self.content,_asserter)
            rule = _asserter.get('rules')
            symbol = _asserter.get('symbol','and')
            rule_results = []
            for field,expect_value in rule.items():
                if isinstance(expect_value,list) and len(expect_value >=2):
                    comparator = expect_value[0]
                    expect_value = expect_value[1]
                else:
                    comparator = 'equals'
                fact_value = extracter.extract_value(field)
                rule_result = self._comparator.compare(expect_value,fact_value,comparator)
                rule_results.append(True if rule_result else False )
            rules_results.append(self.__assemble_result(rule_results,symbol))

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