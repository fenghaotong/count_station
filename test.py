# -*- coding: utf-8 -*-

"""
Author  : htfeng
Date    : 20180626
Content : 一些函数功能测试
"""
import pandas as pd
dd = {}
data = pd.read_table('obsType/IVS_type1.txt', delim_whitespace=True)
data.set_index('type')
#print(data.ix[0].type[:1], data.ix[0].num)
#print(len(data))
for i in range(len(data)):
    dd[data.ix[i].type] = 0
print(dd)

for i in range(10):
    dd[data.ix[i].type] = dd[data.ix[i].type] + 1
    dd[data.ix[i].type] = dd[data.ix[i].type] + 1
print(dd)

"""
IVSTypes = []
file = open('obsType/IVS_type.txt')
IVSTypeLines = file.readlines()
for line in IVSTypeLines:
    IVSTypes.append(line.strip())
    line = line.split()
    exec("%s = %d" % (line[0], 0))
    #s = vars()[line[0]] + 1
    #print('{0}:{1}'.format(line[0], s))

print(CRF)
"""
dd = {'key':1}
dd['key'] = dd['key'] + 1
print(dd)