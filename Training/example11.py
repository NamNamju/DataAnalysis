import cv2
import numpy as np
import matplotlib.pyplot as plt

# 도형그리기

# 1. 직선
image = np.full((512, 512, 3), 255, np.uint8)
image = cv2.line(image, (0,0), (255,255), (255,0,0),3)

plt.imshow(image)
plt.show()

# 2. 사각형
image = np.full((512, 512, 3), 255, np.uint8)
image = cv2.rectangle(image, (20, 20), (255,255), (255, 0, 0), 3)

plt.imshow(image)
plt.show()

# 3. 원
image = np.full((512, 512, 3), 255, np.uint8)
image = cv2.circle(image, (255,255), 30, (255, 0, 0), 3)

plt.imshow(image)
plt.show()

# 4. 다각형
image = np.full((512, 512, 3), 255, np.uint8)
points = np.array([[5, 5], [128, 258], [483, 444], [400, 150]])
image = cv2.polylines(image, [points], True, (0, 0, 255), 4)

plt.imshow(image)
plt.show()

# 5. 텍스트
image = np.full((512, 512, 3), 255, np.uint8)
image = cv2.putText(image, 'Hello World', (0, 200), cv2.FONT_ITALIC, 2, (255, 0, 0))

plt.imshow(image)
plt.show()