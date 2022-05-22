import time
from selenium import webdriver

# 웹사이트 테스트
# 매번 로그인, 검색, 버튼 클릭 자동화, 데이터 수집, 웹 다방면 사용
# 잘안되네 -> 클릭, 스크롤, 키보드 입력
# 자동 로그인
# https://beomi.github.io/gb-crawling/posts/2017-02-27-HowToMakeWebCrawler-With-Selenium.html
# https://codens.info/1848
driver = webdriver.Chrome('data/chromedriver.exe')
driver.implicitly_wait(3)
driver.get('https://nid.naver.com/nidlogin.login')
driver.find_element_by_name('id').send_keys('naver_id')
driver.find_element_by_name('pw').send_keys('mypassword1234')