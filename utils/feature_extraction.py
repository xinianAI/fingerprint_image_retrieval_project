import random
import time

from data_preprocessing import getData, get_cluster, tsp, useless_code, change_to_check
from coordinate_transformation import transform
import numpy as np
import pandas
import matplotlib.pyplot as plt
from data_preprocessing import change_to_temple

# 路径
path1_txt = r'../data_sets/raw_data/TZ_同指.txt'
path2_txt = r'../data_sets/raw_data/TZ_同指200_乱序后_Data.txt'
path3_txt = r'../data_sets/raw_data/TZ_异指.txt'

path1_excel = r'../plots/picture_1.xlsx'
path2_excel = r'../plots/picture_2.xlsx'
path3_excel = r'../plots/picture_3.xlsx'

# 数据集长度
len1 = 1000
len2 = 400
len3 = 10000


def get_plot(input):
    for i in range(len(input)):
        N = int(input[i].point_number)
        r = []
        theta = []
        direction = []
        # print(input[i].points)
        # print("len: ", len(input[i].points))
        for j in range(0, N):
            r.append(input[i].points[j][0])
            theta.append(input[i].points[j][1])
            direction.append(input[i].points[j][2])

        r = np.array(r)
        # area = 200 * r ** 2
        area = r * 0.5
        theta = np.array(theta)
        # print("theta_error: ", theta)
        colors = theta
        ax = plt.subplot(111, projection='polar')
        c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)
        plt.show()





if __name__ == '__main__':
    # 数据集
    tz_data_sets = getData(path1_txt, len1)
    tz_shuffule_data_sets = getData(path2_txt, len2)
    yz_data_sets = getData(path3_txt, len3)
    time_start = time.time()


    # for i in range(len(yz_data_sets)):

    center = get_cluster(tz_data_sets[0])
    # hash_tr = useless_code(center)
    dist, lists = tsp(center)
    center1 = get_cluster(tz_data_sets[1])
    bias =(center.max(axis=0)[2]-center1.max(axis=0)[2])
    dist, lists1 = tsp(center1,bias)
    # print(np.sum((lists-lists1)**2))
    # center2 = get_cluster(tz_data_sets[2])
    # dist, lists2 = tsp(center2)
    # # print(np.sum((lists - lists2) ** 2))
    print(np.corrcoef(lists,lists1))
    # print(center[:,2].reshape(1,-1).shape)
    x=np.vstack((center[:,2].reshape(1,-1),center1[:,2].reshape(1,-1)))
    print(np.corrcoef(x))


    # dist1=dist*1.1
    # dist2=dist*0.9
    # total_dist=np.zeros(len(tz_data_sets))
    # 下面是离线阶段
    # hash_map = {}
    # for i in range(len(tz_data_sets)):
    #     center1 = get_cluster(tz_data_sets[i])
    #     a,b=tsp(center1)
    #     total_dist[i]=a
    #     hash_map[i]=lists
    # c=np.where(total_dist <=dist1)
    # x =np.where(total_dist >=dist2)
    # for i in c:
    #     if i in x:
    #         print(i)
    #
    # print(c)

    # for
    #
    # cp1, cp = get_cluster(tz_data_sets[1])
    # tsp(cp1)

    # time_end = time.time()

    # # 极直坐标转换后的数据集
    # tz_data_sets = transform(tz_data_sets)
    # tz_shuffule_data_sets = transform(tz_shuffule_data_sets)
    # yz_data_sets = transform(yz_data_sets)
    #
    # get_plot(tz_data_sets)
    # get_plot(tz_shuffule_data_sets)
    # get_plot(yz_data_sets)

