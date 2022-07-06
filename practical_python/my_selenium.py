from selenium import webdriver

driver = webdriver.Chrome("./driver/chromedriver.exe")
url = "https://finance.naver.com/"
driver.get(url)

driver.implicitly_wait(3)
driver.implicitly_wait(3)
driver.get_screenshot_as_file("financial_main.png")