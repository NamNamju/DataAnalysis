# 이미지 픽셀끼리 더하기

import cv2
import matplotlib.pyplot as plt

image_1 = cv2.imread('image_1.jpg')
image_2 = cv2.imread('image_2.jpg')

result1 = cv2.add(image_1, image_2)
plt.imshow(cv2.cvtColor(result1, cv2.COLOR_BGR2RGB))
plt.show() # 좀 더 안정적으로 더해짐

result2 = image_1 + image_2
plt.imshow(cv2.cvtColor(result2, cv2.COLOR_BGR2RGB))
plt.show()