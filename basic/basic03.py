import pandas as pd
import numpy as np

# ================================================================================================================================
# Boolean indexing
# ================================================================================================================================

df = pd.DataFrame(
    np.linspace(-10, 10, 6*7).reshape(6, 7),
    index=['R1', 'R2', 'R3', 'R4', 'R5', 'R6'],
    columns=['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7']
)
print(df)
#            C1        C2        C3        C4        C5        C6         C7
# R1 -10.000000 -9.512195 -9.024390 -8.536585 -8.048780 -7.560976  -7.073171
# R2  -6.585366 -6.097561 -5.609756 -5.121951 -4.634146 -4.146341  -3.658537
# R3  -3.170732 -2.682927 -2.195122 -1.707317 -1.219512 -0.731707  -0.243902
# R4   0.243902  0.731707  1.219512  1.707317  2.195122  2.682927   3.170732
# R5   3.658537  4.146341  4.634146  5.121951  5.609756  6.097561   6.585366
# R6   7.073171  7.560976  8.048780  8.536585  9.024390  9.512195  10.000000

print(df[df['C1'] > -3.1708]) # C1 값이 -3.1708 보다 큰 데이터 출력

#           C1        C2        C3        C4        C5        C6         C7
# R3 -3.170732 -2.682927 -2.195122 -1.707317 -1.219512 -0.731707  -0.243902
# R4  0.243902  0.731707  1.219512  1.707317  2.195122  2.682927   3.170732
# R5  3.658537  4.146341  4.634146  5.121951  5.609756  6.097561   6.585366
# R6  7.073171  7.560976  8.048780  8.536585  9.024390  9.512195  10.000000
print(df[-5.55 < df])
#           C1        C2        C3        C4        C5        C6         C7
# R1       NaN       NaN       NaN       NaN       NaN       NaN        NaN
# R2       NaN       NaN       NaN -5.121951 -4.634146 -4.146341  -3.658537
# R3 -3.170732 -2.682927 -2.195122 -1.707317 -1.219512 -0.731707  -0.243902
# R4  0.243902  0.731707  1.219512  1.707317  2.195122  2.682927   3.170732
# R5  3.658537  4.146341  4.634146  5.121951  5.609756  6.097561   6.585366
# R6  7.073171  7.560976  8.048780  8.536585  9.024390  9.512195  10.000000


# ▶▶▶ isin() 메서드로 필터링
df2 = df.copy()
df2['GOODS'] = ['book', 'desk', 'phone', 'shirts', 'nostalgia', 'nostalgia']
print(df2[df2['GOODS'].isin(["nostalgia", "desk"])])
#           C1        C2        C3        C4        C5        C6         C7      GOODS
# R2 -6.585366 -6.097561 -5.609756 -5.121951 -4.634146 -4.146341  -3.658537       desk
# R5  3.658537  4.146341  4.634146  5.121951  5.609756  6.097561   6.585366  nostalgia
# R6  7.073171  7.560976  8.048780  8.536585  9.024390  9.512195  10.000000  nostalgia


# ================================================================================================================================
# Setting
# ================================================================================================================================

s1 = pd.Series([1,2,3,4,5,6], index=['R1', 'R2', 'R3', 'R4', 'R5', 'R6'], dtype=np.int32) # index가 동일하지 않으면 데이터가 NaN으로 들어간다
df['C8'] = s1
print(s1)
# R1    1
# R2    2
# R3    3
# R4    4
# R5    5
# R6    6
# dtype: int32
print(df)
#            C1        C2        C3        C4        C5        C6         C7  C8
# R1 -10.000000 -9.512195 -9.024390 -8.536585 -8.048780 -7.560976  -7.073171   1
# R2  -6.585366 -6.097561 -5.609756 -5.121951 -4.634146 -4.146341  -3.658537   2
# R3  -3.170732 -2.682927 -2.195122 -1.707317 -1.219512 -0.731707  -0.243902   3
# R4   0.243902  0.731707  1.219512  1.707317  2.195122  2.682927   3.170732   4
# R5   3.658537  4.146341  4.634146  5.121951  5.609756  6.097561   6.585366   5
# R6   7.073171  7.560976  8.048780  8.536585  9.024390  9.512195  10.000000   6

s1 = pd.Series(pd.date_range('2020-03-09', '2020-03-10', periods=6), index=['R1', 'R2', 'R3', 'R4', 'R5', 'R6'])
df['C5'] = s1
print(df)
#            C1        C2        C3        C4                  C5        C6         C7  C8
# R1 -10.000000 -9.512195 -9.024390 -8.536585 2020-03-09 00:00:00 -7.560976  -7.073171   1
# R2  -6.585366 -6.097561 -5.609756 -5.121951 2020-03-09 04:48:00 -4.146341  -3.658537   2
# R3  -3.170732 -2.682927 -2.195122 -1.707317 2020-03-09 09:36:00 -0.731707  -0.243902   3
# R4   0.243902  0.731707  1.219512  1.707317 2020-03-09 14:24:00  2.682927   3.170732   4
# R5   3.658537  4.146341  4.634146  5.121951 2020-03-09 19:12:00  6.097561   6.585366   5
# R6   7.073171  7.560976  8.048780  8.536585 2020-03-10 00:00:00  9.512195  10.000000   6
print(df.dtypes)
# C1           float64
# C2           float64
# C3           float64
# C4           float64
# C5    datetime64[ns]
# C6           float64
# C7           float64
# C8             int32
# dtype: object

df2 = df.loc[:, 'C4':'C1':-1]
print(df2)
#           C4        C3        C2         C1
# R1 -8.536585 -9.024390 -9.512195 -10.000000
# R2 -5.121951 -5.609756 -6.097561  -6.585366
# R3 -1.707317 -2.195122 -2.682927  -3.170732
# R4  1.707317  1.219512  0.731707   0.243902
# R5  5.121951  4.634146  4.146341   3.658537
# R6  8.536585  8.048780  7.560976   7.073171

df2[df2 > 0] = -df2
print(df2)
#           C4        C3        C2         C1
# R1 -8.536585 -9.024390 -9.512195 -10.000000
# R2 -5.121951 -5.609756 -6.097561  -6.585366
# R3 -1.707317 -2.195122 -2.682927  -3.170732
# R4 -1.707317 -1.219512 -0.731707  -0.243902
# R5 -5.121951 -4.634146 -4.146341  -3.658537
# R6 -8.536585 -8.048780 -7.560976  -7.073171


# ================================================================================================================================
# Missing data (누락 데이터)
# Pandas는 기본적으로 누락된 데이터를 np.nan을 사용하여 나타낸다 그리고 이 누락 데이터는 계산에 포함되지 않는다
# ================================================================================================================================

df2 = df2.reindex(
    index = pd.date_range('20191229', periods=8),
    columns = list(df.columns) + ["E1", 'E2']
)
print(df2)
#             C1  C2  C3  C4  C5  C6  C7  C8  E1  E2
# 2019-12-29 NaN NaN NaN NaN NaN NaN NaN NaN NaN NaN
# 2019-12-30 NaN NaN NaN NaN NaN NaN NaN NaN NaN NaN
# 2019-12-31 NaN NaN NaN NaN NaN NaN NaN NaN NaN NaN
# 2020-01-01 NaN NaN NaN NaN NaN NaN NaN NaN NaN NaN
# 2020-01-02 NaN NaN NaN NaN NaN NaN NaN NaN NaN NaN
# 2020-01-03 NaN NaN NaN NaN NaN NaN NaN NaN NaN NaN
# 2020-01-04 NaN NaN NaN NaN NaN NaN NaN NaN NaN NaN
# 2020-01-05 NaN NaN NaN NaN NaN NaN NaN NaN NaN NaN

df2.loc['2019-12-29':'2020-01-01', 'C1':'C8':2] = 10
print(df2)
#               C1  C2    C3  C4    C5  C6    C7  C8  E1  E2
# 2019-12-29  10.0 NaN  10.0 NaN  10.0 NaN  10.0 NaN NaN NaN
# 2019-12-30  10.0 NaN  10.0 NaN  10.0 NaN  10.0 NaN NaN NaN
# 2019-12-31  10.0 NaN  10.0 NaN  10.0 NaN  10.0 NaN NaN NaN
# 2020-01-01  10.0 NaN  10.0 NaN  10.0 NaN  10.0 NaN NaN NaN
# 2020-01-02   NaN NaN   NaN NaN   NaN NaN   NaN NaN NaN NaN
# 2020-01-03   NaN NaN   NaN NaN   NaN NaN   NaN NaN NaN NaN
# 2020-01-04   NaN NaN   NaN NaN   NaN NaN   NaN NaN NaN NaN
# 2020-01-05   NaN NaN   NaN NaN   NaN NaN   NaN NaN NaN NaN
df2.loc[['20191229','20191230','20191231','20200101'], ['E1', 'E2']] = 2/3
print(df2)
#               C1  C2    C3  C4    C5  C6    C7  C8        E1        E2
# 2019-12-29  10.0 NaN  10.0 NaN  10.0 NaN  10.0 NaN  0.666667  0.666667
# 2019-12-30  10.0 NaN  10.0 NaN  10.0 NaN  10.0 NaN  0.666667  0.666667
# 2019-12-31  10.0 NaN  10.0 NaN  10.0 NaN  10.0 NaN  0.666667  0.666667
# 2020-01-01  10.0 NaN  10.0 NaN  10.0 NaN  10.0 NaN  0.666667  0.666667
# 2020-01-02   NaN NaN   NaN NaN   NaN NaN   NaN NaN       NaN       NaN
# 2020-01-03   NaN NaN   NaN NaN   NaN NaN   NaN NaN       NaN       NaN
# 2020-01-04   NaN NaN   NaN NaN   NaN NaN   NaN NaN       NaN       NaN
# 2020-01-05   NaN NaN   NaN NaN   NaN NaN   NaN NaN       NaN       NaN
df2.iloc[-1:-5:-1, :] = np.pi
print(df2)
#                    C1        C2         C3        C4  ...         C7        C8        E1        E2
# 2019-12-29  10.000000       NaN  10.000000       NaN  ...  10.000000       NaN  0.666667  0.666667
# 2019-12-30  10.000000       NaN  10.000000       NaN  ...  10.000000       NaN  0.666667  0.666667
# 2019-12-31  10.000000       NaN  10.000000       NaN  ...  10.000000       NaN  0.666667  0.666667
# 2020-01-01  10.000000       NaN  10.000000       NaN  ...  10.000000       NaN  0.666667  0.666667
# 2020-01-02   3.141593  3.141593   3.141593  3.141593  ...   3.141593  3.141593  3.141593  3.141593
# 2020-01-03   3.141593  3.141593   3.141593  3.141593  ...   3.141593  3.141593  3.141593  3.141593
# 2020-01-04   3.141593  3.141593   3.141593  3.141593  ...   3.141593  3.141593  3.141593  3.141593
# 2020-01-05   3.141593  3.141593   3.141593  3.141593  ...   3.141593  3.141593  3.141593  3.141593

# ▶▶▶ NaN인 row를 전부 삭제
print(df2.dropna(how="any"))
#                   C1        C2        C3        C4        C5        C6        C7        C8        E1        E2
# 2020-01-02  3.141593  3.141593  3.141593  3.141593  3.141593  3.141593  3.141593  3.141593  3.141593  3.141593
# 2020-01-03  3.141593  3.141593  3.141593  3.141593  3.141593  3.141593  3.141593  3.141593  3.141593  3.141593
# 2020-01-04  3.141593  3.141593  3.141593  3.141593  3.141593  3.141593  3.141593  3.141593  3.141593  3.141593
# 2020-01-05  3.141593  3.141593  3.141593  3.141593  3.141593  3.141593  3.141593  3.141593  3.141593  3.141593

# ▶▶▶ NaN인 값을 전부 채우기
print(df2.fillna(value="Alternative Value")) 
#                    C1                 C2         C3                 C4         C5                 C6         C7                 C8        E1        E2
# 2019-12-29  10.000000  Alternative Value  10.000000  Alternative Value  10.000000  Alternative Value  10.000000  Alternative Value  0.666667  0.666667  
# 2019-12-30  10.000000  Alternative Value  10.000000  Alternative Value  10.000000  Alternative Value  10.000000  Alternative Value  0.666667  0.666667  
# 2019-12-31  10.000000  Alternative Value  10.000000  Alternative Value  10.000000  Alternative Value  10.000000  Alternative Value  0.666667  0.666667  
# 2020-01-01  10.000000  Alternative Value  10.000000  Alternative Value  10.000000  Alternative Value  10.000000  Alternative Value  0.666667  0.666667  
# 2020-01-02   3.141593           3.141593   3.141593           3.141593   3.141593           3.141593   3.141593           3.141593  3.141593  3.141593  
# 2020-01-03   3.141593           3.141593   3.141593           3.141593   3.141593           3.141593   3.141593           3.141593  3.141593  3.141593  
# 2020-01-04   3.141593           3.141593   3.141593           3.141593   3.141593           3.141593   3.141593           3.141593  3.141593  3.141593  
# 2020-01-05   3.141593           3.141593   3.141593           3.141593   3.141593           3.141593   3.141593           3.141593  3.141593  3.141593
print(df2.dtypes)
# C1    float64
# C2    float64
# C3    float64
# C4    float64
# C5    float64
# C6    float64
# C7    float64
# C8    float64
# E1    float64
# E2    float64
# dtype: object

# ▶▶▶ 데이터가 NaN인지 아닌지를 전부 bool 값으로 마스킹 처리
print(pd.isna(df2))
#                C1     C2     C3     C4     C5     C6     C7     C8     E1     E2
# 2019-12-29  False   True  False   True  False   True  False   True  False  False
# 2019-12-30  False   True  False   True  False   True  False   True  False  False
# 2019-12-31  False   True  False   True  False   True  False   True  False  False
# 2020-01-01  False   True  False   True  False   True  False   True  False  False
# 2020-01-02  False  False  False  False  False  False  False  False  False  False
# 2020-01-03  False  False  False  False  False  False  False  False  False  False
# 2020-01-04  False  False  False  False  False  False  False  False  False  False
# 2020-01-05  False  False  False  False  False  False  False  False  False  False



