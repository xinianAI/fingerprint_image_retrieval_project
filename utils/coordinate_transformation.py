"""极直坐标转换
    input: data_sets type: list
"""
import cmath


# 弧度最小单位为1/(180*pi)
import math


def transform(data_sets):
    for i in range(len(data_sets)):
        for j in range(int(data_sets[i].point_number)):
            tmp = math.sqrt(pow(data_sets[i].points[j][0], 2) + pow(data_sets[i].points[j][1], 2))
            data_sets[i].points[j][1] = data_sets[i].points[j][0], data_sets[i].points[j][1] = math.sqrt(pow(data_sets[i].points[j][0], 2) + pow(data_sets[i].points[j][1], 2)), math.atan2(data_sets[i].points[j][0], data_sets[i].points[j][1]),
            data_sets[i].points[j][2] = data_sets[i].points[j][2] / (180 * cmath.pi)
            data_sets[i].points[j][0] = tmp
            # print("arc1", data_sets[i].points[j][1])
            # print("arc2", data_sets[i].points[j][2])
    return data_sets
