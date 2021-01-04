import numpy as np

# numpy 배열 가로 축으로 합치기
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
array3 = np.concatenate([array1, array2])

print(array3.shape)
print(array3)

# numpy 배열 세로 축으로 합치기
array1 = np.arange(4).reshape(1, 4) # 1차원
array2 = np.arange(8).reshape(2, 4) # 2차원

print(array1)
print(array2)

array3 = np.concatenate([array1, array2], axis = 0)
# axis = 0을 넣으면 아래쪽으로 추가가 된다.
print(array3)

# numpy 배열 형태 바꾸기
array1 = np.array([1,2,3,4])
array2 = array1.reshape(2, 2)

print(array2)

# numpy 배열 나누기
array = np.arange(8).reshape(2,4)
left, right = np.split(array, [2], axis = 1) # 반으로 갈라짐
print(left.shape)
print(right.shape)
print(array)
print(left)


