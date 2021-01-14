import matplotlib.pyplot as plt
import numpy as np

# 선 그래프 그리기
x = np.arange(-9, 10)
y1 = x ** 2
plt.plot(
    x, y1
)
plt.show()

# 막대 그래프 그리기
x = np.arange(-9, 10)
plt.bar(x, x ** 2)
plt.show()

# 누적 막대 그래프 그리기
x = np.random.rand(10)
y = np.random.rand(10)
data = [x, y]
x_array = np.arange(10)
for i in range(0, 2) :
    plt.bar(
        x_array,
        data[i],
        bottom=np.sum(data[:i],axis=0)

    )
plt.show()

# 스캐터 그래프 그리기
x = np.random.rand(10)
y = np.random.rand(10)
colors = np.random.randint(0, 100, 10)
sizes = np.random.randint(0, 100, 10)
sizes = np.pi * 1000 * np.random.rand(10)
plt.scatter(x, y, c=colors, s = sizes, alpha=0.7)
plt.show()