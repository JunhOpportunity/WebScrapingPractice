from selenium import webdriver

# 크롬 브라우저를 띄우지 않고 내부적으로만 실행하게 하기
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")

browser = webdriver.Chrome(options=options)
browser.maximize_window()       # 전체화면으로 열기

# 크롬 브라우저에서 페이지 이동
url = "https://play.google.com/store/movies/top"
browser.get(url)

# 스크롤 내리기
# 모니터 높이만큼을 스크롤 내리기
# browser.execute_script("window.scrollTo(0, 1080)")     # 바탕화면 크기에서 1920 x 1080 에서 1080

# 화면 가장 아래로 스크롤 내리기
browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

import time
interval = 2    # 2초에 한번씩 아래로 스크롤 하기 위해 생성한 변수

# 현재 문서 높이 측정 후 저장
document_height = browser.execute_script("return document.body.scrollHeight")

# 반복 수행
while True:
    # 스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")    # 이거 return document.body.scrollHeight 로 해서 안된거였다

    # 페이지 로딩 대기
    time.sleep(interval)    # 만약 로딩시간이 내가 정해둔 변수인 interveal = 2 초보다 길다면 더 길게 설정하면 된다.

    # 현재 문서 높이를 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == document_height:  # 더 이상 스크롤 X -> 끝냄
        break

    # 더 스크롤 될 경우 (= 아직 최대 높이가 아닌 경우)
    document_height = curr_height

print("스크롤 완료")
browser.get_screenshot_as_file("google_movie.png")  # 백그라운드로 진행중인 것을 캡쳐 후 png 파일로 저장

# 리스트 다시 가져오면 이제 랭킹 모두 가져올 수 있다. 스크롤 모두 맨 아래로 내렸기 때문에
import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source, "lxml")

movies = soup.find_all("div", attrs={"class":"Vpfmgd"})
print(len(movies))

for movie in movies:
    
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    

    # 가격까지 포함해서 출력하기
    price = movie.find("span", attrs={"class":"VfPpfd ZdBevf i5DZme"}).get_text()
   
    print(f"{title} 가격:{price}")
   
