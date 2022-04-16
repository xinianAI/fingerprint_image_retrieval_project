"""
This script is used for the data preprocessing.
"""


class point(object):
    def __init__(self):
        self.x = None
        self.y = None
        self.dct = None
        self.id = None


class Data(object):
    def __init__(self):
        self.id = None
        self.point_number = None
        self.points = point()


# 输入图像文件，输出为数据类Data数组
def getData(path, len):
    myfile = open(path)
    data_N = [Data() for i in range(1, len+1)]
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
            data_N[i].points = [point() for j in range(num)]
            for j in range(2, num * 3 + 2, 3):
                idx = int((j-2)/3)
                data_N[i].points[idx].x = int(row[j])
                data_N[i].points[idx].y = int(row[j+1])
                data_N[i].points[idx].dct = int(row[j+2])
                data_N[i].points[idx].id = data_N[i].id + "_" + str(idx)
            print("point_id: ", data_N[i].id)
            for j in range(num):
                print("x: ", data_N[i].points[j].x)
                print("y: ", data_N[i].points[j].y)
                print("dct: ", data_N[i].points[j].dct)
                print("id: ", data_N[i].points[j].id)
            print("***************")
            i += 1

    myfile.close()
    return data_N
