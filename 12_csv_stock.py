import csv          # 네이버 코스피 지수에서 csv 형태로 저장하기 위해서 csv import
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

filename = "시가총액1~200.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")    # ??? / 글씨 깨지면, utf-8-sig
writer = csv.writer(f)

title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실".split("\t")     # split는 뭐지? 찾아서 공부!
writer.writerow(title)

for page in range(1, 5):
    res = requests.get(url + str(page))     # page 1 ~ 4 까지 총 200개 가져오기
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")

        if len(columns) <= 1:   # 의미 없는 데이터는 skip (그냥 빈 줄들 / 잘 이해 X)
            continue
        data = [column.get_text() for column in columns]
        # print(data)
        writer.writerow(data)

