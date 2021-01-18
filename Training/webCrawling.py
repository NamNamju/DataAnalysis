import requests
from bs4 import BeautifulSoup

# HTML 문서 불러오기

# 특정 URL에 접속하는 요청(Request) 객체를 생성한다.
request = requests.get("http://www.dowellcomputer.com/main.jsp")

# 접속한 이후의 웹 사이트 소스코드를 추출합니다.
html = request.text.strip() # strip 함수로 공백에 제거된 내용을 추출.

# HTML 소스코드를 파이썬 BeautifulSoup 객체로 변환합니다.
soup = BeautifulSoup(html, "html.parser")

# <a> 태그를 포함하는 요소를 추출한다.
links = soup.select('td > a') # a 태그는 보통 링크 정보를 포함한다.

# 모든 링크에 접근
for link in links:
    # 링크고 href 속성을 가지고 있으면
    if link.has_attr('href'):
        # href 속성의 값으로 'notice'라는 문자 포함 -> 공지
        if link.get('href').find('notice') != -1:
            print(link.text)



