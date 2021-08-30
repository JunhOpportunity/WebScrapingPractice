from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get("http://naver.com")

# login 버튼 찾고 누르기
elem = browser.find_element_by_class_name("link_login")
elem.click()

# id & pw 입력하기
browser.find_element_by_id("id").send_keys("testid")    # 입력 하고 끝내는거니까 .send_keyts 를 통해 바로 입력 가능
browser.find_element_by_id("pw").send_keys("testpassward")

# login 버튼 클릭
elem = browser.find_element_by_class_name("btn_login").click()

# new id 입력
browser.find_element_by_id("id").send_keys("newid")     # 이거 하면 아까 썼던 testid 뒤에 붙어서 testidnewid 로 된다. 따라서 clear 해준 후 다시 적어야함
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("newid")