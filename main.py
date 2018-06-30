# -*- coding: utf-8 -*-
"""
Author  : htfeng
Date    : 20180629
Content : main函数
"""
import os
from check import Check
from Get_file import GetFile
from count_station import CountStation
from query import query


def main():
    stations = []
    print("please input stations which you need(split in space):")
    stations.append(input().split())
    station = stations[0]
    print("please input start year:")
    start_year = int(input())
    print("please input end year:")
    end_year = int(input())

    # 获取文件
    get_file = GetFile(start_year, end_year)
    get_file.getFile()
    get_file.getFileInt()

    path_nor = os.getcwd() + '\\station\\'
    fileListNor = os.listdir(path_nor)
    path_int = os.getcwd() + '\\stationInt\\'
    fileListInt = os.listdir(path_int)

    # 检测文件
    test = Check(fileListNor)
    test.countFile()

    # 统计台站观测信息
    print("counting....")
    count_station = CountStation(path_nor, fileListNor, station)
    count_station.count()
    # count_station = CountStation(path_int, fileListInt)
    # count_station.countInt()
    print("End")

    # 查寻某个台站的观测信息
    print("Do you need query anyone station Y/N:")
    choice = input()

    if choice == "Y":
        query()


if '__main__' == __name__:
    main()