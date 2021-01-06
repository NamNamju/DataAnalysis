import numpy as np

# 단일 객체 및 저장 불러오기
array = np.arange(0,10)
np.save('saved.npy', array) # 해당 파일을 저장하면 텍스트 파일로 저장. 내용을 쉽게 파악하기는 어렵다.

result = np.load('saved.npy')
print(result)

# 복수 객체 저장 및 불러오기
array1 = np.arange(0, 10)
array2 = np.arange(10, 20)
np.savez('saved.npz', array1 = array1, array2 = array2)

data = np.load('saved.npz')
result1 = data['array1']
result2 = data['array2']
print(result1)
print(result2)
