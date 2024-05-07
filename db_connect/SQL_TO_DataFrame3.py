import time
import pandas as pd
import numpy as np
import pymysql
import requests
from sqlalchemy import create_engine




conn = pymysql.connect(host="127.0.0.1", port=3306, user='root', passwd='1234', db='myboard', charset='utf8')
df = pd.read_sql(
    """
    SELECT addr1, addr2, addr3, latitude, longitude
    FROM coordinate
    WHERE latitude != ''
    ORDER BY addr1 ASC;
    """, conn)
df['region_code'] \
, df['region_1depth'] \
, df['region_2depth'] \
, df['region_3depth'] \
, df['region_4depth'] \
, df['addr1_new'] \
, df['addr2_new'] = None, None, None, None, None, None, None
print(repr(df))
print(repr(df.dtypes))
conn.close()



# response.content
# response.text
# response.json()
headers = {
    "Content-Type" : "text/plain",
    "Accept" : "application/json",
    "Authorization" : "KakaoAK ab7f142fe71f6a157e739be334f50ecc",
}

startIDX = 40000
endIDX = 40000 + 1030
for idx in range(startIDX, endIDX):
    # isinstance(df.iloc[0, [3,4]], pd.Series) # True
    lat, lng = df.iloc[idx, [3,4]]['latitude'], df.iloc[idx, [3,4]]['longitude']
    response1 = requests.get("https://dapi.kakao.com/v2/local/geo/coord2regioncode.json?x={lng}&y={lat}".format(lat = lat, lng = lng), headers=headers)
    response2 = requests.get("https://dapi.kakao.com/v2/local/geo/coord2address.json?x={lng}&y={lat}&input_coord=WGS84".format(lat = lat, lng = lng), headers=headers)
    time.sleep(0.08)
    # response1.content
    # response1.text
    
    insertRow = {
        'region_code'   : response1.json()['documents'][0]['code'],
        'region_1depth' : response1.json()['documents'][0]['region_1depth_name'],
        'region_2depth' : response1.json()['documents'][0]['region_2depth_name'],
        'region_3depth' : response1.json()['documents'][0]['region_3depth_name'],
        'region_4depth' : response1.json()['documents'][0]['region_4depth_name'],
        'addr1_new' : response2.json()['documents'][0]['address']['address_name'], # 지번주소
        'addr2_new' : response2.json()['documents'][0]['road_address']['address_name'] if response2.json()['documents'][0]['road_address'] != None else '', # 도로명주소
    }
    print(idx, insertRow)
    
    df.loc[idx, ['region_code','region_1depth','region_2depth','region_3depth','region_4depth','addr1_new','addr2_new']] = insertRow  # DataFrame의 일부분을 딕셔너리의 값으로 대체
    pass


# 커넥션 연결
engine = create_engine("mariadb+pymysql://root:1234@localhost:3306/myboard")
# 기존에 만들어 놓은 테이블에 INSERT
df[startIDX:endIDX][['latitude', 'longitude', 'region_code', 'region_1depth', 'region_2depth', 'region_3depth', 'region_4depth', 'addr1_new', 'addr2_new']].to_sql('temp_currency_selling', engine, if_exists='append', index=False)


