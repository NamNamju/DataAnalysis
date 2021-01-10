import cv2

image = cv2.imread('cat.jpg')

# 픽셀 수 및 이미지 크기 확인
print(image.shape)
print(image.size)

px = image[100,100]

# 특정 범위 픽셀 변경

# 1. 하나하나의 픽셀에 접근하여 바꾸기
for i in range(0, 100):
    for j in range(0, 100):
        image[i, j] = [255,255,255]

# 2. slicing
roi = image[200:350, 50:200]

image[0:150, 0:150] = roi

# 픽셀별로 섹상 다루기
image[:,:,2] = 0 # 빨간색 색상이 0이 된다.