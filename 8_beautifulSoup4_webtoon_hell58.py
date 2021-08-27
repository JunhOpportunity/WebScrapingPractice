import requests
from bs4 import BeautifulSoup

# 네이버 웹툰에서 정보 가져오기.
url = "https://comic.naver.com/webtoon/list?titleId=719508"
res = requests.get(url)     
res.raise_for_status()      # 응답코드 오류 -> 실행 종료

soup = BeautifulSoup(res.text, "lxml")

# 웹툰 첫 페이지의 제목들 출력하기
cartoonsTitleList = soup.find_all("td", attrs={"class":"title"})
# for title in cartoonsTitleList:
#     print(title.a.get_text())
# cartoonTitle = cartoonsTitleList[0].a.get_text()

# 링크도 첨부해서 같이 출력하기
cartoonTitle = cartoonsTitleList[0].a.get_text()
cartoonLink = cartoonsTitleList[0].a["href"]   # ※주의) 링크 반환은 이렇게 한다.

print(cartoonTitle + " , " + "https://comic.naver.com" +cartoonLink)  # cartoonLink가 전체 링크가 아니라 /webtoon/detail?titleId=719508&no=141&weekday=tue 이렇게 나오기 때문에 완전한 주소로 만들기 위해서 앞에 빠진 내용을 추가

# List를 이용해 첫번째 페이지에 있는 웹툰의 제목과 링크 출력하기
for cartoon in cartoonsTitleList:
    title = cartoon.a.get_text()
    link = "https://comic.naver.com" + cartoon.a["href"]
    print(title, link)

# 웹툰 평점 구하기
total_rates = 0
average_rate = 0
count = 0

cartoons = soup.find_all("div", attrs={"class":"rating_type"})
for cartoon in cartoons:
    rate = cartoon.find("strong").get_text()    # find() 이 내용 이해 안간다
    total_rates += float(rate)
    count += 1

average_rate = total_rates / count
print(average_rate)