#coding:utf-8
from lasttester import LastTester
import sys
import os


if __name__ == '__main__':
    tests_mapping = {"configs":[{"type":"variable","config_body":{"LEMA_PAY_URL": "http://client1.lema.com/", "apply_limit": "1000000", "recharge_amount": "1000000", "category_id": "101571", "good_id_national_currency": "1059", "good_id_foreign_currency": "1069", "to_phone": "769081411", "LEMA_EXITS_PHONEs": ["769081411", "769081412", "769081413", "769081414", "769081415", "769081416", "769081417", "769081418", "769081419", "769081420", "769081421", "769081422", "769081423", "769081424", "769081425", "769081426", "769081427", "769081428", "769081429", "769081430", "769081431", "769081432", "769081433", "769081434", "769081435", "769081436", "769081437", "769081438", "769081439", "769081440", "769081441", "769081442", "769081443", "769081444", "769081445", "769081446", "769081447", "769081448", "769081449", "769081450", "769081451", "769081452", "769081453", "769081454", "769081455", "769081456", "769081457", "769081458", "769081459", "769081460", "769081461", "769081462", "769081463", "769081464", "769081465", "769081466", "769081467", "769081468", "769081469", "769081470", "769081471", "769081472", "769081473", "769081474", "769081475", "769081476", "769081477", "769081478", "769081479", "769081480", "769081481", "769081484", "769081485", "769081486", "769081487", "769081488", "769081489", "769081490", "769081491", "769081492", "769081493", "769081494", "769081495", "769081496", "769081497", "769081498", "769081499", "769081500", "769081501", "769081502", "769081503", "769081504", "769081505", "769081506", "769081507", "769081508", "769081509", "769081510", "769081511", "769081512", "769081513", "769081514", "769081515"], "LEMA_PAY_VERSION": "1.9.1", "LEMA_PAY_OLD_VERSION": "1.8.6", "LEMA_PAY_DEVICE_ID": "1CEC65BF-3CFB-46DF-9159-5A730079865D"}},
                                {"type": "db", "name": "local","config_body": {"host": "127.0.0.1", "port": 3306, "user": "root", "password": "123456","database": "lemajestic_v2"}},
                                {"type": "code","name": "code1","config_body": "import random\nimport string\nimport time\nimport json\nimport uuid,hashlib\n\nprint(2)\ndef random_select(target_dict):\n    if isinstance(target_dict,list):\n        return random.choice(target_dict)\n    elif isinstance(target_dict,dict):\n        key = random.choice(target_dict)\n        return target_dict.get(key)\n\ndef join_groups(include_groups,groups):\n    include_groups.extend(groups)\n    result = json.dumps(list(set(include_groups)))\n    return result\ndef str_random(len):\n    str_list = [random.choice(string.digits + string.ascii_letters) for i in range(len)]\n    random_str = ''.join(str_list)\n    return random_str\ndef str_time():\n    return time.strftime(\"%Y-%m-%d %H:%M:%S\", time.localtime())\ndef str_timestamp(isShort=False):\n    return str(int_timestamp(isShort))\ndef int_timestamp(isShort=False):\n    if isShort:\n        return int(time.time())\n    return int(time.time()*1000)\ndef genName():\n    baijiaxing = u'\u8d75\u94b1\u5b59\u674e\u5468\u5434\u90d1\u738b\u51af\u9648\u891a\u536b\u848b\u6c88\u97e9\u6768\u6731\u79e6\u5c24\u8bb8\u4f55\u5415\u65bd\u5f20\u5b54\u66f9\u4e25\u534e\u91d1\u9b4f\u9676\u59dc\u621a\u8c22\u90b9\u55bb\u67cf\u6c34\u7aa6\u7ae0\u4e91\u82cf\u6f58\u845b\u595a\u8303\u5f6d\u90ce\u9c81\u97e6\u660c\u9a6c\u82d7\u51e4\u82b1\u65b9\u4fde\u4efb\u8881\u67f3\u9146\u9c8d\u53f2\u5510\u8d39\u5ec9\u5c91\u859b\u96f7\u8d3a\u502a\u6c64\u6ed5\u6bb7\u7f57\u6bd5\u90dd\u90ac\u5b89\u5e38\u4e50\u4e8e\u65f6\u5085\u76ae\u535e\u9f50\u5eb7\u4f0d\u4f59\u5143\u535c\u987e\u5b5f\u5e73\u9ec4\u548c\u7a46\u8427\u5c39\u59da\u90b5\u6e5b\u6c6a\u7941\u6bdb\u79b9\u72c4\u7c73\u8d1d\u660e\u81e7\u8ba1\u4f0f\u6210\u6234\u8c08\u5b8b\u8305\u5e9e\u718a\u7eaa\u8212\u5c48\u9879\u795d\u8463\u6881\u675c\u962e\u84dd\u95f5\u5e2d\u5b63\u9ebb\u5f3a\u8d3e\u8def\u5a04\u5371\u6c5f\u7ae5\u989c\u90ed\u6885\u76db\u6797\u5201\u949f\u5f90\u90b1\u9a86\u9ad8\u590f\u8521\u7530\u6a0a\u80e1\u51cc\u970d\u865e\u4e07\u652f\u67ef\u661d\u7ba1\u5362\u83ab\u67ef\u623f\u88d8\u7f2a\u5e72\u89e3\u5e94\u5b97\u4e01\u5ba3\u8d32\u9093\u90c1\u5355\u676d\u6d2a\u5305\u8bf8\u5de6\u77f3\u5d14\u5409\u94ae\u9f9a\u7a0b\u5d47\u90a2\u6ed1\u88f4\u9646\u8363\u7fc1\u8340\u7f8a\u4e8e\u60e0\u7504\u66f2\u5bb6\u5c01\u82ae\u7fbf\u50a8\u9773\u6c72\u90b4\u7cdc\u677e\u4e95\u6bb5\u5bcc\u5deb\u4e4c\u7126\u5df4\u5f13\u7267\u9697\u5c71\u8c37\u8f66\u4faf\u5b93\u84ec\u5168\u90d7\u73ed\u4ef0\u79cb\u4ef2\u4f0a\u5bab\u5b81\u4ec7\u683e\u66b4\u7518\u94ad\u5386\u620e\u7956\u6b66\u7b26\u5218\u666f\u8a79\u675f\u9f99\u53f6\u5e78\u53f8\u97f6\u90dc\u9ece\u84df\u6ea5\u5370\u5bbf\u767d\u6000\u84b2\u90b0\u4ece\u9102\u7d22\u54b8\u7c4d\u8d56\u5353\u853a\u5c60\u8499\u6c60\u4e54\u9633\u90c1\u80e5\u80fd\u82cd\u53cc\u95fb\u8398\u515a\u7fdf\u8c2d\u8d21\u52b3\u9004\u59ec\u7533\u6276\u5835\u5189\u5bb0\u90e6\u96cd\u5374\u74a9\u6851\u6842\u6fee\u725b\u5bff\u901a\u8fb9\u6248\u71d5\u5180\u6d66\u5c1a\u519c\u6e29\u522b\u5e84\u664f\u67f4\u77bf\u960e\u5145\u6155\u8fde\u8339\u4e60\u5ba6\u827e\u9c7c\u5bb9\u5411\u53e4\u6613\u614e\u6208\u5ed6\u5ebe\u7ec8\u66a8\u5c45\u8861\u6b65\u90fd\u803f\u6ee1\u5f18\u5321\u56fd\u6587\u5bc7\u5e7f\u7984\u9619\u4e1c\u6b27\u6bb3\u6c83\u5229\u851a\u8d8a\u5914\u9686\u5e08\u5de9\u538d\u8042\u6641\u52fe\u6556\u878d\u51b7\u8a3e\u8f9b\u961a\u90a3\u7b80\u9976\u7a7a\u66fe\u6bcb\u6c99\u4e5c\u517b\u97a0\u987b\u4e30\u5de2\u5173\u84af\u76f8\u67e5\u540e\u8346\u7ea2\u6e38\u7afa\u6743\u902e\u76cd\u76ca\u6853\u516c'\n    i = random.randint(0, len(baijiaxing))\n    temp = baijiaxing[i:i + 1]\n    temp = temp + genChinese(2)\n    return temp\n\ndef genChinese(num):\n    temp = \"\"\n    for n in range(1, num + 1, 1):\n        temp = temp + num2Chinese(random.randint(0, 9))\n    return temp\n\ndef genUuid():\n    return hashlib.md5(str(uuid.uuid1()).encode()).hexdigest()\n\ndef num2Chinese(num):\n    temp = \"\"\n    if num == 0:\n        temp = \"\u96f6\"\n    elif num == 1:\n        temp = \"\u4e00\"\n    elif num == 2:\n        temp = \"\u4e8c\"\n    elif num == 3:\n        temp = \"\u4e09\"\n    elif num == 4:\n        temp = \"\u56db\"\n    elif num == 5:\n        temp = \"\u4e94\"\n    elif num == 6:\n        temp = \"\u516d\"\n    elif num == 7:\n        temp = \"\u4e03\"\n    elif num == 8:\n        temp = \"\u516b\"\n    elif num == 9:\n        temp = \"\u4e5d\"\n    return temp\n\n\n# \u968f\u673a\u751f\u6210\u624b\u673a\u53f7\u7801\ndef genPhone(prefix = None,index=1):\n    if not prefix:\n        with open('account_temp.txt','r',encoding='gbk', errors='ignore') as file:\n            prefix = file.read()\n    if len(str(prefix)) + len(str(index)) >11:\n        phoneNo = int(str(prefix)[0:11-len(str(index))])+index\n    else:\n        phoneNo = int(str(prefix).ljust(11-len(str(index)),'0'))+index\n    if phoneNo:\n        with open('account_temp.txt','w',encoding='gbk', errors='ignore') as file:\n            file.write(str(phoneNo))\n    return phoneNo\n\ndef getPhone():\n    phone = ''\n    with open('account_temp.txt', 'r', encoding='gbk', errors='ignore') as file:\n        phone = file.read()\n    return str(phone)\n\n# \u968f\u673a\u751f\u6210\u624b\u673a\u53f7\u7801\ndef genPhone_jinbian(prefix,index):\n    length = len(prefix)\n    if length >9:\n        return prefix\n    phoneNo = int(prefix.ljust(9,'0'))+int(index)\n\n    return str(phoneNo)\n\ndef calcCrfuid(crfuid):\n    return str(abs(getHashCode(crfuid))% 10)\n\ndef convert_n_bytes(n, b):\n    bits = b * 8\n    return (n + 2 ** (bits - 1)) % 2 ** bits - 2 ** (bits - 1)\n\ndef convert_4_bytes(n):\n    return convert_n_bytes(n, 4)\n\ndef getHashCode(s):\n    h = 0\n    n = len(s)\n    for i, c in enumerate(s):\n        h = h + ord(c) * 31 ** (n - 1 - i)\n    return convert_4_bytes(h)\ndef makeCrfuid(idno):\n    pass\n"},
                                {"type": "file","name": "file1","config_body":{"path":'README.md'}},
                                {"type": "redis","name": "redis1","config_body":{"host":'127.0.0.1',"port":6379}},


                                ] ,
                     "testcases": [{"config": {"name": "testcase description",
                                               "variables": {"x": "1", "test": "${genChinese(10)}"}},
                        "teststeps": [
                         {"name": "\u68c0\u6d4b\u7248\u672c\u63a5\u53e3-\u6700\u65b0\u7248\u672c",
                          "type": "http",
                          "request": {"url": "${LEMA_PAY_URL}",
                                      "params": {"ct": "member", "ac": "check_version"},
                                      "method": "POST", "headers": {"Content-Type": "application/x-www-form-urlencoded",
                                                                    "User-Agent": "LP-Main/3 CFNetwork/978.0.7 Darwin/18.7.0",
                                                                    "Keep-Alive": "timeout=20, max=100"}, "data": {
                                  "post_data": "{\n  \"deviceid\" : \"${LEMA_PAY_DEVICE_ID}\",\n  \"sign\" : \"7017434608525C904E690EA36E74F530\",\n  \"x-app-id\" : \"${x}\",\n  \"os\" : \"ios\",\n  \"boundId\" : \"com.awesome.lemaPackage\",\n  \"ios_system_version\" : \"12.4\",\n  \"lang\" : \"zh-Hans\",\n  \"version\" : \"${LEMA_PAY_VERSION}\",\n  \"uuid\" : \"${LEMA_PAY_DEVICE_ID}\"\n}"}},
                          "validate": [{"type":"json","rules": {"code":1},"target":"content"}],
                          "extract": [{"type":"json","output_key":"my_code","rules": "code","target":"text"},{"type":"jsonpath","output_key":"my_code1","rules": "$.code","target":"text"},{"type":"http1","output_key":"cookies","rules": "cookies","target":"cookies"}]},

                         {"name": "\u68c0\u6d4b\u7248\u672c\u63a5\u53e3-\u975e\u6700\u65b0\u7248\u672c",
                          "type": "http",
                          "request": {"url": "${LEMA_PAY_URL}", "params": {"ct": "member", "ac": "check_version"},
                                      "method": "POST", "headers": {"Content-Type": "application/x-www-form-urlencoded",
                                                                    "User-Agent": "LP-Main/3 CFNetwork/978.0.7 Darwin/18.7.0",
                                                                    "Keep-Alive": "timeout=20, max=100"}, "data": {
                                  "post_data": "{\n  \"deviceid\" : \"${LEMA_PAY_DEVICE_ID}\",\n  \"sign\" : \"-------${my_code}\",\n  \"x-app-id\" : \"${x}\",\n  \"os\" : \"ios\",\n  \"boundId\" : \"com.awesome.lemaPackage\",\n  \"ios_system_version\" : \"12.4\",\n  \"lang\" : \"zh-Hans\",\n  \"version\" : \"${LEMA_PAY_OLD_VERSION}\",\n  \"uuid\" : \"${LEMA_PAY_DEVICE_ID}\"\n}"}},
                          "validate": []
                          },
                            {
                                "name":"",
                                "type":"db",
                                "instance":"local",
                                "request":"insert into mp_test values (null,'test',${__TIMESTAMP_10},1,1,1,1)"

                            },

                            {
                                "name": "",
                                "type": "db",
                                "instance": "local",
                                "request": "select * from mp_test where id=1; "

                            },
                            {
                                "name": "",
                                "type": "redis",
                                "instance": "redis1",
                                "request": {
                                    "method":"set",
                                    "args":['aaa',111]
                                }

                            },
                            {
                                "name": "",
                                "type": "redis",
                                "instance": "redis1",
                                "request": {
                                    "method":"get",
                                    "args":['aaa']
                                }

                            },

                        ]}]}
    test = LastTester()
    result = test.run(tests_mapping)
    print(result)


