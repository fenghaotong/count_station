# -*- coding: utf-8 -*-
"""
Author  : htfeng
Date    : 20180630
Content : 查询某个台站某一年的观测信息
"""
import os


def query():
    li = []
    obsFileName = "obsType/IVS_type.txt"
    fileObsType = open(obsFileName)
    lines = fileObsType.readlines()
    for line in lines:
        line = line.split()
        li.append(line[0])

    print("please input station:")
    station = input()
    print("please input query year:")
    year = int(input())
    print("please choose follow Type: \n{0}".format(li))
    Type = input()

    path = os.getcwd() + "\\result\\"
    filename = path + station + ".txt"

    with open(filename, 'r') as file:
        lines = file.readlines()
        types = lines[0].split()

        count = 1
        for i in types:
            if Type == i:
                break
            if Type != i:
                count += 1

        for line in lines:
            line = line.split()
            if line[0] == str(year):
                print(line)
                print("{} station {} year {} obsType: {} ".format(station, year, Type, line[count]))