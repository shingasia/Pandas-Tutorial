import time
import pandas as pd
import numpy as np
import pymysql
from sqlalchemy import create_engine
import random



conn = pymysql.connect(host="127.0.0.1", port=3306, user='root', passwd='1234', db='myboard', charset='utf8')
df = pd.read_sql(
    """
    SELECT
        '테스트데이터'    AS title
	    , 'JPY'          AS money_code1
	    , 20000          AS amount1
	    , 'KRW'          AS money_code2
	    , 190000         AS amount2
        , latitude, longitude, region_code
        , region_1depth, region_2depth, region_3depth, region_4depth, addr1_new, addr2_new
        , '테스트데이터'  AS memo
	    , 'ADMIN'        AS writer
	    , NULL           AS write_date
	    , NULL           AS updater
	    , NULL           AS update_date
	    , 0              AS sold_yn
    FROM temp_currency_selling;
    """, conn)

print(repr(df))
print(repr(df.dtypes))
conn.close()

df.query('write_date.isna()').sample(4500, replace=False, axis=0)['write_date'] = '2016-01-01 12:12:12.000000'
df.query('write_date.isna()').apply(axis=0)

def my_random_choice(x):
    return random.choice([
     '2016-01-01 12:12:12.000000',
     '2017-01-01 12:12:12.000000',
     '2018-01-01 12:12:12.000000',
     '2019-01-01 12:12:12.000000',
     '2020-01-01 12:12:12.000000',
     '2021-01-01 12:12:12.000000',
     '2022-01-01 12:12:12.000000',
     '2023-01-01 12:12:12.000000',
     '2024-01-01 12:12:12.000000',])
    pass

df['write_date'] = df.apply(lambda x : my_random_choice(x), axis = 1)


# 커넥션 연결
engine = create_engine("mariadb+pymysql://root:1234@localhost:3306/myboard")
# 기존에 만들어 놓은 테이블에 INSERT
df.to_sql('temp_currency_selling2', engine, if_exists='append', index=False)

