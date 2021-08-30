from selenium import webdriver
browser = webdriver.Chrome()

# 다음 사이트를 활용한 selenium practice
browser.get("https://www.daum.net")

elem = browser.find_element_by_id("q")
elem

from selenium.webdriver.common.keys import Keys
elem.send_keys("네이버웹툰")
elem = browser.find_element_by_xpath("//*[@id='daumSearch']/fieldset/div/div/button[2]")    # 돋보기 버튼의 xpath 복사 후 붙여넣기
elem.click()    # 돋보기 버튼은 클릭해야 작동하므로 .click 함