"""
This script is used for the data preprocessing.
"""
import random

import numpy as np
from python_tsp.heuristics import solve_tsp_simulated_annealing
from sko.GA import GA_TSP
from python_tsp.exact import solve_tsp_dynamic_programming
import matplotlib.pylab as plt
from sklearn.cluster import KMeans
from skfuzzy.cluster import cmeans


class Data(object):
    def __init__(self, id='', p_num=0, points=[]):
        self.id = id
        self.point_number = p_num
        self.points = points


# 输入图像文件，输出为数据类Data数组
def getData(path, len):
    myfile = open(path)
    data_N = [Data() for i in range(1, len + 1)]
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
            data_N[i].points = [[int(row[j]), int(row[j + 1]), int(row[j + 2])] for j in range(2, num * 3 + 2, 3)]
            # print(data_N[i].id)
            # print(data_N[i].point_number)
            # print(data_N[i].points)
            i += 1

    myfile.close()
    return data_N


def change_to_temple(a: Data):
    """
    1.返回一个指纹的所有转化
    2.首先一个for循环，遍历m个点
    :param a:
    :return:返回一个dict
    """
    hash_tr = {}
    for i in range(len(a.points)):
        # 拷贝a的，然后进行减法，减去x[0].x[1]
        b = np.array(a.points)
        c = np.zeros((len(b), 2))
        c[:, 0] = b[:, 0] - a.points[i][0]
        c[:, 1] = b[:, 1] - a.points[i][1]
        # 不对，得进行变换，构造，三角变换函数
        bias = np.array(
            [[np.cos(a.points[i][2]), np.sin(a.points[i][2])], [-1 * np.sin(a.points[i][2]), np.cos(a.points[i][2])]])
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

        e[1, :] = b[:, 2] - a.points[i][2]

        # 完成后遍历，如果i=j，continue,注意还要对θ进行校验，小于0的要更正
        # 第2行都是角度
        for j in range(len(b)):
            if i == j:
                continue
            if e[1][j] <= 0:
                e[1][j] += 360
            #           离散度为17
            # e[1][j] = np.round(e[1][j] / 17)
            e[0][j] = np.round(e[0][j])

            hash_tr[(e[0][j], e[1][j])] = 1
    return hash_tr


# def change_to_check(a: Data, hash_tr: dict):
#     """
#     1.返回一个指纹的所有转化
#     2.首先一个for循环，遍历m个点
#     :param a:
#     :return:返回一个dict
#     """
#     hash_tr = {}
#     for i in range(len(a.points)):
#         # 拷贝a的，然后进行减法，减去x[0].x[1]
#         b = np.array(a.points)
#         c = np.zeros((len(b), 2))
#         c[:, 0] = b[:, 0] - a.points[i][0]
#         c[:, 1] = b[:, 1] - a.points[i][1]
#         # 不对，得进行变换，构造，三角变换函数
#         bias = np.array(
#             [[np.cos(a.points[i][2]), np.sin(a.points[i][2])], [-1 * np.sin(a.points[i][2]), np.cos(a.points[i][2])]])
#         # 矩阵计算变换后的答案
#         d = bias.dot(c.T)
#         # 去除自己变换的值，自己变换到原点
#         d_1 = np.delete(d, i, axis=1)
#         # 第一次变换后，求出最大值和最小值
#         y_max = np.max(d_1, axis=1)[1]
#         y_min = np.min(d_1, axis=1)[1]
#         # 对所有的x进行修正l=（x-1）*y_max
#         e = np.zeros((2, len(b)))
# 
#         # 第一个是l，第二个是θ
#         e[0, :] = d[0, :] - 1
#         e[0, :] = e[0, :] * y_max
#         e[0, :] = e[0, :] + y_min
#         #
# 
#         e[1, :] = b[:, 2] - a.points[i][2]
# 
#         # 完成后遍历，如果i=j，continue,注意还要对θ进行校验，小于0的要更正
#         # 第2行都是角度
#         for j in range(len(b)):
#             if i == j:
#                 continue
#             if e[1][j] <= 0:
#                 e[1][j] += 360
#             #           离散度为17
#             # e[1][j] = np.round(e[1][j] / 17)
#             e[0][j] = np.round(e[0][j])
#             for p in range(-100, 100):
#                 # print(p)
#                 if (e[0][j] + p, e[1][j]) in hash_tr.keys():
#                     print("yes")
#                 if (e[0][j], e[1][j] + p % 10) in hash_tr.keys():
#                     print("yes")
def change_to_check(a, hash_tr: dict):
    """
    1.返回一个指纹的所有转化
    2.首先一个for循环，遍历m个点
    :param a:
    :return:返回一个dict
    """
    hash_tr = {}
    for i in range(len(a)):
        # 拷贝a的，然后进行减法，减去x[0].x[1]
        b = np.array(a)
        c = np.zeros((len(b), 2))
        c[:, 0] = b[:, 0] - a[i][0]
        c[:, 1] = b[:, 1] - a[i][1]
        # 不对，得进行变换，构造，三角变换函数
        bias = np.array(
            [[np.cos(a[i][2]), np.sin(a[i][2])], [-1 * np.sin(a[i][2]), np.cos(a[i][2])]])
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

        e[1, :] = b[:, 2] - a[i][2]

        # 完成后遍历，如果i=j，continue,注意还要对θ进行校验，小于0的要更正
        # 第2行都是角度
        for j in range(len(b)):
            if i == j:
                continue
            if e[1][j] <= 0:
                e[1][j] += 360
            #           离散度为17
            # e[1][j] = np.round(e[1][j] / 17)
            e[0][j] = np.round(e[0][j])
            for p in range(-100, 100):
                # print(p)
                if (e[0][j] + p, e[1][j]) in hash_tr.keys():
                    print("yes")
                if (e[0][j], e[1][j] + p % 10) in hash_tr.keys():
                    print("yes")


def get_cluster(a: Data):
    cp = np.array(a.points)
    # 对方向放量进行扩大，以免有影响
    cp[cp > 180] = 360 - cp[cp > 180]
    cp[:, 2] = cp[:, 2] * 8
    # 进行转置
    cp = cp.T
    center, u, u0, d, jm, p, fpc = cmeans(cp, c=6, m=2, error=0.005, maxiter=1000)
    # 计算最短路

    center = np.sort(center, axis=0)
    center[:, 2] = center[:, 2] / 8
    # print(center)
    return center


def useless_code(a):
    hash_tr = {}
    for i in range(len(a)):
        # 拷贝a的，然后进行减法，减去x[0].x[1]
        b = np.array(a)
        c = np.zeros((len(b), 2))
        c[:, 0] = b[:, 0] - a[i][0]
        c[:, 1] = b[:, 1] - a[i][1]
        # 不对，得进行变换，构造，三角变换函数
        bias = np.array(
            [[np.cos(a[i][2]), np.sin(a[i][2])], [-1 * np.sin(a[i][2]), np.cos(a[i][2])]])
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

        e[1, :] = b[:, 2] - a[i][2]

        # 完成后遍历，如果i=j，continue,注意还要对θ进行校验，小于0的要更正
        # 第2行都是角度
        for j in range(len(b)):
            if i == j:
                continue
            if e[1][j] <= 0:
                e[1][j] += 360
            #           离散度为17
            # e[1][j] = np.round(e[1][j] / 17)
            e[0][j] = np.round(e[0][j])

            hash_tr[(e[0][j], e[1][j])] = 1
    return hash_tr


def tsp(center,bias=0):
    cp1 = center[:, :-1]
    # 构建3*3的矩阵

    dis = np.zeros((len(center), len(center)))
    for i in range(len(center)):
        for j in range(len(center)):

            dis[i][j] = np.sqrt((cp1[i][0] - cp1[j][0]) ** 2 + (cp1[i][1] - cp1[j][1]) ** 2)

    permutation, distance = solve_tsp_dynamic_programming(dis)
    print(permutation, distance)

    # 进行角度偏移,加入距离
    lists = []
    angle = []
    hash_map = {}
    lists.append(dis[permutation[0]][permutation[len(center) - 1]])
    hash_map[dis[permutation[0]][permutation[len(center) - 1]]] = len(center) - 1

    for i in range(0, len(center) - 1):
        lists.append(dis[permutation[i + 1]][permutation[i]])
        hash_map[dis[permutation[i + 1]][permutation[i]]] = i
        if center[permutation[i]][2] - center[0][2] > 0:
            angle.append(center[permutation[i]][2] - center[0][2])
        else:
            angle.append((center[permutation[i]][2] - center[0][2]) + 360)
    lists.sort()
    lists = np.array(lists)
    k = []
    # p是最小的边的细节点
    p = hash_map[lists[0]]
    for i in lists:
        x = hash_map[i]

        if x == len(center) - 1:
            k.append((cp1[len(center) - 1][1] - cp1[0][1]) / (cp1[len(center) - 1][0] - cp1[0][0]) - bias)
        else:
            k.append((cp1[x][1] - cp1[x + 1][1]) / (cp1[x][0] - cp1[x + 1][0]) - bias)
    # for i in permutation:
    #     if i<len(cp1)-1:
    #         k.append((cp1[i][1] - cp1[i + 1][1]) / (cp1[i][0] - cp1[i + 1][0] - center[0][2]))
    #     else:
    #         k.append((cp1[len(center) - 1][1] - cp1[0][1]) / (cp1[len(center) - 1][0] - cp1[0][0]) - center[0][2])

    # lists是长度，perm是映射，最长对最长
    # ans = []
    # for i in lists:
    #     ans.append(hash_map[i])
    # print(permutation,distance,lists,angle)
    # print()
    # print(k)
    return distance, lists


def save_txt(tz_data_sets, yz_data_sets):
    v = random.sample(range(len(tz_data_sets) // 2), 18)
    # 这是配对了的
    ans = []
    k = 0
    for i in v:
        if k >= 0:
            p1 = i * 2
            p2 = i * 2 + 1
            s = tz_data_sets[p1].id + '_0'
            ans.append(s)
            s = tz_data_sets[p2].id + '_1'
            ans.append(s)
        else:
            p1 = i * 2
            if k % 2 == 0:
                s = tz_data_sets[p1].id + '_0'
            else:
                s = tz_data_sets[p1].id + '_1'
            ans.append(s)
            k += 1

        # print(ans, len(ans))

    v = random.sample(range(len(yz_data_sets)), 294)
    for i in v:
        s = yz_data_sets[i].id + '_0'
        ans.append(s)
        random.shuffle(ans)

    random.shuffle(ans)
    print(ans)
    with open("97的穿透率(18,18).txt", 'w') as f:
        for i in ans:
            f.write(i + '\n')
