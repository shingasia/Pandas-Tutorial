import numpy as np
import pandas as pd
import mariadb
import pymysql
pymysql.install_as_MySQLdb
from sqlalchemy import create_engine


print(np.random.randint(-3.5, 2.4, 15));
print(np.random.randn(2,3,4))
# print(np.random.)

employee = pd.DataFrame (
    data = {
        # "index_no" : 
        "id"   : map(lambda x : "아이디"+str(x), range(0, 300_0000)),
        "name" : map(lambda x : "이름"+str(x), range(0, 300_0000)),
        "age"  : np.random.randint(25, 35, 300_0000),
    },
    dtype = "object"
)
employee["department_code"] = np.random.choice(
    ["CS부서", "마케팅/기획부", "개발1팀", "개발2팀", "개발3팀", "회계/재무부", "인사/리크루트"]
    , 300_0000
    , p=[0.2, 0.1, 0.125, 0.125, 0.2, 0.15, 0.1]
)
employee["sdate"] = pd.date_range(
    start = "2011-01-21",
    end = "2021-06-10",
    periods= 300_0000
)
employee["edate"] = pd.date_range(
    start = "2015-01-21",
    end = "2025-12-10",
    periods= 300_0000
)
employee["marry_YN"] = np.random.choice(
    ["Y", "N"],
    300_0000,
)
employee["salary_kr"] = np.random.randint(210, 450, 300_0000) * 10000
employee["salary_usd"] = employee["salary_kr"] / 1314
employee['memo'] = '' # 빈문자열
print(employee["salary_usd"])
print(employee["memo"])
# 0
# 1
# 2
# 3
# 4
#           ..
# 2999995
# 2999996
# 2999997
# 2999998
# 2999999
# Name: memo, Length: 3000000, dtype: object
print(employee.dtypes)
# id                         object
# name                       object
# age                        object
# department_code            object
# sdate              datetime64[ns]
# edate              datetime64[ns]
# marry_YN                   object
# salary_kr                   int32
# salary_usd                float64
# memo                       object
# dtype: object



employee2 = pd.concat(
    [employee, employee, employee, employee],
    axis = 'index',
    ignore_index = True
)
print(employee2)
#                      id         name age       department_code                         sdate                         edate marry_YN   salary_kr      salary_usd    memo
# 0               아이디0        이름0  31         인사/리크루트 2011-01-21 00:00:00.000000000 2015-01-21 00:00:00.000000000        N    3970000      3021.308980
# 1               아이디1        이름1  30            개발3팀    2011-01-21 00:01:49.238436412 2015-01-21 00:01:54.508838169        Y    3810000      2899.543379
# 2               아이디2        이름2  31         인사/리크루트 2011-01-21 00:03:38.476872825 2015-01-21 00:03:49.017676339        N    4200000      3196.347032
# 4               아이디4        이름4  27            CS부서     2011-01-21 00:07:16.953745651 2015-01-21 00:07:38.035352678        Y    3170000      2412.480974
# 3               아이디3        이름3  33            CS부서     2011-01-21 00:05:27.715309238 2015-01-21 00:05:43.526514508        N    3580000      2724.505327
# ...              ...            ...   ..             ...                                 ...                           ...      ...        ...              ...     ...
# 11999995  아이디2999995  이름2999995  34            CS부서     2021-06-09 23:52:43.046254336 2025-12-09 23:52:21.964647296        N    3760000      2861.491629
# 11999996  아이디2999996  이름2999996  29          회계/재무부  2021-06-09 23:54:32.284690752 2025-12-09 23:54:16.473485440        Y    3630000      2762.557078
# 11999997  아이디2999997  이름2999997  27            CS부서     2021-06-09 23:56:21.523127168 2025-12-09 23:56:10.982323648        N    2260000      1719.939117
# 11999998  아이디2999998  이름2999998  27          회계/재무부  2021-06-09 23:58:10.761563584 2025-12-09 23:58:05.491161792        N    3920000      2983.257230
# 11999999  아이디2999999  이름2999999  29            개발3팀    2021-06-10 00:00:00.000000000 2025-12-10 00:00:00.000000000        N    3930000      2990.867580

# [12000000 rows x 10 columns]

""" 
    DB에 넣는 부분은 기존 테이블 모양을 바꾼다.. 
### 이제 DB 테이블에 INSERT
dbconn = mariadb.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "aza",
    port=3306,
)
# print("mysql+mysqldb://{user}:{pw}@localhost/{db}".format(user = 'root', pw = '1234', db = 'aza'))
engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}".format(user = 'root', pw = '1234', db = 'aza'))

employee2.to_sql(
    "employee",   # 테이블 이름(DataFrame 아님)
    engine,
    if_exists = 'replace',
    chunksize=1000,
    method='multi'
)
"""





