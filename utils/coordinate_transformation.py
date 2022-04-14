"""极直坐标转换
    input: data_sets type: list
"""
import cmath
from math import radians


def transform(data_sets):
    for i in range(len(data_sets)):
        for j in range(int(data_sets[i].point_number)):
            cn = complex(data_sets[i].points[j][0], data_sets[i].points[j][1])
            data_sets[i].points[j][0], data_sets[i].points[j][1] = cmath.polar(cn)
            data_sets[i].points[j][2] = radians(data_sets[i].points[j][2])
            # print(data_sets[i].points[j])
    return data_sets
