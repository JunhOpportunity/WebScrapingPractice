from selenium import webdriver
browser = webdriver.Chrome()        # chromedriver.exe가 현재 폴더에 있다면 괄호 비워도 가능 / chromedriver.exe가 현재 폴더에 없다면 경로 적어주어야 함.

# 네이버에서 활용을 통한 기본 개념 공부
browser.get("http://naver.com")
# elem = browser.find_element_by_class_name("list_login")   # 원래 이 코드였는데, 이 코드대로 한 후 바로 from selenium.webdriver.common.keys import Keys 후 elem.send_keys("") 하면 당연히 오류뜬다.
elem = browser.find_element_by_id("")  # 이걸로 elem을 바꿔주어야 가능하다.
elem.click()        # 버튼 클릭
from selenium.webdriver.common.keys import Keys
elem.send_keys("네이버 검색")           # 검색창에 원하는 내용 입력
elem.send_keys(Keys.ENTER)             # 검색!

elem = browser.find_element_by_tag_name("a")    # a 태그를 가진 첫 번째 엘리먼트만 가져옴
elem

elem = browser.find_elements_by_tag_name("a")   # a 태그를 가진 모든 엘리먼트를 가져옴 (elements)
elem

for e in elem:
    e.get_attribute("href")     # 태그 빼고 텍스트만 가져오기

