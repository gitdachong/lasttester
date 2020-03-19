#coding:utf-8
import ftplib
import os
from ...core import constants
from . import base
class Configurer(base.Configurer):

    def __init__(self,config):
        self._config = config
        self._key = constants.KEY_CONFIGURER_INSTANCES
        self._results = {}
        self.instance = ftplib.FTP()
        self.instance.set_debuglevel(0)
        self.lines = []
        self._ftp_log = []

    def connect(self,_config):
        self._ftp_log.append(self.instance.connect(_config.get('host'),int(_config.get('port',21))))
        _pasv_mode =True if _config.get('mode') ==1 else False
        self.instance.set_pasv(_pasv_mode)
        self._ftp_log.append(self.instance.login(_config.get('username'),_config.get('password')))
        if 'defaut_path' in _config:
            self.opendir(_config.get('defaut_path'))
        self.__current_dir = self.instance.pwd()

    def parse(self):
        _config = self._config.get('config_body')
        self.connect(_config)
        self._results[self._config.get('name')] = self
        return [(self._key,self._results)]

    def close(self):
        if self.instance:
            self.instance.quit()

    def upload(self,remotepath, localpath):
        self._ftp_log = []
        if os.path.isdir(localpath):
            _files = os.listdir(localpath)
            for _file in _files:
                _path = os.path.join(localpath,_file)
                _remotepath = '{}/{}'.format(remotepath.rstrip('/'),_file)
                if os.path.isdir(_path):
                    self.upload(_remotepath,_path)
                else:
                    self.__upload_file(_remotepath,_path)
        else:
            self.__upload_file(remotepath, localpath)

    def __upload_file(self,remotepath, localpath):
        bufsize = 1024
        dirname,basename = self.__split(remotepath)
        self.opendir(dirname)
        fp = open(localpath, 'rb')
        _result = self.instance.storbinary('STOR ' + basename, fp, bufsize)
        print('__upload_file_1',type(_result),_result)
        fp.close()

    def download(self,remotepath, localpath):
        self._ftp_log = []
        try:
            _result = self.instance.cwd(remotepath)
            print('download',type(_result), _result)

            self.__download_dir(remotepath,localpath)
        except ftplib.error_perm:
            self.__download_file(remotepath, localpath)

    def __download_file(self,remotepath, localpath):
        bufsize = 1024
        dirname, basename = self.__split(remotepath)
        self.opendir(dirname)
        fp = open(localpath, 'wb')
        _result = self.instance.retrbinary('RETR ' + basename, fp.write, bufsize)
        print('__download_file_1', type(_result), _result)

        fp.close()

    def __download_dir(self,remotepath, localpath):
        if not os.path.exists(localpath):
            os.makedirs(localpath)
        self.__clear_lines()
        self.opendir(remotepath)
        _result = self.instance.retrlines("LIST", callback=self.__save_line)
        print('__download_dir_1', type(_result), _result)
        for line in self.lines:
            name = line.split(" ")[-1]
            if name in ['.','..']:
                continue
            _remote_path = '{}/{}'.format(remotepath.rstrip('/'),name)
            _local_path = os.path.join(localpath,name)
            if line[0] == "d":
                self.__download_dir(_remote_path,_local_path)
            else:
                self.__download_file(_remote_path,_local_path)


    def delete(self,remotepath):
        self._ftp_log = []
        try:
            self.instance.cwd(remotepath)
            self.delete_dir(remotepath)
        except ftplib.error_perm:
            _result = self.instance.delete(remotepath)
            print('__delete_1', type(_result), _result)

    def delete_dir(self,remotepath):
        self.__clear_lines()
        self.opendir(remotepath)
        self.instance.retrlines("LIST", callback=self.__save_line)
        for line in self.lines:
            name = line.split(" ")[-1]
            if name in ['.','..']:
                continue
            _path = remotepath + "/" + name
            if line[0] == "d":
                self.delete_dir(_path)
            else:
                _result = self.instance.delete(_path)
                print('delete_dir1', type(_result), _result)
        if remotepath !='/':
            _result = self.instance.rmd(remotepath)
            print('delete_dir_2', type(_result), _result)

    def opendir(self,remotepath):
        print(remotepath,self.__current_dir)
        if not remotepath or remotepath == self.__current_dir:
            return True

        dir_lists = remotepath.split(r'/')
        if not dir_lists[0]:
            dir_lists.pop(0)
        dir_lists.insert(0,r'/')
        for _dir in dir_lists:
            try:
                _result = self.instance.cwd(_dir)
                self._ftp_log.append()
                print('opendir_11', type(_result), _result)
            except ftplib.error_perm:
                try:
                    _result = self.instance.mkd(_dir)
                    self._ftp_log.append('mkdir dir ')
                    print('opendir_1', type(_result), _result)
                except ftplib.error_perm:
                    pass
                self.instance.cwd(_dir)
        self.__current_dir = self.instance.pwd()
        return True

    def __clear_lines(self):
        self.lines = []

    def __save_line(self, line):
        self.lines.append(line)

    def __split(self,path):
        while(path.find('//') !=-1):
            path  = path.replace('//','/')
        index = path.rfind('/')
        if index == -1:
            return '',path
        return path[:index],path[index + 1:]


