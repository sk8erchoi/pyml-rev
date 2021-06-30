from selenium.webdriver import Firefox, FirefoxOptions

url = "http://www.naver.com/"

# Firefox를 헤드리스 모드로 설정하는 옵션 --- (※1)
options = FirefoxOptions()
options.add_argument('-headless')

# PhantomJS 드라이버 추출하기 --- (※2)
browser = Firefox(options=options)

# URL 읽어 들이기 --- (※3)
browser.get(url)
# 화면을 캡처해서 저장하기 --- (※4)
browser.save_screenshot("Website.png")
# 브라우저 종료하기 --- (※5)
browser.quit()
