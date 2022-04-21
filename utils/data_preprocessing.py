"""
This script is used for the data preprocessing.
"""
import datetime
import numpy as np


class point(object):
    def __init__(self):
        self.x = None
        self.y = None
        self.dct = None


class Data(object):
    def __init__(self):
        self.id = None
        self.point_number = None
        self.points = point()


# 输入图像文件，输出为数据类Data数组
def getData(path, len):
    t_s = datetime.datetime.now()
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
            # if row[0].count('_'):
            #     data_N[i].id = row[0].split('_')[0]
            # else:
            #     data_N[i].id = row[0]
            data_N[i].id = row[0]
            data_N[i].point_number = row[1]
            num = int(data_N[i].point_number)
            data_N[i].points = [point() for j in range(num)]
            for j in range(2, num * 3 + 2, 3):
                idx = int((j-2)/3)
                data_N[i].points[idx].x = int(row[j])
                data_N[i].points[idx].y = int(row[j+1])
                data_N[i].points[idx].dct = int(row[j+2])
            # print("point_id: ", data_N[i].id)
            # for j in range(num):
            #     print("x: ", data_N[i].points[j].x)
            #     print("y: ", data_N[i].points[j].y)
            #     print("dct: ", data_N[i].points[j].dct)
            #     print("points_id: ", data_N[i].points[j].id)
            # print("***************")
            i += 1
    t_e = datetime.datetime.now()
    print(t_e - t_s)
    myfile.close()
    return data_N


def change_to_temple(a: Data):
    """
    1.返回一个指纹的所有转化
    2.首先一个for循环，遍历m个点
    :param a:
    :return:
    """
    for i in range(int(a.point_number)):
        # 拷贝a的，然后进行减法，减去x[0].x[1]
        print(a.points)
        b = np.array(a.points.x, a.points.y, a.points.dct)
        c = np.zeros((len(b), 2))
        # c[:, 0] = b[:, 0] - a.points[i].x
        # c[:, 1] = b[:, 1] - a.points[i].y
        # 不对，得进行变换，构造，三角变换函数
        bias = np.array(
            [[np.cos(a.points[i].dct), np.sin(a.points[i].dct)], [-1 * np.sin(a.points[i].dct), np.cos(a.points[i].dct)]])
        # 矩阵计算变换后的答案
        d = bias.dot(c.T)
        # 去除自己变换的值，自己变换到原点
        d_1 = np.delete(d, i, axis=1)
        # 第一次变换后，求出最大值和最小值
        y_max = np.max(d_1, axis=1)[1]
        y_min = np.min(d_1, axis=1)[1]
        # 对所有的x进行修正l=（x-1）*y_max
        e = np.zeros((2, len(b)))

        # 第一个是l，第二个是θ
        e[0, :] = d[0, :] - 1
        e[0, :] = e[0, :] * y_max
        e[0, :] = e[0, :] + y_min
        #

        e[1, :] = b[:, 2] - a.points[i].dct
        print(e)
        # 完成后遍历，如果i=j，continue,注意还要对θ进行校验，小于0的要更正

        for j in range(len(e)):
            if i == j:
                continue
            if e[1][j] <= 0:
                e[i][j] += 360
#           离散度为17
            e[i][j] = np.round(e[i][j]/17)