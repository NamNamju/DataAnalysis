import cv2
import matplotlib.pyplot as plt
import numpy as np

# 이미지 크기 조절

image = cv2.imread('cat.jpg')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()

# 이미지 크게
expand = cv2.resize(image, None, fx=2.0, fy = 2.0, interpolation=cv2.INTER_CUBIC)
plt.imshow(cv2.cvtColor(expand, cv2.COLOR_BGR2RGB))
plt.show()

# 이미지 작게
shrink = cv2.resize(image, None, fx = 0.8, fy = 0.8, interpolation=cv2.INTER_AREA)
plt.imshow(cv2.cvtColor(expand,cv2.COLOR_BGR2RGB))
plt.show()

# 이미지 위치 변경

height, width = image.shape[:2]

M = np.float32([[1, 0, 50], [0, 1, 10]])
dst = cv2.warpAffine(image, M, (width, height))

plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)
plt.show()

# 이미지 회전

M = cv2.getRotationMatrix2D((width / 2, height / 2), 90, 0.5) # 변환행렬
dst = cv2.warpAffine(image, M (width, height)) 

plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.show()