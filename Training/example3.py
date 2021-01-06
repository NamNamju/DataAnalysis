import numpy as np

array = np.random.randint(1, 10, size = 4).reshape(2,2)
print(array)

# 데이터에 곱셈
result_array = array * 10

# 서로 다른 형태의 Numpy 연산

array1 = np.arange(4).reshape(2, 2)
array2 = np.arange(2)

array3 = array1 + array2

print(array3)

# 브로드캐스트

array1= np.arange(0, 8).reshape(2, 4)
array2 = np.arange(0, 8).reshape(2, 4)
array3 = np.concatenate([array1, array2], axis = 0)
array4 = np.arange(0, 4).reshape(4, 1)

print(array3 + array4)

# 마스킹 연산

array1 = np.arange(16).reshape(4, 4)
print(array1)

array2 = array1 < 10
print(array2)

# 마스킹 연산 활용
array1[array2] = 100
print(array1)
# 10보다 작은 원소만 선택해서 100으로 바꿈

# 집계 함수
array = np.arange(16).reshape(4, 4)
print("최대값: ", np.max(array))
print("최솟값: ", np.min(array))
print("합계: ", np.sum(array))
print("평균값: ", np.min(array))

# 행이나 열에 대해서만 합계를 구할 수도 있다.
print("합계: ", np.sum(array, axis = 0)) # 열