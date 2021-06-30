import scrapy
# Selenium 미들웨어 읽어 들이기
from ..selenium_middleware import *

# 쿠팡 이메일과 비밀번호 지정하기 --- (※1)
USER = "쿠팡 이메일을 입력해주세요"
PASSWORD = "쿠팡 비밀번호를 입력해주세요"

class CoupangSpider(scrapy.Spider):
  name = 'coupang1'
  # 미들웨어 등록하기 --- (※2)
  custom_settings = {
    "DOWNLOADER_MIDDLEWARES": {
      "coupang.selenium_middleware.SeleniumMiddleware": 0
    }
  }

  # 요청 전에 로그인하기 --- (※3)
  def start_requests(self):
    # 로그인 페이지로 이동 후 로그인
    selenium_get("https://login.coupang.com/login/login.pang")
    email = get_dom('._loginForm [name=email]')
    email.send_keys(USER)
    password = get_dom('._loginForm [name=password]')
    password.send_keys(PASSWORD)
    button = get_dom("._loginForm button[type=submit]")
    button.click()

    # 마이 페이지로 이동
    a = get_dom('#myCoupang > a')
    mypage = a.get_attribute('href')
    yield scrapy.Request(mypage, self.parse)
  
  def parse(self, response):
    # 원하는 정보 추출하기 --- (※4)
    items = response.css('.my-order-unit__item-info')
    for item in items:
      title = item.css(".my-order-unit__info-name strong:last-child::text").extract_first().strip()
      info = item.css(".my-order-unit__info-ea::text").extract_first().split("/")[0].strip()
      yield {
        "title": title,
        "info": info
      }
