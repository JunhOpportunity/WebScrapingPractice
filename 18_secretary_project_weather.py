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
# ★★★★★★★★★여기 아랫부분 인덱스로 처리하는거 이해 안감.★★★★★★★★★★★★★★★
fine_dust = soup.find("dl", attrs={"class":"indicator"})   # 미세먼지 농도와 상태
dust_pm10 = fine_dust.find_all("dd")[0].get_text()
dust_pm25 = fine_dust.find_all("dd")[1].get_text()
print("-" * 30)
print("오늘의 날씨")
print(weather_inform)
print(f"현재 온도는 {temperature}º 이고, 체감 온도는 {sensible_temperature}º입니다")
print(f"마지막으로 미세먼지 농도는 {dust_pm10}, 초미세먼지 농도는 {dust_pm25}입니다")
print("-" * 30)