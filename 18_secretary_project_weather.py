# 일산의 오늘 날씨 (날씨, )
# 네이버 뉴스에서 헤드라인 뉴스 3개와 링크
# 네이버 뉴스에서 IT뉴스에서 맨 위에 세개와 링크

import requests
from bs4 import BeautifulSoup

url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%9D%BC%EC%82%B0+%EB%82%A0%EC%94%A8&oquery=%E3%85%A3%E3%85%87%E3%84%B9%EC%82%B0+%EB%82%A0%EC%94%A8&tqi=hf9CEsp0JywssuMIxeGssssstNK-315709"
res = requests.get(url)     
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

weather_inform = soup.find("p",attrs={"class":"cast_txt"}).get_text()   # 날씨 요약
temperature = soup.find("span", attrs={"class":"todaytemp"}).get_text()     # 현재 온도
sensible_temperature = soup.find("span", attrs={"class":"sensible"}).find("span", attrs={"class":"num"}).get_text()     # 체감 온도
fine_dust = soup.find("dd", attrs={"class":"lv1"}).get_text()   # 미세먼지 농도와 상태

print("-" * 30)
print("오늘의 날씨")
print(weather_inform)
print(f"현재 온도는 {temperature}º 이고, 체감 온도는 {sensible_temperature}º입니다")
print(f"마지막으로 미세먼지 농도는 {fine_dust}입니다")
print("-" * 30)