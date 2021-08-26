import requests
from bs4 import BeautifulSoup

# 네이버 웹툰에서 정보 가져오기.
url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)     
res.raise_for_status()      # 응답코드 오류 -> 실행 종료

soup = BeautifulSoup(res.text, "lxml")

# 네이버 웹툰 전체 목록 가져오기
cartoons = soup.find_all("a", attrs={"class":"title"})
for cartoon in cartoons:    # 네이버 웹툰 전체 목록 출력하는 반복문
    print(cartoon.get_text())