# 네이버 뉴스에서 헤드라인 뉴스 3개와 링크

import requests
from bs4 import BeautifulSoup

url = "https://news.naver.com"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

news_list = soup.find("ul", attrs={"class":"hdline_article_list"}).find_all("li")
for index, news in enumerate(news_list):
    title = news.find("a").get_text().strip()
    link = url + news.find("a")["href"]
    print("{}. {}".format(index+1, title))
    print("     (링크 : {}}".format(link))
print()
