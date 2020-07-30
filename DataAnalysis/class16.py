import numpy as np

# axis=0 代表的是跨行（跨行就是按照列），所以实际上是对[4, 2] [3, 4] [2, 1]来进行排序，
# 排序结果是[2, 4] [3, 4] [1, 2]，对应的是每一列的排序结果。
# 还原到矩阵中也就是 [[2 3 1], [4, 4, 2]]


a = np.array([[4,3,2],[2,4,1]])
print (np.sort(a))
print (np.sort(a, axis=None))
print (np.sort(a, axis=0))
print (np.sort(a, axis=1))