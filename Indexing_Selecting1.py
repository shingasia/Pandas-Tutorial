import numpy as np
import pandas as pd

# ==================================================================================================================================
# Indexing 과 Selecting
# Python과 NumPy의 인덱싱 연산자 [ ]와 속성 연산자 . 처럼 다양한 사용사례에서 Pandas 데이터 구조에 빠르고 쉽게 엑세스 할 수 있다.
# Python 딕셔너리와 NumPy 배열을 다루는 방법을 이미 알고있다면 대화형 작업을 직관적으로 만든다.
# 그러나 접근할 데이터의 유형을 미리 알 수 없기 때문에 표준 연산자를 직접 사용하는 것은 최적화에 한계가 있다.
# Pandas를 사용할 때는 최적화된 데이터 액세스 방법이 따로 있다.
# ==================================================================================================================================

# ==================================================================================================================================
# ▶▶▶ .loc 라벨(Label) 기반으로 허용되는 입력값은 다음과 같다
# 1) 5 또는 'A'처럼 싱글 라벨 (여기서 5는 인덱스가 아니라 라벨 이름이다 -> 정수도 된다)
# 2) ['A', 'B', 'C'] 처럼 라벨 여러개 있는 배열
# 3) 'COL2:COL8' 처럼 슬라이싱 (보통의 Python 슬라이스와 달리 시작과 끝 모두 포함)
# 4) A boolean array
# 5) A callable function with one argument (the calling Series or DataFrame) and that returns valid output for indexing (one of the above).
# ==================================================================================================================================
df = pd.DataFrame(
    np.arange(-100, -60).reshape(5, 8),
    index=map(lambda x : 'R'+str(x), [1,2,3,4,5]),
    columns=[5, 10, 15, 20, 25, 30, 35, 40]
)
print(df)
#      5   10  15  20  25  30  35  40
# R1 -100 -99 -98 -97 -96 -95 -94 -93
# R2  -92 -91 -90 -89 -88 -87 -86 -85
# R3  -84 -83 -82 -81 -80 -79 -78 -77
# R4  -76 -75 -74 -73 -72 -71 -70 -69
# R5  -68 -67 -66 -65 -64 -63 -62 -61

print(df.loc['R1', 15])      # -98

print(df.loc[:, 35:10:-1])
# 라벨 슬라이싱은 경계포함이다, 그리고 라벨이 정수 타입이어도 
# .loc은 위치가 아니라 기본적으로 라벨 '이름'으로 인덱싱 하기 때문에 -5가 아니라 -1로 해야 한 라벨씩 거꾸로 출력한다

#     35  30  25  20  15  10
# R1 -94 -95 -96 -97 -98 -99
# R2 -86 -87 -88 -89 -90 -91
# R3 -78 -79 -80 -81 -82 -83
# R4 -70 -71 -72 -73 -74 -75
# R5 -62 -63 -64 -65 -66 -67

print(df.loc[[True, False, False, True, True], 15:35]) # 이렇게 bool 배열로도 가능하다
#     15  20  25  30  35
# R1 -98 -97 -96 -95 -94
# R4 -74 -73 -72 -71 -70
# R5 -66 -65 -64 -63 -62

print(df.loc[lambda x : (x[40] >= -85) & (x[40] <= -65), :]) # 조건마다 괄호를 씌우고 and 대신에 '&'를 써야한다
#     5   10  15  20  25  30  35  40
# R2 -92 -91 -90 -89 -88 -87 -86 -85
# R3 -84 -83 -82 -81 -80 -79 -78 -77
# R4 -76 -75 -74 -73 -72 -71 -70 -69

print(df.loc['R2':, lambda x : [10, 20, 30, 40]])
#     10  20  30  40
# R2 -91 -89 -87 -85
# R3 -83 -81 -79 -77
# R4 -75 -73 -71 -69
# R5 -67 -65 -63 -61
df = pd.DataFrame(
    {
        '상품명' : ['상품1', '상품2', '상품3', '상품4', '상품5'],
        '주문수량' :[10, 13, 15, 17, 19],
        '가격' : [34500, 19800, 26700, 12500, 24300],
    },
)
print(df)
#    상품명   주문수량     가격
# 0   상품1         10    34500
# 1   상품2         13    19800
# 2   상품3         15    26700
# 3   상품4         17    12500
# 4   상품5         19    24300

print(df.loc[df['가격'] > 20000]) # 앞에서 배운것 처럼 이런 조건식도 가능
#    상품명   주문수량     가격
# 0   상품1         10    34500
# 2   상품3         15    26700
# 4   상품5         19    24300

print(df.loc[df['주문수량'] <= 15, '가격': '상품명':-1])
#       가격  주문수량  상품명
# 0    34500        10   상품1
# 1    19800        13   상품2
# 2    26700        15   상품3


# ==================================================================================================================================
# ▶▶▶ .iloc 정수 위치 기반(0 부터 축의 길이 - 1 까지)으로 허용되는 입력값은 다음과 같다
# 1) 정수값 1개
# 2) [4, 3, -1] 처럼 정수 여러개
# 3) 1:5 처럼 슬라이싱
# 4) A boolean array
# 5) A callable function with one argument (the calling Series or DataFrame) and that returns valid output for indexing (one of the above).
# 6) A tuple of row (and column) indexes, whose elements are one of the above types.
#    요소가 위 유형 중 하나인 행(및 열) 인덱스의 튜플
# ==================================================================================================================================
df = pd.DataFrame(
    np.arange(10, 70).reshape(6, 10),
    index=map(lambda a : 'R'+str(a), [1,2,3,4,5,6]),
    columns=map(lambda a : 'C'+str(a), [1,2,3,4,5,6,7,8,9,10])
)
print(df)
#     C1  C2  C3  C4  C5  C6  C7  C8  C9  C10
# R1  10  11  12  13  14  15  16  17  18   19
# R2  20  21  22  23  24  25  26  27  28   29
# R3  30  31  32  33  34  35  36  37  38   39
# R4  40  41  42  43  44  45  46  47  48   49
# R5  50  51  52  53  54  55  56  57  58   59
# R6  60  61  62  63  64  65  66  67  68   69

print(df.iloc[-4])  # R3 행
# C1     30
# C2     31
# C3     32
# C4     33
# C5     34
# C6     35
# C7     36
# C8     37
# C9     38
# C10    39
# Name: R3, dtype: int32
print(df.iloc[:, -4])    # 전체행, C7열
# R1    16
# R2    26
# R3    36
# R4    46
# R5    56
# R6    66
# Name: C7, dtype: int32
print(df.iloc[[2, 4, -2], :])
#     C1  C2  C3  C4  C5  C6  C7  C8  C9  C10
# R3  30  31  32  33  34  35  36  37  38   39
# R5  50  51  52  53  54  55  56  57  58   59
# R5  50  51  52  53  54  55  56  57  58   59

print(df.iloc[[2, 4, -2], [-3, -3, 5]])
#     C8  C8  C6
# R3  37  37  35
# R5  57  57  55
# R5  57  57  55

print(df.iloc[::-2, -1:-9:-1])
#     C10  C9  C8  C7  C6  C5  C4  C3
# R6   69  68  67  66  65  64  63  62
# R4   49  48  47  46  45  44  43  42
# R2   29  28  27  26  25  24  23  22

print(df.iloc[:, df.columns.map(lambda x : True if int(x.replace('C','')) % 2 == 0 else False)]) # boolean array도 가능
#     C2  C4  C6  C8  C10
# R1  11  13  15  17   19
# R2  21  23  25  27   29
# R3  31  33  35  37   39
# R4  41  43  45  47   49
# R5  51  53  55  57   59
# R6  61  63  65  67   69


# ==================================================================================================================================
# 다차원 선택이 있는 객체에서 값을 가져올 때 다음과 같은 표기법을 사용한다(이 예제에서는 .loc을 사용하지만 .iloc에도 적용된다)
# 모든 차원(axis)의 접근자는 ':'가 될 수 있다 표기에서 생략된 차원은 다 ':'로 간주된다. 그러니까 p.loc['a']는 p.loc['a',:,:]와 동일하다.
# Series      ===> s.loc[indexer]
# DataFrame   ===> df.loc[row_indexer, column_indexer]
# ▶▶▶ .loc, .iloc, [] 세 가지 인덱싱 방법 모두 알아두면 좋다
# ==================================================================================================================================

df[['C1', 'C2']] = df[['C2', 'C1']] # C1과 C2 바꾸기
print(df)
#     C1  C2  C3  C4  C5  C6  C7  C8  C9  C10
# R1  11  10  12  13  14  15  16  17  18   19
# R2  21  20  22  23  24  25  26  27  28   29
# R3  31  30  32  33  34  35  36  37  38   39
# R4  41  40  42  43  44  45  46  47  48   49
# R5  51  50  52  53  54  55  56  57  58   59
# R6  61  60  62  63  64  65  66  67  68   69

# ▶▶▶ 주의할 점...이라기 보다는 알아두면 좋은 점

print(df.loc[:, 'C4':'C7'])
#     C4  C5  C6  C7
# R1  13  14  15  16
# R2  23  24  25  26
# R3  33  34  35  36
# R4  43  44  45  46
# R5  53  54  55  56
# R6  63  64  65  66
print(df.loc[:, 'C7':'C4':-1])
#     C7  C6  C5  C4
# R1  16  15  14  13
# R2  26  25  24  23
# R3  36  35  34  33
# R4  46  45  44  43
# R5  56  55  54  53
# R6  66  65  64  63

df.loc[:, 'C4':'C7'] = df.loc[:, 'C7':'C4':-1] # 이렇게 하면 과연 C4 부터 C7까지 값이 바뀔까??

print(df) # 정답은 NO !!! 안바뀜! -> 칼럼 정렬이 값 할당 이전에 수행되어서 원래의 df 값을 바꾸지 않음...
#     C1  C2  C3  C4  C5  C6  C7  C8  C9  C10
# R1  11  10  12  13  14  15  16  17  18   19
# R2  21  20  22  23  24  25  26  27  28   29
# R3  31  30  32  33  34  35  36  37  38   39
# R4  41  40  42  43  44  45  46  47  48   49
# R5  51  50  52  53  54  55  56  57  58   59
# R6  61  60  62  63  64  65  66  67  68   69

df.loc[:, 'C4':'C7'] = df.loc[:, 'C7':'C4':-1].to_numpy() # 이렇게 원시 데이터로 값을 변경하면 바뀐다
print(df)
#     C1  C2  C3  C4  C5  C6  C7  C8  C9  C10
# R1  11  10  12  16  15  14  13  17  18   19
# R2  21  20  22  26  25  24  23  27  28   29
# R3  31  30  32  36  35  34  33  37  38   39
# R4  41  40  42  46  45  44  43  47  48   49
# R5  51  50  52  56  55  54  53  57  58   59
# R6  61  60  62  66  65  64  63  67  68   69

df.iloc[-2::-1, -3:-1:1] = 0.1234567    # 스칼라 값으로 바꾸기
print(df)
#     C1  C2  C3  C4  C5  C6  C7         C8         C9  C10
# R1  11  10  12  16  15  14  13   0.123457   0.123457   19
# R2  21  20  22  26  25  24  23   0.123457   0.123457   29
# R3  31  30  32  36  35  34  33   0.123457   0.123457   39
# R4  41  40  42  46  45  44  43   0.123457   0.123457   49
# R5  51  50  52  56  55  54  53   0.123457   0.123457   59
# R6  61  60  62  66  65  64  63  67.000000  68.000000   69


df = pd.DataFrame(
    data = {
        'C1': pd.date_range(start="20230505", end="2023-12-10", periods=10, tz="Asia/Seoul"),
        'C2': pd.period_range(start=pd.Timestamp.now(), periods=10, freq="M"),
        'C3': pd.timedelta_range(start='1 day', end='5 day', freq='10h'),
        'C4': np.nan,
        'C5': None,
    },
    index=map(lambda x : 'R'+str(x), [1,2,3,4,5,6,7,8,9,10]),
)
print(df)
#                            C1       C2              C3  C4    C5
# R1  2023-05-05 00:00:00+09:00  2024-03 1 days 00:00:00 NaN  None
# R2  2023-05-29 08:00:00+09:00  2024-04 1 days 10:00:00 NaN  None
# R3  2023-06-22 16:00:00+09:00  2024-05 1 days 20:00:00 NaN  None
# R4  2023-07-17 00:00:00+09:00  2024-06 2 days 06:00:00 NaN  None
# R5  2023-08-10 08:00:00+09:00  2024-07 2 days 16:00:00 NaN  None
# R6  2023-09-03 16:00:00+09:00  2024-08 3 days 02:00:00 NaN  None
# R7  2023-09-28 00:00:00+09:00  2024-09 3 days 12:00:00 NaN  None
# R8  2023-10-22 08:00:00+09:00  2024-10 3 days 22:00:00 NaN  None
# R9  2023-11-15 16:00:00+09:00  2024-11 4 days 08:00:00 NaN  None
# R10 2023-12-10 00:00:00+09:00  2024-12 4 days 18:00:00 NaN  None

print(df[0:-3][['C1','C3']].__repr__())
#                           C1              C3
# R1 2023-05-05 00:00:00+09:00 1 days 00:00:00
# R2 2023-05-29 08:00:00+09:00 1 days 10:00:00
# R3 2023-06-22 16:00:00+09:00 1 days 20:00:00
# R4 2023-07-17 00:00:00+09:00 2 days 06:00:00
# R5 2023-08-10 08:00:00+09:00 2 days 16:00:00
# R6 2023-09-03 16:00:00+09:00 3 days 02:00:00
# R7 2023-09-28 00:00:00+09:00 3 days 12:00:00

print(df[::-1][['C1','C2','C3','C4','C5'][::-1]].__repr__())
#        C5  C4              C3       C2                        C1
# R10  None NaN 4 days 18:00:00  2024-12 2023-12-10 00:00:00+09:00
# R9   None NaN 4 days 08:00:00  2024-11 2023-11-15 16:00:00+09:00
# R8   None NaN 3 days 22:00:00  2024-10 2023-10-22 08:00:00+09:00
# R7   None NaN 3 days 12:00:00  2024-09 2023-09-28 00:00:00+09:00
# R6   None NaN 3 days 02:00:00  2024-08 2023-09-03 16:00:00+09:00
# R5   None NaN 2 days 16:00:00  2024-07 2023-08-10 08:00:00+09:00
# R4   None NaN 2 days 06:00:00  2024-06 2023-07-17 00:00:00+09:00
# R3   None NaN 1 days 20:00:00  2024-05 2023-06-22 16:00:00+09:00
# R2   None NaN 1 days 10:00:00  2024-04 2023-05-29 08:00:00+09:00
# R1   None NaN 1 days 00:00:00  2024-03 2023-05-05 00:00:00+09:00

df.iloc[:, -1] =\
    df.iloc[:, [0]].map(\
        lambda x : 'FUTURE'\
        if x > pd.Timestamp("2023-10-01", tz="Asia/Seoul")\
        else 'PAST')
print(df)
#                            C1       C2              C3  C4      C5
# R1  2023-05-05 00:00:00+09:00  2024-03 1 days 00:00:00 NaN    PAST
# R2  2023-05-29 08:00:00+09:00  2024-04 1 days 10:00:00 NaN    PAST
# R3  2023-06-22 16:00:00+09:00  2024-05 1 days 20:00:00 NaN    PAST
# R4  2023-07-17 00:00:00+09:00  2024-06 2 days 06:00:00 NaN    PAST
# R5  2023-08-10 08:00:00+09:00  2024-07 2 days 16:00:00 NaN    PAST
# R6  2023-09-03 16:00:00+09:00  2024-08 3 days 02:00:00 NaN    PAST
# R7  2023-09-28 00:00:00+09:00  2024-09 3 days 12:00:00 NaN    PAST
# R8  2023-10-22 08:00:00+09:00  2024-10 3 days 22:00:00 NaN  FUTURE
# R9  2023-11-15 16:00:00+09:00  2024-11 4 days 08:00:00 NaN  FUTURE
# R10 2023-12-10 00:00:00+09:00  2024-12 4 days 18:00:00 NaN  FUTURE


"""
    나머지는 스킵하고 Selection by callable 부터 보자...
"""

# ==================================================================================================================================
# Selection by callable
# .loc, .iloc, [] 을 활용한 인덱싱은 모두 "callable"을 인덱서로 받을 수 있다.
# 여기서 callable은 데이터 인덱싱에 유효한 출력을 반환하면서 동시에 하나의 Series 또는 DataFrame을 받는 함수이다
# ==================================================================================================================================

df = pd.DataFrame(
    np.arange(0, -48, -1).reshape(6, 8),
    index=map(lambda a : 'R'+str(a), [1,2,3,4,5,6]),
    columns=map(lambda a : 'C'+str(a), [1,2,3,4,5,6,7,8])
)
print(df)
#     C1  C2  C3  C4  C5  C6  C7  C8
# R1   0  -1  -2  -3  -4  -5  -6  -7
# R2  -8  -9 -10 -11 -12 -13 -14 -15
# R3 -16 -17 -18 -19 -20 -21 -22 -23
# R4 -24 -25 -26 -27 -28 -29 -30 -31
# R5 -32 -33 -34 -35 -36 -37 -38 -39
# R6 -40 -41 -42 -43 -44 -45 -46 -47

print(df.loc[lambda df_obj : df_obj['C8'] > -30, :]) # 이렇게 인덱싱에 유효한 값을 리턴하는 함수
#     C1  C2  C3  C4  C5  C6  C7  C8
# R1   0  -1  -2  -3  -4  -5  -6  -7
# R2  -8  -9 -10 -11 -12 -13 -14 -15
# R3 -16 -17 -18 -19 -20 -21 -22 -23

print(df.iloc[:, lambda df_obj : [-1, -2, -5]])
#     C8  C7  C4
# R1  -7  -6  -3
# R2 -15 -14 -11
# R3 -23 -22 -19
# R4 -31 -30 -27
# R5 -39 -38 -35
# R6 -47 -46 -43


# ==================================================================================================================================
# Boolean indexing
# 또 다른 일반적인 작업은 boolean 백터를 사용하여 데이터를 필터링 하는 것이다.
# 연산자는 다음과 같다
# or 연산을 위한 |, and 연산을 위한 &, not 연산을 위한 ~
# 이 연산자들은 괄호를 사용하여 그룹화해야 한다. 
# ▶▶▶ 기본적으로 파이썬은 df['A'] > 2 & df['B'] < 3 을 df['A'] > (2 & df['B']) < 3 으로 해석한다 (연산자 우선순위)
# 반면에 원하는 평가 순서는 (df['A'] > 2) & (df['B'] < 3) 이다.
# ==================================================================================================================================

s = pd.Series(range(-3, 4))
print(s)
# 0   -3
# 1   -2
# 2   -1
# 3    0
# 4    1
# 5    2
# 6    3
# dtype: int64
print(s[(s < -1) | (s > 0.5)])
# 0   -3
# 1   -2
# 4    1
# 5    2
# 6    3
# dtype: int64
print(s[~(s < 0)])
# 3    0
# 4    1
# 5    2
# 6    3
# dtype: int64






