# -*- coding: utf-8 -*-
import pymysql
import re

class DbHelper(object):
    def __init__(self , config,**kwargs):
        self.con = None
        self.cur = None
        if not config.get('cursorclass'):
            config['cursorclass'] =pymysql.cursors.DictCursor
        self.config = config
        self.connect(self.config)

    def connect(self,config):
        try:
            self.con = pymysql.connect(**config)
            self.con.autocommit(1)
            # 所有的查询，都在连接 con 的一个模块 cursor 上面运行的
            self.cur = self.con.cursor()
        except Exception as e:
            print(e)

    def reconnect(self):
        self.connect(self.config)

    # 关闭数据库连接
    def close(self):

        if self.con and self.con.open:
            self.con.close()

    # 创建数据库
    def createDataBase(self,DB_NAME):
        # 创建数据库
        self.cur.execute('CREATE DATABASE IF NOT EXISTS %s DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci' % DB_NAME)
        self.con.select_db(DB_NAME)

    # 选择数据库
    def selectDataBase(self,DB_NAME):
        self.con.select_db(DB_NAME)

    # 获取数据库版本号
    def getVersion(self):
        self.cur.execute("SELECT VERSION() as version")
        return self.getOneData()

    # 获取上个查询的结果
    def getOneData(self):
        # 取得上个查询的结果，是单个结果
        data = self.cur.fetchone()
        return data

    # 创建数据库表
    def creatTable(self, tablename, attrdict, constraint):
        if self.isExistTable(tablename):
            return True #幂等
        sql = ''
        sql_mid = '`id` bigint(11) NOT NULL AUTO_INCREMENT,'
        for attr,value in attrdict.items():
            sql_mid = sql_mid + '`'+attr + '`'+' '+ value+','
        sql = sql + 'CREATE TABLE IF NOT EXISTS %s ('%tablename
        sql = sql + sql_mid
        sql = sql + constraint
        sql = sql + ') ENGINE=InnoDB DEFAULT CHARSET=utf8'
        print('creatTable:'+sql)
        self.executeCommit(sql)

    def executeSql(self,sql=''):
        try:
            self.cur.execute(sql)
            records = self.cur.fetchall()
            return records
        except pymysql.Error as e:
            error = 'MySQL execute failed! ERROR (%s): %s' %(e.args[0],e.args[1])
            raise error
        return None

    def executeCommit(self,sql=''):
        """执行数据库sql语句，针对更新,删除,事务等操作失败时回滚

        """
        print(sql)
        result = None
        try:
            result = self.cur.execute(sql)
            self.con.commit()
            self.cur
        except pymysql.Error as e:
            self.con.rollback()
            error = 'MySQL execute failed! ERROR (%s): %s' %(e.args[0],e.args[1])
            print("error:", error)
            raise error
        return result

    def insert(self, tablename, params = {}):
        if not params or params == {}:
            return
        _sql = []
        _sql.append('INSERT INTO {} '.format(tablename))
        if isinstance(params,str):
            _sql.append(params)
        elif isinstance(params,dict):
            _sql.append( ' ({}) values ({}) '.format(','.join(params.keys()),','.join(["'{}'".format(self.__format_sql_value(v)) if isinstance(v,str) else '{}'.format(v) for v in params.values()])))
        else:
            _sql.append(str(params))
        print('_insert:'+''.join(_sql))
        self.executeCommit(''.join(_sql))

    def getOne(self, tablename, where='',fields='*', **kwargs):
        result = self.select(tablename,where,fields,**kwargs)
        return result if not result else result[0]

    def getMany(self, tablename, where='', fields='*',**kwargs):
        return self.select(tablename,where,fields,**kwargs)

    def __add_where(self,where):
        if isinstance(where,dict):
            temp_sql = []
            for k, v in where.items():
                temp_sql.append(self._adds(k,v))
            _sql= ' where ' + ' and '.join(temp_sql)
        elif isinstance(where,str):
            _sql =' where ' + where
        else:
            _sql =' where ' +str(where)
        return _sql

    def _adds(self,k,v,s='='):
        if isinstance(v,str):
            return "{} {}'{}'".format(k,s,v)
        elif isinstance(v,int) or isinstance(v,float) or isinstance(v,complex):
            return "{} {} {}".format(k, s, v)
        elif isinstance(v,tuple):
            return self._adds(k,v[1],v[0])
        elif isinstance(v,list):
            return "{} {} ({})".format(k,s,','.join(["'{}'".format(self.__format_sql_value(vv)) if isinstance(vv,str) else "{}".format(vv) for vv in v]))
        return ''

    def select(self, tablename, where='',fields='*',**kwargs):
        sql=[]
        sql.append('SELECT ')
        if isinstance(fields,list):
            sql.append( ",".join(fields))
        elif isinstance(fields,str):
            sql.append(fields)
        elif isinstance(fields,dict):
            sql.append(",".join(fields.keys()))
        else:
            sql.append(str(fields))
        sql.append(' FROM {}'.format(tablename))
        sql.append(self.__add_where(where))
        if kwargs.get('order'):
            sql.append(' order by {}'.format(kwargs.get('order')))
        if kwargs.get('limit'):
            sql.append(' limit {}'.format(kwargs.get('limit')))
        sql = ''.join(sql)
        print('select:' + sql)
        return self.executeSql(sql)

    def delete(self, tablename, where):
        _sql = []
        _sql.append('DELETE from {} '.format(tablename))
        _sql.append(self.__add_where(where))
        print('delete:',''.join(_sql))
        return self.executeCommit(''.join(_sql))

    def update(self, tablename, update = None, where = {}):
        if not update:
            return False
        _sql = []
        _sql.append('UPDATE {} set '.format(tablename))
        if isinstance(update,str):
            _sql.append(update)
        elif isinstance(update,dict):
            _sql.append(','.join(["{}='{}'".format(k,self.__format_sql_value(v)) if isinstance(v,str) else "{}={}".format(k,v) for k,v in update.items()]))
        _sql.append(self.__add_where(where))
        print(''.join(_sql))
        return self.executeCommit(''.join(_sql))

    def dropTable(self, tablename):
        sql = "DROP TABLE  %s" % tablename
        self.executeCommit(sql)

    def deleteTable(self, tablename):
        """清空数据库表

            args：
                tablename  ：表名字
        """
        sql = "DELETE FROM %s" % tablename
        print("sql=",sql)
        self.executeCommit(sql)

    def isExistTable(self, tablename):
        """判断数据表是否存在

            args：
                tablename  ：表名字

            Return:
                存在返回True，不存在返回False
        """
        sql = "select * from %s" % tablename
        result = self.executeCommit(sql)
        if result is None:
            return True
        else:
            if re.search("doesn't exist", result):
                return False
            else:
                return True
    def __format_sql_value(self,v):
        v = v.replace("'", r"\'")
        if v[-1:] =='\\':
            v+="\\"
        return v

    def __del__(self):
        self.close()