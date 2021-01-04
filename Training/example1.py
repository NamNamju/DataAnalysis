import numpy as np
# 일반적으로 numpy는 np로 줄여서 사용한다.

list_data = [1, 2, 3]
array = np.array(list_data) # 특정한 리스트 데이터를 numpy 자료형으로 바꾸어준다.

# 제공되는 몇 가지 함수
print(array.size)
print(array.dtype)
print(array[2])

# 0부터 3까지의 배열 만들기
array1 = np.arange(4)
print(array1)

array2 = np.zeros((4,4), dtype = float) # 4 X 4 크기의 0으로 초기화 된 2차원 배열에, 타입은 실수형
print(array2)

# 0부터 9까지 랜덤하게 초기화 된 배열 만들기
array4 = np.random.randint(0, 10, (3, 3)) # 3 X 3 크기의 0부터 9까지의 랜덤한 수
print(array4)

# 평균이 0이고, 표준편차가 1인 표준 정규를 띄는 배열
array5 = np.random.normal(0, 1, (3, 3))

