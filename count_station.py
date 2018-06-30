# -*- coding: utf-8 -*-
"""
Author  : htfeng
Date    : 20180626
Content : 统计IVS台站观测数量
"""
import os


class CountStation():
    def __init__(self, path, file_list, station):
        self.path = path
        self.file_list = file_list
        self.station = station

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

            with open(filename, 'a') as file:
                file.write(
                    '\t' + 'R1' + '\t' + 'R4' + '\t' + 'T2' + '\t' + 'CRF' + '\t' + 'CRD' + '\t' + 'RD' + '\t' + 'APSG' + '\t' + 'AOV' + '\t' + 'AUA' + '\t' + 'RV' + '\t' + 'EUR' + '\t' + 'OHG' + '\t' + 'C' + '\t' + 'V' + '\t' + 'AUG' + '\t' + 'HOB' + '\t' + 'JX' + '\t' + 'JD' + '\t' + 'BG' + '\t' + 'A1' + '\t' + 'OHIG' + '\t' + 'AUS' + '\t' + 'CRM' + '\n')

            # year = (2, 4, 6, 8, 10, 12)

            for i in range(len(self.file_list)):
                with open(filename, 'a') as file:
                    year_plans = []

                    R1 = 0
                    R4 = 0
                    T2 = 0
                    CRF = 0
                    CRD = 0
                    RD = 0
                    APSG = 0
                    AOV = 0
                    AUA = 0
                    RV = 0
                    EUR = 0
                    OHG = 0
                    C1 = 0
                    V1 = 0
                    AUG = 0
                    HOB = 0
                    JX = 0
                    JD = 0
                    BG = 0
                    A1 = 0
                    OHIG = 0
                    AUS = 0
                    CRM = 0
                    fileList = open(self.path + self.file_list[i])
                    lines = fileList.readlines()
                    for line in lines:
                        line = line.replace('|', '\t')
                        if '------' not in line:
                            year_plans.append(line.split())

                    IVSTypes = []

                    file_2 = open(pathType + 'IVS_type.txt')
                    IVSTypeLines = file_2.readlines()
                    for line in IVSTypeLines:
                        IVSTypes.append(line.strip())

                    for plan in range(len(year_plans)):
                        for IVSType in range(len(IVSTypes)):
                            if IVSTypes[IVSType] in year_plans[plan][1] \
                                    and IVSTypes[IVSType][:1] == year_plans[plan][1][:1] \
                                    and self.station[li] in year_plans[plan][6]:
                                if IVSTypes[IVSType] == 'R1':
                                    R1 += 1
                                if IVSTypes[IVSType] == 'R4':
                                    R4 += 1
                                if IVSTypes[IVSType] == 'T2':
                                    T2 += 1
                                if IVSTypes[IVSType] == 'CRF':
                                    CRF += 1
                                if IVSTypes[IVSType] == 'CRD':
                                    CRD += 1
                                if IVSTypes[IVSType] == 'RD':
                                    RD += 1
                                if IVSTypes[IVSType] == 'APSG':
                                    APSG += 1
                                if IVSTypes[IVSType] == 'AOV':
                                    AOV += 1
                                if IVSTypes[IVSType] == 'AUA':
                                    AUA += 1
                                if IVSTypes[IVSType] == 'RV':
                                    RV += 1
                                if IVSTypes[IVSType] == 'EUR':
                                    EUR += 1
                                if IVSTypes[IVSType] == 'OHG':
                                    OHG += 1
                                if IVSTypes[IVSType] == 'C1':
                                    C1 += 1
                                if IVSTypes[IVSType] == 'V1':
                                    V1 += 1
                                if IVSTypes[IVSType] == 'AUG':
                                    AUG += 1
                                if IVSTypes[IVSType] == 'HOB':
                                    HOB += 1
                                if IVSTypes[IVSType] == 'JX':
                                    JX += 1
                                if IVSTypes[IVSType] == 'JD':
                                    JD += 1
                                if IVSTypes[IVSType] == 'BG':
                                    BG += 1
                                if IVSTypes[IVSType] == 'A1':
                                    A1 += 1
                                if IVSTypes[IVSType] == 'OHIG':
                                    OHIG += 1
                                if IVSTypes[IVSType] == 'AUS':
                                    AUS += 1
                                if IVSTypes[IVSType] == 'CRM':
                                    CRM += 1
                    file.write(self.file_list[i][:4] + '\t' + '{}'.format(R1) + '\t' + '{}'.format(R4) + '\t' + '{}'.format(
                        T2) + '\t' + '{}'.format(CRF) + '\t' + '{}'.format(CRD) + '\t' + '{}'.format(RD) + '\t' + '{}'.format(
                        APSG) + '\t' + '{}'.format(AOV) + '\t' + '{}'.format(AUA) + '\t' + '{}'.format(RV) + '\t' + '{}'.format(
                        EUR) + '\t' + '{}'.format(OHG) + '\t' + '{}'.format(C1) + '\t' + '{}'.format(V1) + '\t' + '{}'.format(
                        AUG) + '\t' + '{}'.format(HOB) + '\t' + '{}'.format(JX) + '\t' + '{}'.format(JD) + '\t' + '{}'.format(
                        BG) + '\t' + '{}'.format(A1) + '\t' + '{}'.format(OHIG) + '\t' + '{}'.format(AUS) + '\t' + '{}'.format(
                        CRM) + '\n')


