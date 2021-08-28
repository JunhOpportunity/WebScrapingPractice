from sre_constants import AT
import requests
import re
from bs4 import BeautifulSoup, BeautifulSoup

# 쿠팡에서 '노트북' 제품들의 정보 가져오기

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}

for i in range(1, 6):
    print("페이지 :", i)
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=auto&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=&backgroundColor=".format(i)


    res = requests.get(url, headers=headers)    # 이걸 해줘야 사용자 입장에서 접속하는 것으로 보이게 할 수 있다고 나는 그렇게 이해함
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    items = soup.find_all("li", attrs={"class":re.compile("^search-product")})  # li 태그에서 클래스가 search-product로 시작하는 모든 엘리먼트들 가져옴

    for item in items:
        name = item.find("div", attrs={"class":"name"}).get_text()
        
        # +) 광고로 올려진 '노트북' 제품들의 정보는 제외하고 가져오기
        ad_badge = item.find("span", attrs={"class":"ad-badge"})
        if ad_badge:
            print("<광고 제외>")
            continue
        
        discount_price = item.find("strong", attrs={"class":"price-value"}).get_text()
        print(name, discount_price)     # if else를 코멘트 처리하고 이것만 실행하면, 모두 잘 출력된다. 도대체 어디서 문제인걸까?

