import requests
from bs4 import BeautifulSoup

url = "https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=732"
pre_url = "https://news.naver.com/"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")
security_news_list = soup.find("ul",attrs={"class":"type06_headline"}).find_all("li", limit=3)  # 3개 까지만 가져오기

for index, news in enumerate(security_news_list):
    title = news.find("a").get_text().strip()
    link = pre_url + news.find("a")["href"]
    print(f"{index + 1} {title} {link}")

