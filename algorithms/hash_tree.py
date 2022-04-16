from utils.data_preprocessing import getData


"""
    哈希表
    inputs: 数据库中N个指纹模板， M个细节点位置以及方向信息 type: list (N * M * 3 x 1)
    processes: f(L, theta, points.id, id) = (points.id, id)
    outputs: N个指纹模板ID, N * M个核心细节点ID, 特征向量作为索引的参数
"""


# 路径
path1_txt = r'../data_sets/raw_data/TZ_同指.txt'
path2_txt = r'../data_sets/raw_data/TZ_同指200_乱序后_Data.txt'
path3_txt = r'../data_sets/raw_data/TZ_异指.txt'

# 数据集长度
len1 = 1000
len2 = 400
len3 = 10000

# 数据集:
tz_data_sets = getData(path1_txt, len1)
tz_shuffule_data_sets = getData(path2_txt, len2)
yz_data_sets = getData(path3_txt, len3)


# hash_table:
class hash_table():
    def __init__(self, size):
        self.size = size
        self.key = [None] * self.size
        self.data = [None] * self.size

    def hash_func(self, key, size):
        return key % size

    def rehash(self, old, size):
        return (old + 1) % size

    def put(self, key, data):
        hash_val = self.hash_func(key, len(self.key))
        if self.key[hash_val] is None:
            self.key[hash_val] = key
            self.data[hash_val] = data
        else:
            nextsloc = self.rehash(hash_val, len(self.key))
            while self.key[nextsloc] is not None and self.key[nextsloc] != key:
                nextsloc = self.rehash(nextsloc, len(self.key))
            if self.key[nextsloc] == None:
                self.key[nextsloc] = key
                self.data[nextsloc] = data
            else:
                self.data[nextsloc] = data

    def get(self, key):
        startsloc = self.hash_func(key, len(self.key))
        data = None
        stop = False
        found = False
        position = startsloc
        while self.key[position] is not None and not found and not stop:
            if self.key[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.key))
                if position == startsloc:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)


if __name__ == '__main__':
    H = hash_table(len1)
    H.put(key=50, data='cat')
    H.put(key=2000, data='bear')
    print(H[50])
    print(H[2000])
    print(H.get(2000))
