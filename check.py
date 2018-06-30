# -*- coding: utf-8 -*-
"""
Author  : htfeng
Date    : 20180626
Content : 检查程序是否正确
"""


class Check:
    def __init__(self, file):
        self.file = file

    # 统计文件个数
    def countFile(self):
        file_count = 0
        for i in range(len(self.file)):
            if 'txt' in self.file[i]:
                file_count += 1

        return file_count

    def checkYearPlans(self):
        year_plans = []

        file = open(self.file)
        lines = file.readlines()
        for line in lines:
            line = line.replace('|', '\t')
            if '------' not in line:
                year_plans.append(line.split())

        return year_plans

    # 查看IVS观测类型
    def ivsTypes(self):
        IVS_types = []

        file = open('IVS_type.txt')
        IVS_type_lines = file.readlines()
        for line in IVS_type_lines:
            IVS_types.append(line.strip())

        return IVS_types

    # 检测IVS观测类型是否覆盖了所有的观测计划
    def checkCover(self, year_plans, IVS_types):
        j = 0
        plans = []

        for plan in range(len(year_plans)):
            for IVS_type in range(len(IVS_types)):
                if IVS_types[IVS_type] in year_plans[plan][1] \
                        and IVS_types[IVS_type][:1] == year_plans[plan][1][:1]:
                    plans.append(year_plans[plan][1])
                    j += 1

        return j,plans

    #检测读写的观测计划是否一一对应
    def checkEqual(self, plans, year_plans):
        i = 0

        for i in range(len(plans)):
            if plans[i] == year_plans[i][1]:
                i += 1
            else:
                print(i)

        return i