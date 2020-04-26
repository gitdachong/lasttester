#coding:utf-8
import uuid
import importlib
class DbClass(object):
    def __init__(self,config={},driver = 'mysql',**kwargs):
        self.driver = driver
        instance_class = importlib.import_module('.{}'.format(driver),'lasttester.contrib.database')
        self.db_instance = instance_class.DbHelper(config,**kwargs)

    # 关闭数据库连接
    def close(self):
        self.db_instance.close()

    # 创建数据库
    def createDataBase(self,DB_NAME):
        self.db_instance.createDataBase(DB_NAME)

    # 选择数据库
    def selectDataBase(self,DB_NAME):
        self.db_instance.selectDataBase(DB_NAME)

    # 获取数据库版本号
    def getVersion(self):
        return self.db_instance.getVersion()

    # 获取上个查询的结果
    def getOneData(self):
        return self.db_instance.getOneData()

    # 创建数据库表
    def creatTable(self, tablename, attrdict, constraint):
        return self.db_instance.creatTable(tablename, attrdict, constraint)

    def executeSql(self,sql=''):
        return self.db_instance.executeSql(sql)

    def executeCommit(self,sql=''):
        return self.db_instance.executeCommit(sql)

    def insert(self, tablename, params):
        return self.db_instance.insert(tablename, params)

    def select(self, tablename, where='',fields='*',**kwargs):
        return self.db_instance.select(tablename, where,fields,**kwargs)

    def getOne(self, tablename, where='',fields='*',**kwargs):
        return self.db_instance.getOne(tablename, where,fields,**kwargs)

    def getMany(self, tablename, where='',fields='*',**kwargs):
        return self.db_instance.getMany(tablename, where,fields,**kwargs)

    def delete(self, tablename, cond_dict):
        return self.db_instance.delete(tablename, cond_dict)

    def update(self, tablename, attrs_dict, cond_dict):
        return self.db_instance.update(tablename, attrs_dict, cond_dict)

    def dropTable(self, tablename):
        return self.db_instance.dropTable(tablename)

    def deleteTable(self, tablename):
        return self.db_instance.deleteTable(tablename)

    def isExistTable(self, tablename):
        return self.db_instance.isExistTable(tablename)

    def switch_db(self,name = None):
        return self.db_instance.switch_db(name)

    def reconnect(self):
        return self.db_instance.reconnect()

    def get_instance(self):
        return self.instance

    def call_method(self,method,*args,**kwargs):
        if hasattr(self.db_instance,method):
            return self.db_instance.method(*args,**kwargs)
        return None


