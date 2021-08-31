# Headless solution 
from selenium import webdriver

# 크롬 브라우저를 띄우지 않고 내부적으로만 실행하게 하기
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")

# 중요) Headless 문제점의 해결책
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36")

browser = webdriver.Chrome(options=options)
browser.maximize_window()

# user agent string 사이트 들어가서 headless의 문제점 파악하기
url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser.get(url)

# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36
user_agent = browser.find_element_by_id("detected_value")
print(user_agent.text)
browser.quit()

# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/92.0.4515.159 Safari/537.36
# 나의 user agent string 과 다른 Headless 가 추가된 user agent가 출력된다. 따라서 사이트에서 Headless가 붙어있는 사용자를 차단할 수 있으므로 해결책을 마련해야한다.
