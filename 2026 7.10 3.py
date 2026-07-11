import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['Microsoft Yahei']
plt.rcParams['axes.unicode_minus'] = False

print("正在生成模拟空气质量数据...")

# 生成2013-2017年的小时级时间序列（小写 'h' 避免报错）
dates = pd.date_range('2013-01-01', '2017-12-31', freq='h')
np.random.seed(42)
values = np.random.normal(80, 40, len(dates))
values = values * (1 + 0.5 * np.sin(2 * np.pi * dates.month / 12))  # 模拟冬季高、夏季低
pm25 = pd.Series(values, index=dates)

print("数据时间范围：", pm25.index.min(), "到", pm25.index.max())
print("平均PM2.5浓度：", round(pm25.mean(), 2))
print("\n描述统计：")
print(pm25.describe())

# 构建多污染物数据框用于相关性分析
data2 = pd.DataFrame({
    'PM2.5': pm25,
    'PM10': pm25 * 1.5 + np.random.normal(0, 5, len(pm25)),
    'SO2': pm25 * 0.2 + np.random.normal(0, 2, len(pm25)),
    'NO2': pm25 * 0.8 + np.random.normal(0, 10, len(pm25))
}).dropna()

print("\n污染物相关性矩阵：")
print(data2.corr().round(2))

# 绘图
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
pm25.resample('ME').mean().plot(color='orange')  # ✅ 修复：'M' → 'ME'
plt.title('PM2.5 月度平均趋势')
plt.ylabel('μg/m³')

plt.subplot(2, 2, 2)
pm25.hist(bins=50, color='skyblue', edgecolor='black')
plt.title('PM2.5 浓度分布直方图')
plt.xlabel('PM2.5 (μg/m³)')

plt.subplot(2, 2, 3)
plt.scatter(data2['PM2.5'], data2['NO2'], alpha=0.3, s=5)
plt.title('PM2.5 vs NO2 散点图')
plt.xlabel('PM2.5')
plt.ylabel('NO2')

plt.subplot(2, 2, 4)
plt.imshow(data2.corr(), cmap='coolwarm', aspect='auto')
plt.colorbar()
plt.xticks(range(4), data2.columns)
plt.yticks(range(4), data2.columns)
plt.title('污染物相关性热力图')

plt.tight_layout()
plt.show()

# 季节性分析
monthly = pm25.resample('ME').mean()
seasonal = monthly.groupby(monthly.index.month).mean()
print("\n各月平均PM2.5浓度：")
print(seasonal.round(2))
print(f"\n浓度最高的月份：{seasonal.idxmax()}月（冬季污染较重）")
print("\n任务二成功完成。")
