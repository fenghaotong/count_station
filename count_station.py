# -*- coding: utf-8 -*-
"""
Author  : htfeng
Date    : 20180626
Content : 统计IVS台站观测数量
"""
import os
import pandas as pd

class CountStation():
    def __init__(self, path, file_list, station, start_year, end_year):
        self.path = path
        self.file_list = file_list
        self.station = station
        self.start_year = start_year
        self.end_year = end_year

    # 统计INT观测结果
    def countInt(self):
        print('\t' + 'INT')

        for i in range(len(self.file_list)):
            year_plans = []
            file_1 = open(self.path + self.file_list[i])
            lines = file_1.readlines()
            for line in lines:
                line = line.replace('|', '\t')
                if '------' not in line:
                    year_plans.append(line.split())

            j = 0
            for plan in range(len(year_plans)):
                if 'Sh' in year_plans[plan][6]:
                    j += 1
            print(self.file_list[i][:4] + '\t' + '{}'.format(j))

    # 统计IVS观测结果
    def count(self):
        # station = ['Sh', 'Ur', 'Km']
        pathResult = os.getcwd() + "\\result\\"
        pathType = os.getcwd() + "\\obsType\\"

        if not os.path.exists(pathResult):
            os.mkdir(pathResult)
        if not os.path.exists(pathType):
            os.mkdir(pathType)

        for li in range(len(self.station)):
            filename = pathResult + self.station[li] + '.txt'
            with open(filename, 'w') as file:
                file.truncate()

            # 写入保存文件表头
            data = pd.read_table('obsType/IVS_type.txt', delim_whitespace = True)
            data.set_index('type')
            with open(filename, 'a') as file:
                file.write('year\t')
                for IVSType in range(len(data)):
                    file.write('{0}'.format(data.ix[IVSType].type) + "\t")
                file.write('\n')

            for i in range(len(self.file_list)):
                fileYear = int(self.file_list[i][:4])
                if (fileYear >= self.start_year) and (fileYear < self.end_year):
                    with open(filename, 'a') as file:
                        # 读取观测类型文件，存到一个字典中
                        dd = {}
                        for j in range(len(data)):
                            dd[data.ix[j].type] = 0

                        # 保存每一年的观测计划
                        year_plans = []
                        fileList = open(self.path + self.file_list[i])
                        lines = fileList.readlines()
                        for line in lines:
                            line = line.replace('|', '\t')
                            if '------' not in line:
                                year_plans.append(line.split())

                        # 计数
                        for plan in range(len(year_plans)):
                            for IVSType in range(len(data)):
                                if data.ix[IVSType].type in year_plans[plan][1] \
                                        and data.ix[IVSType].type[:1] == year_plans[plan][1][:1] \
                                        and self.station[li] in year_plans[plan][6]:
                                    dd[data.ix[IVSType].type] = dd[data.ix[IVSType].type] + 1
                        # 写入文件
                        file.write(self.file_list[i][:4] + '\t')
                        for IVSType in range(len(data)):
                            file.write('{0}'.format(dd[data.ix[IVSType].type]) + "\t")
                        file.write('\n')
