# -*- coding: utf-8 -*-
"""
Author  : htfeng
Date    : 20180626
Content : 获取数据
"""
import os
import subprocess

root_url = "ftp://cddis.gsfc.nasa.gov/pub/vlbi/ivscontrol/"
path_src = os.getcwd() + '\\src\\'
path_new = os.getcwd() + '\\station\\'
path_int = os.getcwd() + '\\stationInt\\'


class GetFile:
    def __init__(self, start_year, end_year):
        self.start_year = start_year
        self.end_year = end_year

    def getFile(self):
        for year in range(self.start_year, self.end_year):
            year = str(year)
            srcFilename = path_src + 'master{0}.txt'.format(year[-2:])
            file_url = root_url + 'master{0}.txt'.format(year[-2:])
            if not os.path.exists(path_new):
                os.mkdir(path_new)
            newFilename = path_new + '{0}.txt'.format(year)

            # 下载观测计划文件
            if not os.path.exists(srcFilename):
                cmd_get = "wget -P {0} {1}".format(path_src, file_url)
                subprocess.call(cmd_get)

            # 修改文件名称
            if os.path.exists(srcFilename):
                if os.path.exists(newFilename):
                    print("File exists!")
                    continue
                with open(newFilename, 'a') as file:
                    srcFile = open(srcFilename)
                    lines = srcFile.readlines()
                    for line in lines:
                        if line[0:1] == '|':
                            file.write(line)

    def getFileInt(self):
        for year in range(self.start_year, self.end_year):
            year = str(year)
            srcFilename = path_src + 'master{0}-int.txt'.format(year[-2:])
            file_url = root_url + 'master{0}-int.txt'.format(year[-2:])
            if not os.path.exists(path_int):
                os.mkdir(path_int)
            newFilename = path_int + '{0}_int.txt'.format(year)

            # 下载观测计划文件
            if not os.path.exists(srcFilename):
                cmd_get = "wget -P {0} {1}".format(path_src, file_url)
                subprocess.call(cmd_get)

            # 修改文件名称
            if os.path.exists(srcFilename):
                if os.path.exists(newFilename):
                    print("File exists!")
                    continue
                with open(newFilename, 'a') as file:
                    srcFile = open(srcFilename)
                    lines = srcFile.readlines()
                    for line in lines:
                        if line[0:1] == '|':
                            file.write(line)