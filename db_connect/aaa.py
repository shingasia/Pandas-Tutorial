import time
import numpy as np
import pandas as pd
# import mariadb
import pymysql
# pymysql.install_as_MySQLdb
from sqlalchemy import create_engine

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException



# 크롬드라이버 실행
# driver = webdriver.Chrome(R'C:/webdriver/chromedriver-win64/chromedriver.exe')
# driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
my_user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
chrome_options = webdriver.ChromeOptions()
# headless 로 브라우저 안보이게 할 수 있음
chrome_options.add_argument('--headless')
chrome_options.add_argument(F'--user-agent={my_user_agent}')
# 브라우저 꺼짐 방지 옵션
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
driver.implicitly_wait(2)
driver.get("https://deveapp.com/map.php")
print(repr(driver.get_cookies()))
driver_UA = driver.execute_script("return navigator.userAgent")
print(F'driver_UA : {driver_UA}')

driver.quit()

# 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/122.0.6261.112 Safari/537.36'
# 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'