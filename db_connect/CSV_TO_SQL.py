import numpy as np
import pandas as pd
# import mariadb
import pymysql
# pymysql.install_as_MySQLdb
from sqlalchemy import create_engine


# conn = pymysql.connect('localhost', 'root', '1234', 'myboard')
# cur = conn.cursor()
# cur.execute('SELECT * FROM email_send_log;')
# result = cur.fetchall()
# conn.close()


# engine = create_engine("mariadb+pymysql://user:pass@some_mariadb/dbname?charset=utf8mb4")
engine = create_engine("mariadb+pymysql://root:1234@localhost:3306/myboard")
# data = pd.read_csv('C:/Users/skdsk/Downloads/a_202206.csv', encoding='CP949')
data = pd.read_excel('C:/Users/skdsk/Downloads/a_202312.xlsx')


# 칼럼이름 변경
data.columns = ['addr1','addr2','addr3','extent','contract_year','contract_day','amount','construction_year','addr4',]
print(repr(data.shape))
# 공백, 콤마 제거
data.loc[:, 'amount'] = data.loc[:, 'amount'].map(lambda x : x.strip().replace(',',''))

# 테이블에 INSERT
data.to_sql('estate_sale', engine, if_exists='append', index=False)
"""
addr1              VARCHAR(255)   COMMENT '시군구',
addr2              VARCHAR(10)    COMMENT '번지',
addr3              VARCHAR(255)   COMMENT '단지명',
extent             DECIMAL(10,5)  COMMENT '전용면적',
contract_year      INT            COMMENT '계약년월',
contract_day       VARCHAR(5)     COMMENT '계약일',
amount             INT            COMMENT '거래금액',
construction_year  VARCHAR(10)    COMMENT '건축년도',
addr4              VARCHAR(255)   COMMENT '도로명'
"""

# 2022-07 부터 xlsx로 다운받아 업로드 함

