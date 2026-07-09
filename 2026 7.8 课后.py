import numpy as np
# 1. 创建不同维度数组
arr_1d = np.array([1, 2, 3, 4, 5, 6])
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("1D数组:", arr_1d)
print("2D数组:\n", arr_2d)
print("3D数组:\n", arr_3d)
# 2. 索引与切片
print("\n--- 索引与切片 ---")
print("第二行第三列:", arr_2d[1, 2])
print("所有行第一列:", arr_2d[:, 0])
print("前三个元素:", arr_1d[:3])
# 3. 形状变换
print("\n--- 形状变换 ---")
arr_reshaped = arr_1d.reshape(2, 3)
print("重塑为2x3:\n", arr_reshaped)
print("展平:", arr_reshaped.ravel())
print("转置:\n", arr_reshaped.T)
# 4. 矩阵运算函数
def mat_add(a, b):
    return a + b
def mat_mul(a, b):
    return np.dot(a, b)
def mat_transpose(a):
    return a.T
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print("\n--- 矩阵运算 ---")
print("加法:\n", mat_add(A, B))
print("乘法:\n", mat_mul(A, B))
print("转置:\n", mat_transpose(A))
# 5. 随机数据与统计
np.random.seed(0)
data = np.random.rand(10)
print("\n--- 随机数据统计 ---")
print("均值:", np.mean(data))
print("标准差:", np.std(data))
print("最大值:", np.max(data))
print("最小值:", np.min(data))
