# This script is used for the data preprocessing.
import string
import os
import datetime

path1 = r'../data_sets/raw_data/TZ_同指.txt'
path2 = r'../data_sets/raw_data/TZ_同指200_乱序后_Data.txt'
path3 = r'../data_sets/raw_data/TZ_异指.txt'
# myfile1 = open(path1)
# myfile2 = open(path2)
# myfile3 = open(path3)
len1 = 1000
len2 = 400
len3 = 20000


class Data(object):
    class Struct(object):
        def __init__(self, id, p_num, points):
            self.id = id
            self.point_number = p_num
            self.points = points


# 输入图像文件，输出为numpy数组
def getData(path, len):
    t_s = datetime.datetime.now()
    myfile = open(path)
    # lines = len(myfile.readlines())
    data_N = [Data() for i in range(1, len)]
    while 1:
        lines = myfile.readlines(len)
        i = 0
        if not lines:
            break
        for line in lines:
            # print(type(line))
            row = line.split(',')
            if row[0].count('_'):
                data_N[i].id = row[0].split('_')[0]
            else:
                data_N[i].id = row[0]
            data_N[i].point_number = row[1]
            num = int(data_N[i].point_number)
            data_N[i].points = [[int(row[i]), int(row[i+1]), int(row[i+2])] for i in range(2, num*3 + 2, 3)]
            # print(data_N[i].id)
            # print(data_N[i].point_number)
            # print(data_N[i].points)
            i += 1
    t_e = datetime.datetime.now()
    print(t_e - t_s)
    myfile.close()


if __name__ == '__main__':
    getData(path1, len1)
    getData(path2, len2)
    getData(path3, len3)