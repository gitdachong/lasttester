#coding:utf-8
import re
import uuid
import time
def _eval(code):
    return eval(code)

def equals(fact_value,expect_value):
    return fact_value == expect_value

def more_than(fact_value,expect_value):
    return fact_value > expect_value

def less_than(fact_value,expect_value):
    return fact_value < expect_value

def more_than_equals(fact_value,expect_value):
    return fact_value >= expect_value

def less_than_equals(fact_value,expect_value):
    return fact_value <= expect_value


def not_equals(fact_value,expect_value):
    return fact_value != expect_value

def length_equals(fact_value,expect_value):
    return len(fact_value) == int(expect_value)

def length_more_than(fact_value,expect_value):
    return len(fact_value) > int(expect_value)

def length_less_than(fact_value,expect_value):
    return len(fact_value) < int(expect_value)

def length_more_than_equals(fact_value,expect_value):
    return len(fact_value) >= int(expect_value)

def length_less_than_equals(fact_value,expect_value):
    return len(fact_value) <= int(expect_value)

def length_not_equals(fact_value,expect_value):
    return len(fact_value) != int(expect_value)

def is_none(fact_value):
    return fact_value is None

def is_not_none(fact_value):
    return fact_value is not None

def is_instance(face_value,expect_value):
    if isinstance(expect_value,str):
        expect_value = eval(expect_value)
    return isinstance(face_value,expect_value)

def is_not_instance(face_value,expect_value):
    if isinstance(expect_value,str):
        expect_value = eval(expect_value)
    return not isinstance(face_value,expect_value)

def regex_match(face_value,expect_value):
    if not isinstance(face_value,str) or not isinstance(expect_value,str):
        return False
    if re.search(expect_value,face_value):
        return True
    return False

def regex_not_match(face_value,expect_value):
    if not isinstance(face_value,str) or not isinstance(expect_value,str):
        return False
    if re.search(expect_value,face_value):
        return False
    return True

def ins(face_value,expect_value):
    if not isinstance(expect_value,(str,list,dict,tuple,set)):
        return False
    return face_value in expect_value

def not_ins(face_value,expect_value):
    if not isinstance(expect_value,(str,list,dict,tuple,set)):
        return False
    return face_value not in expect_value

def reverse_ins(face_value,expect_value):
    if not isinstance(face_value,(str,list,dict,tuple,set)):
        return False
    return expect_value in face_value

def reverse_not_ins(face_value,expect_value):
    if not isinstance(expect_value,(str,list,dict,tuple,set)):
        return False
    return expect_value not in face_value

def start_with(face_value,expect_value):
    return str(face_value).startswith(expect_value)

def end_with(face_value,expect_value):
    return str(face_value).endswith(expect_value)



