import time
import pandas as pd
import pymysql
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from sqlalchemy import create_engine

conn = pymysql.connect(host="127.0.0.1", port=3306, user='root', passwd='1234', db='myboard', charset='utf8')
df1 = pd.read_sql(
    """
    -- mainquery rows : 3656
    SELECT
    	 A.addr1    AS former_addr1
    	,A.addr2    AS former_addr2
    	,A.addr3    AS former_addr3
    	,B.addr4    AS former_addr4
    	,B.cnt_addr4
    	,A.addr1    AS posterior_addr1
    	,NULL       AS posterior_addr2
    	,A.addr3    AS posterior_addr3
    	,B.addr4    AS posterior_addr4
    FROM   coordinate AS A
    LEFT OUTER JOIN (
    	-- subquery rows : 44686
    	SELECT   addr1, addr2, addr3, COUNT(DISTINCT addr4) AS cnt_addr4, MIN(addr4) AS addr4
    	FROM     estate_sale
    	GROUP BY addr1, addr2, addr3
    	ORDER BY addr1, addr2, addr3
    ) AS B
    ON    A.addr1 = B.addr1
    AND   A.addr2 = B.addr2
    AND   A.addr3 = B.addr3
    WHERE A.latitude = '' OR A.longitude = ''
    ORDER BY A.addr1 ASC, A.addr2 ASC, A.addr3 ASC;
    """, conn)
print(repr(df1)) # NULL 값은  DataFrame에서 None으로 바뀐다.
print(repr(df1.dtypes))
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
driver.get("https://map.naver.com/p?c=15.00,0,0,0,dh")

# 결과를 저장할 DataFrame
df2 = pd.DataFrame(
    {
        "former_addr1" : [],
        "former_addr2" : [],
        "former_addr3" : [],
        "former_addr4" : [],
        "posterior_addr1" : [],
        "posterior_addr2" : [],
        "posterior_addr3" : [],
        "posterior_addr4" : [],
    },
)

df2['former_addr1'] = df2['former_addr1'].astype(str)
df2['former_addr2'] = df2['former_addr2'].astype(str)
df2['former_addr3'] = df2['former_addr3'].astype(str)
df2['former_addr4'] = df2['former_addr4'].astype(str)
df2['posterior_addr1'] = df2['posterior_addr1'].astype(str)
df2['posterior_addr2'] = df2['posterior_addr2'].astype(str)
df2['posterior_addr3'] = df2['posterior_addr3'].astype(str)
df2['posterior_addr4'] = df2['posterior_addr4'].astype(str)


search_box = driver.find_element(By.CSS_SELECTOR, 'div.search_box > div.input_box > input.input_search')
startIDX = 3000
endIDX = 3000 + 656 # len(df1)

for idx in range(startIDX, endIDX):
    time.sleep(0.7)
    row = dict(df1.iloc[idx])
    # print(isinstance({**row}, dict)) True,  **(Unpack operator)
    
    search_box.clear()
    search_box.send_keys(row['former_addr4'] + Keys.ENTER)
    # driver.execute_script(R"document.querySelector('div.search_box > div.input_box > input.input_search').setAttribute('value', '')")
    
    time.sleep(1.5)
    addr_list = driver.find_elements(By.CSS_SELECTOR, 'ul.address_list > li > span:nth-child(2)')
    addr_list = list(map(lambda x : x.text, addr_list))
    
    print('addr_list: {addr_list}, idx: {idx}'.format(addr_list = addr_list, idx = idx))
    
    insertRow = {
        'former_addr1' : row['former_addr1'],
        'former_addr2' : row['former_addr2'],
        'former_addr3' : row['former_addr3'],
        'former_addr4' : row['former_addr4'],
        'posterior_addr1' : row['posterior_addr1'],
        'posterior_addr2' : addr_list[0].split(' ')[-1] if len(addr_list) >= 2 else None,
        'posterior_addr3' : row['posterior_addr3'],
        'posterior_addr4' : row['posterior_addr4'],
    }
    # DataFrame 행추가
    # 방법1) df2.loc[len(df2)] = new_row
    # 방법2) pd.concat([df2, pd.DataFrame(new_row)], axis=0, ignore_index=True)
    # DataFrame 행삭제
    # df2.drop([0], axis=0, inplace=True)
    df2 = pd.concat([df2, pd.DataFrame(insertRow, index=[0])], axis=0, ignore_index=True)
    driver.back()
    pass

print(df2)
driver.quit()

# 커넥션 연결
engine = create_engine("mariadb+pymysql://root:1234@localhost:3306/myboard")
# 기존에 만들어 놓은 테이블에 INSERT
df2.to_sql('addr_change_log', engine, if_exists='append', index=False)

