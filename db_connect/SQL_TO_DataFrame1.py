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

# conn = pymysql.connect('localhost', 'root', '1234', 'myboard')
# cur = conn.cursor()
# cur.execute('SELECT * FROM email_send_log;')
# result = cur.fetchall()
# conn.close()


conn = pymysql.connect(host="127.0.0.1", port=3306, user='root', passwd='1234', db='myboard', charset='utf8')
df = pd.read_sql(
    """
    SELECT * FROM addr_only_p8;
    """, conn)
df['latitude'], df['longitude'] = None, None
print(repr(df))
print(repr(df.dtypes))
conn.close()


# 크롬드라이버 실행
# driver = webdriver.Chrome(R'C:/webdriver/chromedriver-win64/chromedriver.exe')
# driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
chrome_options = webdriver.ChromeOptions()
# # headless 로 브라우저 안보이게 할 수 있음
# chrome_options.add_argument('--headless')
# 브라우저 꺼짐 방지 옵션
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
driver.implicitly_wait(2)
driver.get("https://deveapp.com/map.php")

startIDX = 0
endIDX = 0

for a1, a2, idx in zip(df.loc[startIDX:endIDX, 'addr1'], df.loc[startIDX:endIDX, 'addr2'], range(startIDX,endIDX)):
    e1 = driver.find_element(By.CSS_SELECTOR, 'input[id="search_area"][class="form-control wd50"]')
    e1.clear()
    a1 = ' '.join(a1.replace('  ', ' ').split(' ')[-2:]) # 공백2개짜리 제거, 'XX시 XX동' 또는 'XX면 XX리' 만 사용
    e1.send_keys(a1+' '+a2)
    e2 = driver.find_element(By.CSS_SELECTOR, 'button[id="search_address"]')
    
    lat = driver.find_element(By.ID, 'lat')
    lng = driver.find_element(By.ID, 'lng')
    lat.clear()
    lng.clear()
    e2.click()
    
    try:
        element = WebDriverWait(driver, 3).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '#map > div:nth-child(1) > div > div:nth-child(6) > div, #centerAddr, input#lat, input#lng')))
    except Exception:
        driver.quit()
        pass
    finally:
        time.sleep(0.5) # 그냥 무조건 기다리자...
    
    lat_v = lat.get_dom_attribute('value') if lat.get_attribute('value') == '' else lat.get_attribute('value')
    lng_v = lng.get_dom_attribute('value') if lng.get_attribute('value') == '' else lng.get_attribute('value')
    print('lat_v: {lat_v}, lng_v: {lng_v}, idx: {idx}'.format(lat_v = lat_v, lng_v = lng_v, idx = idx))
    df.iloc[idx,-2], df.iloc[idx, -1] = lat_v, lng_v
    pass

driver.quit()
# 타입변환
# df = df.astype({'latitude':'float64','longitude':'float64'})
print(df.iloc[startIDX:endIDX, :])

# 커넥션 연결
engine = create_engine("mariadb+pymysql://root:1234@localhost:3306/myboard")
# 기존에 만들어 놓은 테이블에 INSERT
df.iloc[startIDX:endIDX, :].to_sql('coordinate', engine, if_exists='append', index=False)

