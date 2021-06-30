from selenium.webdriver import Firefox, FirefoxOptions

# Firefox 실행하기
options = FirefoxOptions()
options.add_argument('-headless')
browser = Firefox(options=options)

# 적당한 웹 페이지 열기
browser.get("https://google.com")

# 자바스크립트 실행하기
r = browser.execute_script("return 100 + 50")
print(r)
