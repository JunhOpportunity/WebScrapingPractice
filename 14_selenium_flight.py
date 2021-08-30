from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 로딩 후 수행하게 해주는 함수들
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window()   # 창 최대화
url = "https://beta-flight.naver.com/"
browser.get(url) # url로 이동하기

# 가는 날 선택 클릭     <- ★★★★★★★★★★★★★이거 안됨.★★★★★★★★★★★★★★★★★★★★★
browser.find_element_by_link_text("가는 날").click()

# 이번달 31일 -> 31일 선택
# browser.find_element_by_link_text("31")[0].click()  # [0] = 이번달
# browser.find_element_by_link_text("31")[0].click()  # [0] = 이번달

# 이번달 31일 -> 다음달 15일 선택
browser.find_element_by_link_text("31")[0].click()  # [0] = 이번달
browser.find_element_by_link_text("15")[1].click()  # [1] = 다음달

# 제주도 선택
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[7]/div/ul/li[1]/button/figure/img").click()   # 여행지 선택 클릭

# 항공권 검색 클릭
browser.find_element_by_link_text("항공권 검색").click

# 브라우저를 최대 10초 동안 내가 검색하고자하는 엘리먼트가 나올 때 까지 대기
try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located(By.XPATH, "//*[@id='__next']/div/div[1]/div[5]/div/div[2]/div[2]/div/button"))
    # 성공했을 때 동작 수행
    print(elem.text)    # 첫 번째 결과 출력
finally:
    browser.quit()

# 첫 번째 결과 출력     # 로딩 시간이 있어서 검색 못 함.
elem = browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[5]/div/div[2]/div[2]/div/button")

# 


