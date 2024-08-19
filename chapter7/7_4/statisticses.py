import statistics


data = [1, 2, 2, 3, 4, 5, 6]
# 平均
print(statistics.mean(data))
# 幾何平均
print(statistics.geometric_mean(data))
# 中央値
print(statistics.median(data))

# 分散
print(statistics.pvariance(data))
