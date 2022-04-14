from data_preprocessing import getData

# 路径
path1 = r'../data_sets/raw_data/TZ_同指.txt'
path2 = r'../data_sets/raw_data/TZ_同指200_乱序后_Data.txt'
path3 = r'../data_sets/raw_data/TZ_异指.txt'

# 数据集长度
len1 = 1000
len2 = 400
len3 = 20000

# 数据集
tz_data_sets = getData(path1, len1)
tz_shuffule_data_sets = getData(path2, len2)
yz_data_sets = getData(path3, len3)
