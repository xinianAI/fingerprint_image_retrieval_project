# demo

# todo：完成快速选择
import math
from utils.coordinate_transformation import transform_1

from utils.data_preprocessing import Data


# 进行检验哪一个图像的值可以匹配
class solver():
    def __init__(self):
        pass

    # 计算两个的原始最近，使用cos距离
    # 返回ab，2个里面最相似的点
    @staticmethod
    def get_change_1(a: Data, b: Data) -> (Data, Data):
        p = None
        q = None
        l = 400.0
        for i in a.points:
            for j in b.points:
                fenmu = math.sqrt(i[0] ** 2 + i[1] ** 2 + i[2] ** 2) * math.sqrt(j[0] ** 2 + j[1] ** 2 + j[2] ** 2)
                fenzi = i[0] * j[0] + i[1] * j[1] + i[2] * j[2]
                fenzi = float(fenzi)
                if l < (fenzi / fenmu):
                    p = i
                    q = j
        return p, q

    # 还是使用圆这种方法吧
    """
    1.构建局部周围的向量
    2.取周围大于10的为领域点
    
    """

    @staticmethod
    def get_change_2(a: Data, b: Data) -> (Data, Data):
        R = 80
        θ = 7
        pass

    '''
    1.进行平移变换，按照pq
    2.这个就是算法里的
    '''

    @staticmethod
    def trans(a: Data, b: Data, p: list, q: list):
        for i in a.points:
            r, e, beta = transform_1(p, i)
            i[0] = r
            i[1] = e
            i[2] = beta

        for j in b.points:
            r, e, beta = transform_1(q, j)
            j[0] = r
            j[1] = e
            j[2] = beta
