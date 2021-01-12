import pandas as pd;
array = pd.Series(['사과', '바나나', '당근'], index = ['a','b','c'])

print(array)
print(array['a'])

# Dict 자료형을 series로 바꾸기
data = {
    'a' : '사과',
    'b' : '바나나',
    'c' : '당근'
}

array = pd.Series(data)
print(array['a'])

# Data Frame -> 인덱스끼리 묶는다

word_dict = {
    'Apple' : '사과',
    'Banana' : '바나나',
    'Carrot' : '당근',
    'Durian' : '두리안'
}

frequency_dict = {
    'Apple' : 3,
    'Banana' : 5,
    'Carrot' : 7,
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

# 이름(Name) : 값(Values)
summary = pd.DataFrame({
    'word' : word,
    'frequency' : frequency,
    'importance' : importance
})

# 더하기
score = summary['frequency'] + summary['importance']
summary['score'] = score
print(summary)

# 이름을 기준으로 슬라이싱
print(summary.loc['Banana' : 'Carrot', 'importance':])

# 인덱스를 기준으로 슬라이싱
print(summary.iloc[1:3, 2:])

# DataFrame 변경과 삽입

summary.loc['Apple', 'importance'] = 5 # 데이터의 변경
summary.loc['Elderberry'] = ['엘더베리',5,2,7] # 새 데이터 삽입

print(summary)