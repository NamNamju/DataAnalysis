import cv2

img_basic = cv2.imread('cat.jpg',cv2.IMREAD_COLOR) # 이미지 읽기
cv2.imshow('Image Basic', img_basic) # 이미지를 화면에 출력
cv2.waitKey(0) # 키보드 입력을 처리한다.
cv2.imwrite('result1.png',img_basic) # 특정한 이미지 파일로 저장한다.

cv2.destroyAllWindows() # 이미지 창을 닫는다.

img_gray = cv2.cvtColor(img_basic, cv2.COLOR_BGR2) # BGR컬러 -> Grayscale로 변환
cv2.imshow('Image Basic', img_gray)
cv2.waitKey(0)
cv2.imwrite('result1.png',img_gray)

# matplotlib를 이용하면 손쉽게 이미지 출력 가능.
# matplotlib는 RGB를 기준으로 하기 때문에, cv2.imread로 읽어주면 이것을 COLOR_BGR2RGB로 바꾸어주어야한다.
# COLOR -> BGR2RGB
# BGR2GRAY -> GRAY2RGB
