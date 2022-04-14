# This script is used for the data preprocessing.
import string
import os
import datetime

# path1 = r'../data_sets/raw_data/TZ_同指.txt'
# path2 = r'../data_sets/raw_data/TZ_同指200_乱序后_Data.txt'
# path3 = r'../data_sets/raw_data/TZ_异指.txt'

# len1 = 1000
# len2 = 400
# len3 = 20000


class Data(object):
    def __init__(self, id='', p_num=0, points=[]):
        self.id = id
        self.point_number = p_num
        self.points = points


# 输入图像文件，输出为数据类Data数组
def getData(path, len):
    # t_s = datetime.datetime.now()
    myfile = open(path)
    data_N = [Data() for i in range(1, len+1)]
    i = 0
    while 1:
        lines = myfile.readlines(len)
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
            data_N[i].points = [[int(row[j]), int(row[j+1]), int(row[j+2])] for j in range(2, num*3 + 2, 3)]
            # print(data_N[i].id)
            # print(data_N[i].point_number)
            # print(data_N[i].points)
            i += 1
    # t_e = datetime.datetime.now()
    # print(t_e - t_s)

    myfile.close()
    return data_N


# if __name__ == '__main__':
#     tz_data_sets = getData(path1, len1)
#     tz_shuffule_data_sets = getData(path2, len2)
#     yz_data_sets = getData(path3, len3)
