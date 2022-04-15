from data_preprocessing import getData
from coordinate_transformation import transform
import numpy as np
import pandas
import matplotlib.pyplot as plt
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

    # 极直坐标转换后的数据集
    tz_data_sets = transform(tz_data_sets)
    tz_shuffule_data_sets = transform(tz_shuffule_data_sets)
    yz_data_sets = transform(yz_data_sets)

    get_plot(tz_data_sets)
    get_plot(tz_shuffule_data_sets)
    get_plot(yz_data_sets)
