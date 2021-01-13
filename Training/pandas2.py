import pandas as pd
import numpy as np 

# 데이터 프레임의 Null 여부 확인

word_dict = {
    'Apple' : '사과',
    'Banana' : '바나나',
    'Carrot' : '당근',
    'Durian' : '두리안'
}

frequency_dict = {
    'Apple' : 3,
    'Banana' : 5,
    'Carrot' : np.nan,
    'Durian' : 2
}

importance_dict = {
    'Apple' : 3,
    'Banana' : 2,
    'Carrot' : 1,
    'Durian' : 1
}

word = pd.Series(word_dict)
frequency = pd.Series(frequency_dict)
importance = pd.Series(importance_dict)

summary = pd.DataFrame({
    'word':word,
    'frequency' : frequency,
    'importance' : importance
})

print(summary)

summary = summary.sort_values('frequency', ascending=False) # 데이터 프레임 정렬 함수
print(summary)

print(summary.notnull())
print(summary.isnull())
summary['frequency'] = summary['frequency'].fillna('데이터 없음')
print(summary)

# 시리즈 자료형의 연산

array1 = pd.Series([1, 2, 3], index = ['A', 'B', 'C'])
array2 = pd.Series([4, 5, 6], index = ['B', 'C', 'D'])

array = array1.add(array2, fill_value = 0)
print(array)

# 데이터 프레임 집계 함수

array1 = pd.DataFrame([[1, 2], [3, 4]], index = ['A','B'])
array2 = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], index = ['B', 'C', 'D'])

array = array1.add(array2, fill_value=0)
print(array)
print("컬럼 1의 합: ", array[1].sum())
print(array.sum())



