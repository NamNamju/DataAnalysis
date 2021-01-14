import matplotlib.pyplot as plt
import numpy as np

# 기본 직선형
x = [1, 2, 3]
y = [1, 2, 3]
plt.plot(x, y)
plt.title("My Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
# plt.savefig("picture.png") 특정한 이름으로 이미지 파일 저장

# 사인함수, 코사인 함수
x = np.linspace(0, np.pi * 10, 500) # 0부터 pi * 10까지 500개 간격의 점
fig, axes = plt.subplots(2, 1)  # 2개의 그래프가 들어감.
axes[0].plot(x, np.sin(x))
axes[1].plot(x, np.cos(x))
plt.show()

# 2차함수
x = np.arange(-9 ,10)
y1 = x ** 2
plt.plot(x, y1, linestyle = ":", marker="*") # 라인과 점 스타일
plt.show()

# legend
y2 = -x
plt.plot(x, y1, linestyle = ":", marker="*", color = "red",label="y = x*x")
plt.plot(x, y2, linestyle="-", marker="o",color="blue",label="y = -x")
plt.legend(
    shadow=True,
    borderpad=1
)
plt.show()
