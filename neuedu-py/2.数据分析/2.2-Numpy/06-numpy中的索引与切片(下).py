import numpy as np

# 花式索引
# 可以指定利用整数数组进行索引
# 为了以特定的顺序选取子矩阵,只需要传入一个用于指定顺序的整数列表即可

# 2维
# n1 = np.arange(64).reshape((8, 8))
# print(n1)

# 取矩阵中单一的元素
# print(n1[0][0])
# print(n1[0, 7])

# 取二维矩阵中第一个向量
# print(n1[0])

# 通过花式索引可以取多行(多个一维向量)  => 新的矩阵(行数取决于列表元素的个数 列就是一维向量的列)
# print(n1[[0, 3, 2, 1]])
# n1[[0, 3, 2, 1]][0, 0] = 999
# n1[[0, 3, 2, 1]]形成了一个新数组，[0,0]则是其第零行第零列
# print(n1)

# 在矩阵中取多个值   => (0, 0) (2, 1) (1, 3)
# print(n1[[0, 2, 1], [0, 1, 3]])

# 取区域
# print(n1[:2, :2])
# 取区域(利用花式索引取)
# print(n1[[0, 3, 5]][:, [0, 3, 1, 2]])

# 对花式索引切出的区域在次进行切割(切的是行)
# print(n1[[0, 3, 5]][:2, [0, 3, 1, 2]])
# 把n1[[0, 3, 5]] 的第二行去掉

arr = np.arange(32).reshape(8, 4)
# print(arr)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]
#  [12 13 14 15]
#  [16 17 18 19]
#  [20 21 22 23]
#  [24 25 26 27]
#  [28 29 30 31]]

# print(arr[[0, 4, 5], [0, 1, 2]])# 第一个数组是x，第二个数组是y，所以是00 41 52三个点
# print(arr[[0, 4, 5]])# 取0 4 5行组成3*4数组
# print(arr[[0, 4, 5]][:, [0, 3, 1, 2]])# 后者的[a,b],a表示行切片（这里未做任何切片），b表示列切片
# print(arr[[0, 4, 5]][:2, [0, 3, 1, 2]])# 行切片，步进2，所以只保留了第一第三行
# print(arr[3:4, 2:])
# print((arr[3:4, 2:3]).shape)

# 3维 0轴 1轴 2轴
n4 = np.arange(18).reshape(2, 3, 3)
print(n4)
print(n4.shape)
print(n4.ndim)
print("*" * 50)

# 1. 取值
# print(n4[0, 0, 0])

# 2. 当取值的索引数少于真实的轴数
# print(n4[0, 1])

# 3. 通过切片取值
# print(n4[:2, :3, :1])

# 4. 取子区域(子矩阵)
# print(n4[1:, 1:, 1:])

# 5. 通过花式索引取值
# 组合(0, 1, 2) (1, 1, 2)
# print(n4[[0, 1], [1, 1], [2, 2]])

# 6. 通过花式索引取矩阵
# print(arr[[0, 4, 5]][:2, [0, 3, 1, 2]])

# 和二维花式索引切片不一样的地方是, 在二维花式索引中, 第一个:操作的是行, 而这里操作的是:列
# print(n4[[1, 0]])
# print("*" * 50)
# print(n4[[1, 0]][:, :1, [2, 1]])

# 子区域 14 13
#        17 16
# print(n4[[1]][:, 1:3, [2, 1]])



























