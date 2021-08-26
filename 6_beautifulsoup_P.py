import requests
from bs4 import BeautifulSoup

# 네이버 웹툰에서 정보 가져오기.
url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)     
res.raise_for_status()      # 응답코드 오류 -> 실행 종료

soup = BeautifulSoup(res.text, "lxml")     # 가져온 html문서를 lxml을 통해서 Beautifulsoup 객체로 만든 것

print(soup.title)               # title 전체 출력 (태그까지)
print(soup.title.get_text())    # 글자만 출력
print(soup.a)                   # soup 객체에서 처음 발견되는 a element 출력
print(soup.a.attrs)             # a element의 속성 정보를 출력
print(soup.a["href"])           # a element의 href 속성 정보를 출력

# soup.find("a", attrs={"class":"Nbtn_upload"})   # a태그 안에 있는 것들 중 class가 Nbtn_upload 인 것을 찾기

# practice - 네이버 웹툰 사이트에서 랭크 1위 웹툰 링크 가져와서 이름 출력하기
naverWTU = "https://comic.naver.com/webtoon/weekday"
resS = requests.get(naverWTU)
resS.raise_for_status()
bSoup = BeautifulSoup(resS.text, "lxml")
rank1 = bSoup.find("li", attrs={"class":"rank01"})
print(rank1.a.get_text)

# 부모-자식 관계로 다음 정보 가져오기
rank2 = rank1.next_sibling.next_sibling     # 원래 next_sibling을 한 번만 하는 경우도 있지만, 그랬을 경우 아무것도 출력되지 않는다면 두 번 이상 해보면 된다.
rank3 = rank2.next_sibling.next_sibling
print(rank3.a.get_text)

# 부모-자식 관계로 이전 정보 가져오기
rank2 = rank3.previous_sibling.previous_sibling
rank1 = rank2.previous_sibling.previous_sibling

# 두 번 이상 쓰는 것을 분별하기 힘들거나 귀찮을 때 사용하는 방법
rank2 = rank1.find_next_sibling("li")
rank3 = rank2.find_next_sibling("li")
rank2 = rank3.find_previous_sibling("li")
rank1 = rank2.find_previous_sibling("li")

# ++) var_find_next|previous_siblings 를 입력하면, var 다음의 모든 형제관계의 내용들을 반환한다.
