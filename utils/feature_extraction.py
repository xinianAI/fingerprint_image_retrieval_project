from data_preprocessing import getData
from coordinate_transformation import transform

# 路径
path1 = r'../data_sets/raw_data/TZ_同指.txt'
path2 = r'../data_sets/raw_data/TZ_同指200_乱序后_Data.txt'
path3 = r'../data_sets/raw_data/TZ_异指.txt'

# 数据集长度
len1 = 1000
len2 = 400
len3 = 10000

# 数据集
tz_data_sets = getData(path1, len1)
tz_shuffule_data_sets = getData(path2, len2)
yz_data_sets = getData(path3, len3)

# 极直坐标转换后的数据集
tz_data_sets = transform(tz_data_sets)
tz_shuffule_data_sets = transform(tz_shuffule_data_sets)
yz_data_sets = transform(yz_data_sets)

for i in range(len(tz_data_sets)):
    for j in range(int(tz_data_sets[i].point_number)):
        print(tz_data_sets[i].points[j])

# todo：用excel把半径的分布画出来， 丢掉特别小的（100以下）
