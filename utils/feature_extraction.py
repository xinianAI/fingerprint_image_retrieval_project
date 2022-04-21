
from data_preprocessing import getData
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


# def remove_fake_feature(input):
#     for i in range(len(input)):
#         for j in range(int(input[i].point_number)):
#             if(input[i].points[j].)


def get_plot(input):
    for i in range(0, len(input), 2):
        N = int(input[i].point_number)
        N_ = int(input[i+1].point_number)
        r = []
        r_ = []
        theta = []
        theta_ = []
        direction = []
        direction_ = []
        # print(input[i].points)
        # print("len: ", len(input[i].points))
        for j in range(0, N):
            r.append(input[i].points[j].x)
            theta.append(input[i].points[j].y)
            direction.append(input[i].points[j].dct)
        for j in range(0, N_):
            r_.append(input[i + 1].points[j].x)
            theta_.append(input[i + 1].points[j].y)
            direction_.append(input[i + 1].points[j].dct)

        r = np.array(r)
        area = r * 0.5
        theta = np.array(theta)
        direction = np.array(direction)
        x = np.array([1] * N)
        y = np.tan(direction)
        colors = theta
        ax = plt.subplot(1, 2, 1, projection='polar')
        # ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)
        ax.quiver(theta, r, x, y, colors, scale_units='xy')
        # plt.title(input[i].id + "_0", fontsize='large')

        r_ = np.array(r_)
        area_ = r_ * 0.5
        theta_ = np.array(theta_)
        direction_ = np.array(direction_)
        x_ = np.array([1] * N_)
        y_ = np.tan(direction_)
        colors_ = theta_

        ax_ = plt.subplot(1, 2, 2, projection='polar')
        # ax_.scatter(theta_, r_, c=colors_, s=area_, cmap='hsv', alpha=0.75)
        ax_.quiver(theta_, r_, x_, y_, colors_, scale_units='xy')
        # plt.title(input[i+1].id + "_1", fontsize='x-large')
        plt.tight_layout()
        # plt.subplots_adjust(wspace=0, hspace=0)  # 调整子图间距
        # plt.suptitle("A case of success_matching fingerprint plots")
        plt.suptitle("A case of different fingerprint plots")
        plt.show()


if __name__ == '__main__':
    # 数据集
    tz_data_sets = getData(path1_txt, len1)
    tz_shuffule_data_sets = getData(path2_txt, len2)
    yz_data_sets = getData(path3_txt, len3)
    # change_to_temple(tz_data_sets[0])

    # 极直坐标转换后的数据集
    tz_data_sets = transform(tz_data_sets)
    tz_shuffule_data_sets = transform(tz_shuffule_data_sets)
    yz_data_sets = transform(yz_data_sets)

    # get_plot(tz_data_sets)
    # get_plot(tz_shuffule_data_sets)
    get_plot(yz_data_sets)
