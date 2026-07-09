import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号
# 生成模拟股票价格数据（3只股票，100天）
np.random.seed(42)
prices = np.cumprod(1 + np.random.normal(0.001, 0.02, (100, 3)), axis=0) * 100
# 计算日收益率
returns = np.diff(prices, axis=0) / prices[:-1]
# 计算平均收益率和波率
mean_ret = np.mean(returns, axis=0)
vol = np.std(returns, axis=0)
print("--- 金融数据分析 ---")
print("平均收益率:", mean_ret)
print("波动率:", vol)
# 移动平均线（第一只股票，窗口10）
def ma(data, window):
    return np.convolve(data, np.ones(window)/window, mode='valid')
ma10 = ma(prices[:, 0], 10)
print("Stock1 10日移动平均前5值:", ma10[:5])
# 投资组合风险（方差、协方差）
cov = np.cov(returns.T)
weights = np.array([1/3, 1/3, 1/3])
port_var = np.dot(weights.T, np.dot(cov, weights))
port_std = np.sqrt(port_var)
print("\n--- 投资组合风险 ---")
print("协方差矩阵:\n", cov)
print("组合方差:", port_var)
print("组合标准差(风险):", port_std)
# 可视化
plt.figure(figsize=(12, 8))
plt.subplot(2, 2, 1)
plt.plot(prices)
plt.title("股票价格走势")
plt.legend(["S1", "S2", "S3"])
plt.grid(True)
plt.subplot(2, 2, 2)
plt.hist(returns.flatten(), bins=50)
plt.title("收益率分布")
plt.grid(True)
plt.subplot(2, 2, 3)
plt.plot(ma10)
plt.title("Stock1 10日移动平均")
plt.grid(True)
plt.subplot(2, 2, 4)
plt.imshow(cov, cmap='viridis')
plt.colorbar()
plt.title("协方差矩阵热力图")
plt.xticks(range(3), ["S1", "S2", "S3"])
plt.yticks(range(3), ["S1", "S2", "S3"])
plt.tight_layout()
plt.show()