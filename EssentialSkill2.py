import numpy as np
import pandas as pd
from tabulate import tabulate
# ==================================================================================================================================
# Pandas 객체에 함수 적용하기
# 사용자가 만든 함수나 또는 다른 라이브러리의 함수를 Pandas 객체에 적용하려면 아래의 방법들을 알고있어야 한다
# 함수가 DataFrame 또는 Series에 적용할지, 행 또는 열 단위로 적용할지, 또는 요소별로 적용할지에 따라 적절한 방법을 택하면 된다
# 1. Tablewise Function Application            : pipe()
# 2. Row or Column-wise Function Application   : apply()
# 3. Aggregation API                           : agg() and transform()
# 4. Applying Elementwise Functions            : applymap()
# ==================================================================================================================================


# ==================================================================================================================================
# DataFrame.apply(func, axis=0, raw=False, result_type=None, args=(), **kwargs)
# 행 또는 열 단위로 함수 적용
# 임의의 함수는 기술 통계 메서드와 마찬가지로 apply()메서드를 사용하여 특정 axis를 따라 적용할 수 있다.
# ==================================================================================================================================
df = pd.DataFrame(
    np.arange(-10, 10).reshape(4, 5)
)
df2 = df.copy()
print(df)
#     0  1  2  3  4
# 0 -10 -9 -8 -7 -6
# 1  -5 -4 -3 -2 -1
# 2   0  1  2  3  4
# 3   5  6  7  8  9
print(df2)
#     0  1  2  3  4
# 0 -10 -9 -8 -7 -6
# 1  -5 -4 -3 -2 -1
# 2   0  1  2  3  4
# 3   5  6  7  8  9

df.index=('R1', 'R2', 'R3', 'R4')
df.columns=('C1', 'C2', 'C3', 'C4', 'C5')
print(df)
#       C1  C2  C3  C4  C5
# R1 -10.0  -9  -8  -7  -6
# R2  -5.0  -4  -3  -2  -1
# R3   0.0   1   2   3   4
# R4   5.0   6   7   8   9
print(df.apply(np.mean))
# C1   -2.5
# C2   -1.5
# C3   -0.5
# C4    0.5
# C5    1.5
# dtype: float64
print(df.apply(np.mean, axis = 1))
# R1   -8.0
# R2   -3.0
# R3    2.0
# R4    7.0
# dtype: float64
print(df.apply(lambda x : x.max() - x.min()))
# C1    15.0
# C2    15.0
# C3    15.0
# C4    15.0
# C5    15.0
# dtype: float64
print(df.apply(np.exp))
#             C1          C2           C3           C4           C5
# R1    0.000045    0.000123     0.000335     0.000912     0.002479
# R2    0.006738    0.018316     0.049787     0.135335     0.367879
# R3    1.000000    2.718282     7.389056    20.085537    54.598150
# R4  148.413159  403.428793  1096.633158  2980.957987  8103.083928




# ==================================================================================================================================
# DataFrame.aggregate(func=None, axis=0, *args, **kwargs) 또는 별칭으로 DataFrame.agg(func=None, axis=0, *args, **kwargs)
# 지정된 차원(axis)에 대해 하나 이상의 작업을 사용하여 집계
# 함수를 1개만 사용하면 apply()와 동일하다 지정된 메서드를 문자열로 전달할 수도 있다.
# 리스트를 이용해 여러개의 함수를 전달할 수 있다.
# ==================================================================================================================================
df = pd.DataFrame(
    np.random.randint(1, 5, 15).reshape(3, 5) # np.random.randint(1, 5, size=(3, 5)) 와 같다
)
print(df)
#    0  1  2  3  4
# 0  2  3  1  2  4
# 1  4  3  4  4  1
# 2  2  2  3  4  4

print(df.agg(np.sum)) # df.agg("sum")
# 0     8
# 1     8
# 2     8
# 3    10
# 4     9
# dtype: int64

df2 = pd.DataFrame(
    np.random.randn(5, 8),
    columns=('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'),
    index=pd.date_range('2021/07/03', periods=5)
)
print(df2)
#                    A         B         C         D         E         F         G         H
# 2021-07-03 -0.142629  1.060395 -0.358611  0.030513 -0.887380 -0.483378  1.744862  1.287035
# 2021-07-04 -0.244343 -0.573208  2.204391 -0.351602 -1.075160  0.879936 -0.041706  1.111736
# 2021-07-05 -0.831209 -0.328236  0.618028  0.528731 -1.626581  1.073054  0.997673  0.457464
# 2021-07-06  0.066147  2.008383 -2.322917 -0.942159 -0.009623  0.707416  1.319545 -0.900995
# 2021-07-07 -0.739636  0.372018 -1.651403  0.361461 -1.944000 -1.054062 -1.135432  0.862771
print(df2.agg(np.max))
# A    0.066147
# B    2.008383
# C    2.204391
# D    0.528731
# E   -0.009623
# F    1.073054
# G    1.744862
# H    1.287035
# dtype: float64
print(df2['A'].agg(np.sum))  # -1.891669311034919


df = pd.DataFrame(
    np.array([
        [100, 150, 200, 250, 300],
        [200, 300, 400, 500, 600],
        [500, 1000, 1500, 2000, 2500]
    ]),
    index=['R1', 'R2', 'R3'],
    columns=['C1', 'C2', 'C3', 'C4', 'C5']
)
print(df)
#      C1    C2    C3    C4    C5
# R1  100   150   200   250   300
# R2  200   300   400   500   600
# R3  500  1000  1500  2000  2500


print(df.agg([np.max, np.min, np.sum]))
#        C1    C2    C3    C4    C5
# amax  500  1000  1500  2000  2500
# amin  100   150   200   250   300
# sum   800  1450  2100  2750  3400


# ==================================================================================================================================
# 각 요소별로 함수 적용하기
# 모든 함수를 벡터화할 수 있는 것은 아니기 때문에(NumPy 배열을 받고 다른 배열 또는 스칼라 값을 리턴)
# DataFrame의 applymap() 메서드와 Series의 map() 단일값(스칼라 값)을 받고 단일값을 리턴하는 모든 파이썬 함수를 허용한다
# ==================================================================================================================================

print(df)
#      C1    C2    C3    C4    C5
# R1  100   150   200   250   300
# R2  200   300   400   500   600
# R3  500  1000  1500  2000  2500

def f(x):
    return len(str(x))

print(df['C1'].map(f))
# R1    3
# R2    3
# R3    3
# Name: C1, dtype: int64

print(df.applymap(f))
#     C1  C2  C3  C4  C5
# R1   3   3   3   3   3
# R2   3   3   3   3   3
# R3   3   4   4   4   4


# ==================================================================================================================================
# Reindexing and altering labels 재인덱싱, 레이블 변경하기
# reindex()는 Pands의 기본 데이터 정렬 방법이다.
# 다시 인덱싱 하는 것은 특정 axis를 따라 주어진 레이블 집합과 일치시키는 것을 의미한다.
# 1. 새 레이블 집합과 일치하도록 기존 데이털르 재정렬한다.
# 2. 주어진 레이블에 대한 데이터가 존재하지 않으면 레이블 위치에 NaN 을 삽입한다.
# 3. fill 기능으로 누락된 레이블이 있는면 지정된 로직을 사용하여 데이터를 채울 수 있다.
# ==================================================================================================================================

s = pd.Series(np.array([10, 20, 30, 40, 50]), index=['a', 'b', 'c', 'd', 'e',], dtype=np.int64)
print(s)
# a    10
# b    20
# c    30
# d    40
# e    50
# dtype: int64
s = s.reindex(['A', 'b', 'C', 'd']) # A, C 레이블은 시리즈에 포함되지 않으므로 NaN
print(s)
# A     NaN
# b    20.0
# C     NaN
# d    40.0
# dtype: float64

df = pd.DataFrame(
    np.arange(-100, -65).reshape(5, 7),
    index=map(lambda x : 'R'+str(x), [1,2,3,4,5]),
    columns=map(lambda x : 'C'+str(x), [1,2,3,4,5,6,7])
)
print(df)
#      C1  C2  C3  C4  C5  C6  C7
# R1 -100 -99 -98 -97 -96 -95 -94
# R2  -93 -92 -91 -90 -89 -88 -87
# R3  -86 -85 -84 -83 -82 -81 -80
# R4  -79 -78 -77 -76 -75 -74 -73
# R5  -72 -71 -70 -69 -68 -67 -66

print(df.reindex(['R5', 'R4', 'R3', 'NEW_R1', 'NEW_R2'], axis='index')) # axis = 0 과 같다
#           C1    C2    C3    C4    C5    C6    C7
# R5     -72.0 -71.0 -70.0 -69.0 -68.0 -67.0 -66.0
# R4     -79.0 -78.0 -77.0 -76.0 -75.0 -74.0 -73.0
# R3     -86.0 -85.0 -84.0 -83.0 -82.0 -81.0 -80.0
# NEW_R1   NaN   NaN   NaN   NaN   NaN   NaN   NaN
# NEW_R2   NaN   NaN   NaN   NaN   NaN   NaN   NaN
print(df.reindex(['C7', 'C6', 'C5', 'C4', 'NEW_C3', 'NEW_C2', 'NEW_C1', 'NEW_C0'], axis='columns')) # axis = 1 과 같다
#     C7  C6  C5  C4  NEW_C3  NEW_C2  NEW_C1  NEW_C0
# R1 -94 -95 -96 -97     NaN     NaN     NaN     NaN
# R2 -87 -88 -89 -90     NaN     NaN     NaN     NaN
# R3 -80 -81 -82 -83     NaN     NaN     NaN     NaN
# R4 -73 -74 -75 -76     NaN     NaN     NaN     NaN
# R5 -66 -67 -68 -69     NaN     NaN     NaN     NaN








