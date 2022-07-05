import numpy as np
import pandas as pd

# ==================================================================================================================================
# 필수적인 기능
# ==================================================================================================================================

# ▶▶▶ Series및 DataFrame을 NumPy array로 바꾸려면 to_numpy() 또는 numpy.asarray()를 사용한다. (물론 DataFrame의 경우 모든 columns 들의 데이터 타입이 같아야 한다)
ser = pd.Series(pd.date_range("2000", periods=10, tz="Asia/Seoul"))
print(ser)
# 0   2000-01-01 00:00:00+09:00
# 1   2000-01-02 00:00:00+09:00
# 2   2000-01-03 00:00:00+09:00
# 3   2000-01-04 00:00:00+09:00
# 4   2000-01-05 00:00:00+09:00
# 5   2000-01-06 00:00:00+09:00
# 6   2000-01-07 00:00:00+09:00
# 7   2000-01-08 00:00:00+09:00
# 8   2000-01-09 00:00:00+09:00
# 9   2000-01-10 00:00:00+09:00

print(repr(ser.to_numpy(dtype=object))) # dtype="object" 이렇게 문자열로 해도 상관 X
# array([Timestamp('2000-01-01 00:00:00+0900', tz='Asia/Seoul'),
#        Timestamp('2000-01-02 00:00:00+0900', tz='Asia/Seoul'),
#        Timestamp('2000-01-03 00:00:00+0900', tz='Asia/Seoul'),
#        Timestamp('2000-01-04 00:00:00+0900', tz='Asia/Seoul'),
#        Timestamp('2000-01-05 00:00:00+0900', tz='Asia/Seoul'),
#        Timestamp('2000-01-06 00:00:00+0900', tz='Asia/Seoul'),
#        Timestamp('2000-01-07 00:00:00+0900', tz='Asia/Seoul'),
#        Timestamp('2000-01-08 00:00:00+0900', tz='Asia/Seoul'),
#        Timestamp('2000-01-09 00:00:00+0900', tz='Asia/Seoul'),
#        Timestamp('2000-01-10 00:00:00+0900', tz='Asia/Seoul')],
#       dtype=object)

print(repr(ser.to_numpy(dtype="datetime64[ns]")))
# array(['1999-12-31T15:00:00.000000000', '2000-01-01T15:00:00.000000000',
#        '2000-01-02T15:00:00.000000000', '2000-01-03T15:00:00.000000000',
#        '2000-01-04T15:00:00.000000000', '2000-01-05T15:00:00.000000000',
#        '2000-01-06T15:00:00.000000000', '2000-01-07T15:00:00.000000000',
#        '2000-01-08T15:00:00.000000000', '2000-01-09T15:00:00.000000000'],
#       dtype='datetime64[ns]')


df = pd.DataFrame(
    data = {
        "COL1": pd.Series([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]),
        "COL2": pd.Series([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]),
        "COL3": pd.Series(pd.date_range("2000", periods=10, tz="Asia/Seoul")),
        "COL4": pd.Series(list("ABCEDFGHI")),
        "COL5": 20000,
        "COL6": np.linspace(-100+20J, 0, 10) # 원래 수학에서 복소수는 대소판별이 없다 근데 이상하게 여기서는 된다;;
    }
)
df['COL7'] = df['COL6'].map(lambda x : x.conjugate())
print(df)
#    COL1  COL2                      COL3 COL4   COL5                  COL6                  COL7
# 0   1.0   1.0 2000-01-01 00:00:00+09:00    A  20000  -100.00000+20.00000j  -100.00000-20.00000j
# 1   2.0   2.0 2000-01-02 00:00:00+09:00    B  20000 -88.888889+17.777778j -88.888889-17.777778j
# 2   3.0   3.0 2000-01-03 00:00:00+09:00    C  20000 -77.777778+15.555556j -77.777778-15.555556j
# 3   4.0   4.0 2000-01-04 00:00:00+09:00    E  20000 -66.666667+13.333333j -66.666667-13.333333j
# 4   5.0   5.0 2000-01-05 00:00:00+09:00    D  20000 -55.555556+11.111111j -55.555556-11.111111j
# 5   6.0   6.0 2000-01-06 00:00:00+09:00    F  20000  -44.444444+8.888889j  -44.444444-8.888889j
# 6   7.0   7.0 2000-01-07 00:00:00+09:00    G  20000  -33.333333+6.666667j  -33.333333-6.666667j
# 7   8.0   8.0 2000-01-08 00:00:00+09:00    H  20000  -22.222222+4.444444j  -22.222222-4.444444j
# 8   NaN   9.0 2000-01-09 00:00:00+09:00    I  20000  -11.111111+2.222222j  -11.111111-2.222222j
# 9   NaN   NaN 2000-01-10 00:00:00+09:00  NaN  20000  0.0000000+0.0000000j  0.0000000-0.0000000j

print(df['COL1'].dtype) # float64
print(df['COL2'].dtype) # float64
print(df['COL3'].dtype) # datetime64[ns, Asia/Seoul]
print(df['COL4'].dtype) # object
print(df['COL5'].dtype) # int64
print(df['COL6'].dtype) # complex128
print(df['COL7'].dtype) # complex128
print(repr(df.to_numpy()))  # np.asarray(df).__repr__() 와 같다
# array([[1.0, 1.0, Timestamp('2000-01-01 00:00:00+0900', tz='Asia/Seoul'),
#         'A', 20000, (-100+20j), (-100-20j)],
#        [2.0, 2.0, Timestamp('2000-01-02 00:00:00+0900', tz='Asia/Seoul'),
#         'B', 20000, (-88.88888888888889+17.77777777777778j),
#         (-88.88888888888889-17.77777777777778j)],
#        [3.0, 3.0, Timestamp('2000-01-03 00:00:00+0900', tz='Asia/Seoul'),
#         'C', 20000, (-77.77777777777777+15.555555555555555j),
#         (-77.77777777777777-15.555555555555555j)],
#        [4.0, 4.0, Timestamp('2000-01-04 00:00:00+0900', tz='Asia/Seoul'),
#         'E', 20000, (-66.66666666666667+13.333333333333332j),
#         (-66.66666666666667-13.333333333333332j)],
#        [5.0, 5.0, Timestamp('2000-01-05 00:00:00+0900', tz='Asia/Seoul'),
#         'D', 20000, (-55.55555555555556+11.11111111111111j),
#         (-55.55555555555556-11.11111111111111j)],
#        [6.0, 6.0, Timestamp('2000-01-06 00:00:00+0900', tz='Asia/Seoul'),
#         'F', 20000, (-44.44444444444444+8.88888888888889j),
#         (-44.44444444444444-8.88888888888889j)],
#        [7.0, 7.0, Timestamp('2000-01-07 00:00:00+0900', tz='Asia/Seoul'),
#         'G', 20000, (-33.33333333333334+6.666666666666666j),
#         (-33.33333333333334-6.666666666666666j)],
#        [8.0, 8.0, Timestamp('2000-01-08 00:00:00+0900', tz='Asia/Seoul'),
#         'H', 20000, (-22.22222222222223+4.444444444444443j),
#         (-22.22222222222223-4.444444444444443j)],
#        [nan, 9.0, Timestamp('2000-01-09 00:00:00+0900', tz='Asia/Seoul'),
#         'I', 20000, (-11.111111111111114+2.2222222222222214j),
#         (-11.111111111111114-2.2222222222222214j)],
#        [nan, nan, Timestamp('2000-01-10 00:00:00+0900', tz='Asia/Seoul'),
#         nan, 20000, 0j, -0j]], dtype=object)


# ==================================================================================================================================
# 가속화된 작업 => 실습은 X
# Pandas는 numexpr, bottleneck이 기본적으로 활성화되어있다 => 특정 유형의 이진 숫자 및 불(boolean) 연산 가속화를 지원한다
# 이러한 라이브러리는 대용량 데이터를 처리할 때 유용하다
# ==================================================================================================================================


# ==================================================================================================================================
# 유연한 산술연산
# DataFrame.add(other, axis='columns', level=None, fill_value=None)
# DataFrame.sub(other, axis='columns', level=None, fill_value=None)
# DataFrame.mul(other, axis='columns', level=None, fill_value=None)
# DataFrame.div(other, axis='columns', level=None, fill_value=None)
# DataFrame.mod(other, axis='columns', level=None, fill_value=None)
# DataFrame.pow(other, axis='columns', level=None, fill_value=None)
# ▶▶▶ add, sub, mul, div, mod, pow 는 각각 +, -, *, /, //, %, ** 연산자와 동일하다
# 파라미터
# other      = scalar, sequence, Series, or DataFrame
#              Any single or multiple element data structure, or list-like object.
# axis       = {0 or 'index', 1 or 'columns'}
#              index로 비교할지 columns으로 비교할지 여부
# level      = int or lable
#              Broadcast across a level, matching Index values on the passed MultiIndex level.
# fill_value = 계산하기 전에 누락데이터(NaN)을 대체할 값. 만약 두 DataFrame 위치의 데이터가 모두 NaN이면 결과도 NaN이다
# ==================================================================================================================================

df = pd.DataFrame (
    np.linspace(30, -50, 12).reshape(4, 3)
)
df.iloc[0, 0], df.iloc[-1, -1] = np.nan, np.nan
print(df)
#            0          1          2
# 0        NaN  22.727273  15.454545
# 1   8.181818   0.909091  -6.363636
# 2 -13.636364 -20.909091 -28.181818
# 3 -35.454545 -42.727273        NaN

df2 = pd.DataFrame (
    data = 10,
    index=list(range(0, 4)),
    columns=list(range(0, 3))
)

print(df2)
#     0   1   2
# 0  10  10  10
# 1  10  10  10
# 2  10  10  10
# 3  10  10  10



print(df + df2) # NaN(누락 데이터)은 산술연산에서 무시된다
#            0          1          2
# 0        NaN  32.727273  25.454545
# 1  18.181818  10.909091   3.636364
# 2  -3.636364 -10.909091 -18.181818
# 3 -25.454545 -32.727273        NaN

print(df / df2)
#           0         1         2
# 0       NaN  2.272727  1.545455
# 1  0.818182  0.090909 -0.636364
# 2 -1.363636 -2.090909 -2.818182
# 3 -3.545455 -4.272727       NaN



print(df.gt(df2)) # df > df2
#        0      1      2
# 0  False   True   True
# 1  False  False  False
# 2  False  False  False
# 3  False  False  False
print(df.lt(df2)) # df < df2
#        0      1      2
# 0  False  False  False
# 1   True   True   True
# 2   True   True   True
# 3   True   True  False


# ==================================================================================================================================
# 유연한 비교연산
# Series및 DataFrame에는 위에서 설명한 이진 산술 연산과 비슷한 이진 비교 연산도 재공한다
# DataFrame.eq(other, axis='columns', level=None)
# DataFrame.ne(other, axis='columns', level=None)
# DataFrame.le(other, axis='columns', level=None)
# DataFrame.lt(other, axis='columns', level=None)
# DataFrame.ge(other, axis='columns', level=None)
# DataFrame.gt(other, axis='columns', level=None)
# ▶▶▶ eq, ne, le, lt, ge, gt 는 각각의 요소별로 ==, !=, <=, <, >=, > 연산을 수행한다.
# ==================================================================================================================================

df = pd.DataFrame(
    np.arange(5 * 6).reshape(6, 5),
    index=list(map(lambda x : 'R'+str(x), range(6))),
    columns=list(map(lambda x : 'C'+str(x), range(5)))
)

df2 = pd.DataFrame(
    np.arange(40).reshape(8, 5),
    index=list(map(lambda x : 'R'+str(x), range(8))),
    columns=list(map(lambda x : 'C'+str(x), range(5)))
)
df.loc['C6'] = np.linspace(10, -20, 5)
df2['C5'] = np.linspace(-10, 20, 8)
print(df)
#       C0    C1    C2    C3    C4
# R0   0.0   1.0   2.0   3.0   4.0
# R1   5.0   6.0   7.0   8.0   9.0
# R2  10.0  11.0  12.0  13.0  14.0
# R3  15.0  16.0  17.0  18.0  19.0
# R4  20.0  21.0  22.0  23.0  24.0
# R5  25.0  26.0  27.0  28.0  29.0
# C6  10.0   2.5  -5.0 -12.5 -20.0
print(df2)
#     C0  C1  C2  C3  C4         C5
# R0   0   1   2   3   4 -10.000000
# R1   5   6   7   8   9  -5.714286
# R2  10  11  12  13  14  -1.428571
# R3  15  16  17  18  19   2.857143
# R4  20  21  22  23  24   7.142857
# R5  25  26  27  28  29  11.428571
# R6  30  31  32  33  34  15.714286
# R7  35  36  37  38  39  20.000000

print(df.eq(df2))
#        C0     C1     C2     C3     C4     C5
# C6  False  False  False  False  False  False
# R0   True   True   True   True   True  False
# R1   True   True   True   True   True  False
# R2   True   True   True   True   True  False
# R3   True   True   True   True   True  False
# R4   True   True   True   True   True  False
# R5   True   True   True   True   True  False
# R6  False  False  False  False  False  False
# R7  False  False  False  False  False  False

print(df.ne(df2))
#        C0     C1     C2     C3     C4    C5
# C6   True   True   True   True   True  True
# R0  False  False  False  False  False  True
# R1  False  False  False  False  False  True
# R2  False  False  False  False  False  True
# R3  False  False  False  False  False  True
# R4  False  False  False  False  False  True
# R5  False  False  False  False  False  True
# R6   True   True   True   True   True  True
# R7   True   True   True   True   True  True

# ==================================================================================================================================
# 부울 타입으로 감소연산
# DataFrame.empty  Series 또는 DataFrame에 항목이 없으면(axes의 길이가 0이면) True, 항목이 있으면 False
# DataFrame.any(axis=0, bool_only=None, skipna=True, level=None, **kwargs) axis 별로 True이거나 이에 상응하는(non-zero or non-empty)값이 하나 이상 있으면 True 없으면 False
# DataFrame.all(axis=0, bool_only=None, skipna=True, level=None, **kwargs) axis 별로 False이거나 이에 상응하는(0 또는 비어있는 값)이 적어도 하나 있으면 False 하나도 없으면 True
# 
# ==================================================================================================================================

df = pd.DataFrame({'A' : [1, 2], 'B' : [0, 2], 'C': [0, 0]})
print(df)
#    A  B  C
# 0  1  0  0
# 1  2  2  0
print(df.any())
# A     True
# B     True
# C    False
# dtype: bool
print(df.any(axis=1))
# 0    True
# 1    True
# dtype: bool

print(pd.Series([False, False]).any())        # False
print(pd.Series([False, -5]).any())           # True
print(pd.Series([], dtype=np.float64).any())  # False
print(pd.Series([0, np.nan]).any())           # False
print(pd.Series([np.nan]).any())              # False
print(pd.Series([np.nan]).any(skipna=False))  # True => np.nan은 0이 아니므로 True로 간주된다


print(pd.Series([True, True]).all())          # True
print(pd.Series([True, False]).all())         # False
print(pd.Series([], dtype="float64").all())   # True  => 값 자체가 없음
print(pd.Series([[]], dtype="float64").all()) # False => 빈 값이 있음
print(pd.Series([np.nan]).all())              # True
print(pd.Series([np.nan]).all(skipna=False))  # True


# ==================================================================================================================================
# 객체가 동일한지 비교하기
# 가끔 동일한 결과를 계산한느 방법이 두 가지 이상 있을 수 있다 예를 들어 df + df 와 df * 2를 생각해보면 된다
# 정말 df + df와 df * 2가 동일한 지는 (df + df == df * 2).all()을 사용한느 것을 상상할 수 있다. 그런데 실제로 이 표현은 틀렸다.
# NaN은 == 연산으로 비교할 수 없기 대문이다
# ==================================================================================================================================

df = pd.DataFrame(
    np.arange(-10, 10).reshape(4, 5)
)
df.loc[0, 0] = np.nan
df2 = df.copy()
print(df)
#      0  1  2  3  4
# 0  NaN -9 -8 -7 -6
# 1 -5.0 -4 -3 -2 -1
# 2  0.0  1  2  3  4
# 3  5.0  6  7  8  9
print(df2)
#      0  1  2  3  4
# 0  NaN -9 -8 -7 -6
# 1 -5.0 -4 -3 -2 -1
# 2  0.0  1  2  3  4
# 3  5.0  6  7  8  9

print(df * 2 == df + df) # NaN은 비교하면 False로 된다
#        0     1     2     3     4
# 0  False  True  True  True  True
# 1   True  True  True  True  True
# 2   True  True  True  True  True
# 3   True  True  True  True  True
df.loc[0, 0], df2.loc[0, 0] = -10, -10 # NaN을 다시 -10으로 하면

print(df * 2 == df + df)
#       0     1     2     3     4
# 0  True  True  True  True  True
# 1  True  True  True  True  True
# 2  True  True  True  True  True
# 3  True  True  True  True  True
print((df * 2 == df + df).all(axis=None)) # True
print((df * 2).equals(df + df))           # True



