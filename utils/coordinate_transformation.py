"""极直坐标转换
    input: data_sets type: list
"""
import cmath

# 弧度最小单位为1/(180*pi)
import math


def transform(data_sets):
    for i in range(len(data_sets)):
        for j in range(int(data_sets[i].point_number)):
            tmp = math.sqrt(pow(data_sets[i].points[j].x, 2) + pow(data_sets[i].points[j].y, 2))
            data_sets[i].points[j].y = data_sets[i].points[j].x, data_sets[i].points[j].y = math.sqrt(
                pow(data_sets[i].points[j].x, 2) + pow(data_sets[i].points[j].y, 2)), math.atan2(
                data_sets[i].points[j].x, data_sets[i].points[j].y),
            data_sets[i].points[j].dct = data_sets[i].points[j].dct / (180 * cmath.pi)
            data_sets[i].points[j].x = tmp
            # print("arc1", data_sets[i].points[j][1])
            # print("arc2", data_sets[i].points[j][2])
    return data_sets


def transform_1(p: list, a: list) :
    """
    1.返回以我p为中心的转化的极坐标
    :return:
    """
    r = (p[0] - a[0]) ** 2 + (p[1] - a[1]) ** 2
    r = math.sqrt(r)
    e = math.atan(float(p[1] - a[1]) / float(p[0] - a[0]))
    beta = a[2] - p[2]
    return r, e, beta
