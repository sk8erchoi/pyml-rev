# 네이버 로그인 절차가 강화되어 자동입력 방지문자(Captcha)를 입력해야 로그인할 수 있습니다.
# 따라서 파이썬 셸이나 주피터 노트북(5-3절에서 설명)에서 비밀번호 입력까지만 실행하고
# 자동입력 방지문자는 브라우저 창에서 수작업으로 입력 후 나머지 코드를 이어서 실행하시기 바랍니다.

# Step 1

from selenium.webdriver import Firefox, FirefoxOptions

USER = "<아이디>"
PASS = "<비밀번호>"

# Firefox 실행하기 --- (※1)
options = FirefoxOptions()
#options.add_argument('-headless')
browser = Firefox(options=options)

# 로그인 페이지에 접근하기 --- (※2)
url_login = "https://nid.naver.com/nidlogin.login"
browser.get(url_login)
print("로그인 페이지에 접근합니다.")

# 텍스트 박스에 아이디와 비밀번호 입력하기 --- (※3)
e = browser.find_element_by_id("id")
e.clear()
e.send_keys(USER)
e = browser.find_element_by_id("pw")
e.clear()
e.send_keys(PASS)

########################################################
# Step 2
# 브라우저 창에서 자동입력 방지문자를 입력해주세요.


########################################################
# Step 3

# 입력 양식 전송해서 로그인하기 --- (※4)
form = browser.find_element_by_css_selector("input.btn_global[type=submit]")
form.submit()
print("로그인 버튼을 클릭합니다.")

# 쇼핑 페이지의 데이터 가져오기 --- (※5)
browser.get("https://order.pay.naver.com/home?tabMenu=SHOPPING")

# 쇼핑 목록 출력하기 --- (※6)
products = browser.find_elements_by_css_selector(".name")
print(products)
for product in products:
  print("-", product.text)
