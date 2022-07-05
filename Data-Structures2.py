import numpy as np
import pandas as pd

# ================================================================================================================================
# DataFrame
# DataFrame은 2차원의 라벨이 지정된 데이터구조이다. DataFrame의 각각의 칼럼은 서로다른 타입의 데이터를 가질 수 있다.
# DataFrame은 다양한 종류의 입력으로 만들 수 있다.
# 1) Dict of 1D ndarrays, lists, dicts, or Series
# 2) 2-D numpy.ndarray
# 3) Numpy의 Structured arrays
# 4) Series
# 5) 또다른 DataFrame
# ================================================================================================================================

# ================================================================================================================================
# DataFrame을 만들때 데이터와 함께 index(row lables) 및 columns(column labels) 인자값을 선택적으로 전달할 수 있다
# index와 columns을 각각 선택적으로 전달하면 결과 DataFrame의 index와 columns이 지정된 것을 보장한다
# 그래서 index가 지정된 Series의 딕셔너리(dict)를 전달하면 index와 매칭되지 않는 데이터는 버려진다.
# ================================================================================================================================


# ================================================================================================================================
# From dict of Series or dicts
# ================================================================================================================================
d = {
    "one":pd.Series([1.0, 2.0, 3.0], index=['a', 'b', 'c']),
    "two":pd.Series([1.0, 2.0, 3.0, 4.0], index=['a', 'b', 'c', 'd'])
}

df = pd.DataFrame(d)
print(df)
#    one  two
# a  1.0  1.0
# b  2.0  2.0
# c  3.0  3.0
# d  NaN  4.0

df = pd.DataFrame(d, index=['d', 'b', 'a', 'e'])
print(df)
#    one  two
# d  NaN  4.0
# b  2.0  2.0
# a  1.0  1.0
# e  NaN  NaN

df = pd.DataFrame(d, index=['d', 'b', 'a'], columns=['one', 'two', 'three'])
print(df)
#    one  two three
# d  NaN  4.0   NaN
# b  2.0  2.0   NaN
# a  1.0  1.0   NaN

print(np.nan is df.iloc[0, 2])       # True
print(np.isnan(df.at['d', 'three'])) # True
print(f'np.nan ==> {np.nan}, df.iloc[0, 2] ==> {df.iloc[0, 2]}') # np.nan ==> nan, df.iloc[0, 2] ==> nan

# 행과 열의 레이블을 각각 index, columns 속성으로 접근할 수 있다.
print(repr(df.index))   # Index(['d', 'b', 'a'], dtype='object')
print(repr(df.columns)) # Index(['one', 'two', 'three'], dtype='object')

# ================================================================================================================================
# From dict of ndarrays / lists
# ================================================================================================================================
d = {
    "one": [1.0, 2.0, 3.0, 4.0],
    "two": [4.0, 3.0, 2.0, 1.0]
}
df = pd.DataFrame(d)
print(df)
#    one  two
# 0  1.0  4.0
# 1  2.0  3.0
# 2  3.0  2.0
# 3  4.0  1.0

df = pd.DataFrame(d, index=["A", "B", "C", "D"])
print(df)
#    one  two
# A  1.0  4.0
# B  2.0  3.0
# C  3.0  2.0
# D  4.0  1.0

data = np.zeros((2,), dtype=[("A", "i4"), ("B", "f4"), ("C", "a10")])
print(data.__repr__())
# array([(0, 0., b''), (0, 0., b'')],
#       dtype=[('A', '<i4'), ('B', '<f4'), ('C', 'S10')])

data[:] = [(1, 2.0, "Hello"), (2, 3.0, "World")]

print(pd.DataFrame(data, index=['first', 'second']))
#         A    B         C
# first   1  2.0  b'Hello'
# second  2  3.0  b'World'
print(pd.DataFrame(data, columns=['C', 'A', 'B']))
#           C  A    B
# 0  b'Hello'  1  2.0
# 1  b'World'  2  3.0

# ================================================================================================================================
# From a list of dicts
# ================================================================================================================================
data = [{"A": 1, "B":2}, {"A":3, "B":4, "C":5}, {"A":10, "B":20, "D":100, "C":30}]

print(pd.DataFrame(data))
#     A   B     C      D
# 0   1   2   NaN    NaN
# 1   3   4   5.0    NaN
# 2  10  20  30.0  100.0

print(pd.DataFrame(data, index=["Row1", "Row2", "Row3"])) # index로 넘겨주는 리스트는 data의 row 개수와 일치해야 한다 안그러면 Error
#        A   B     C      D
# Row1   1   2   NaN    NaN
# Row2   3   4   5.0    NaN
# Row3  10  20  30.0  100.0

print(pd.DataFrame(data, columns=['A', 'B', 'C', 'D', 'E'])) # column은 넘겨준 data보다 많으면 NaN으로 
#     A   B     C      D   E
# 0   1   2   NaN    NaN NaN
# 1   3   4   5.0    NaN NaN
# 2  10  20  30.0  100.0 NaN


# ================================================================================================================================
# From a dict of tuples
# ================================================================================================================================
data = pd.DataFrame(
    {
        ("a", "b"): {("A", "B"):1, ("A", "C"):2},
        ("a", "a"): {("A", "C"):3, ("A", "B"):4},
        ("a", "c"): {("A", "B"):5, ("A", "C"):6},
        ("b", "a"): {("A", "C"):7, ("A", "B"):8},
        ("b", "b"): {("A", "D"):9, ("A", "B"):10},
        ("a", "d"): {("A", "C"):11, ("A", "D"):12, ("A", "B"):13}
    }
)

print(data)
#        a              b         a
#        b    a    c    a     b   d
# A B  1.0  4.0  5.0  8.0  10.0  13
#   C  2.0  3.0  6.0  7.0   NaN  11
#   D  NaN  NaN  NaN  NaN   9.0  12
print(repr(data.columns))
# MultiIndex([('a', 'b'),
#             ('a', 'a'),
#             ('a', 'c'),
#             ('b', 'a'),
#             ('b', 'b'),
#             ('a', 'd')])
print(repr(data.index))
# MultiIndex([('A', 'B'),
#             ('A', 'C'),
#             ('A', 'D')])

row_list = pd.MultiIndex.from_tuples([
        ('발주1', '상품1'),('발주1', '상품2'),('발주1', '상품3'),
        ('발주2', '상품1'),('발주2', '상품2'),('발주2', '상품3'),('발주2', '상품4'),
])
col_list = pd.MultiIndex.from_tuples([
    ('상품코드', '상품코드'), ('상품명', '상품명'),
    ('수량', '구매입고'), ('수량', '주문출고'), ('수량', '반품입고'),
    ('가격', '매입원가'), ('가격', '공급가격'), ('가격', '판매가격'), ('가격', '적립포인트')
])
order_list = [
    ['G0001', 'CJ 햇반 205g X 36개입', 1000, 450, 5, 24700, 28800, 33720, 1250],
    ['G0002', '오뚜기 3분 카레 약간매운맛 200g X 24개입', 590, 300, 2, 17510, 19580, 22320, 900],
    ['G0003', '농심 올리브 짜파게티 40개', 2500, 2247, 2, 23200, 25190, 28410, 1020],
    ['G0005', '맥심 화이트골드 커피믹스 11.7g x 320p', 730, 210, 10, 30040, 32090, 37500, 2100],
    ['G0006', '빙그레 바나나맛우유 240ml X 8개입', 3400, 7500, 9030, 400],
    ['G0007', '비비고 순살 고등어구이', 1005, 601, 30, 5100, 7380, 9140, 860],
    ['G0008', '해찬들 재래식 된장', 1500, 1300, 14, 3400, 5210, 7600, 1030]
]
df = pd.DataFrame(order_list, row_list, col_list)
print(df) # 예쁘게 출력이 안된다...
#           상품코드                          상품명    수량                 가격
#           상품코드                          상품명  구매입고  주문출고  반품입고   매입원가     공급가격     판매가격   적립포인트
# 발주1 상품1  G0001            CJ 햇반 205g X 36개입  1000   450     5  24700  28800.0  33720.0  1250.0
#     상품2  G0002  오뚜기 3분 카레 약간매운맛 200g X 24개입   590   300     2  17510  19580.0  22320.0   900.0
#     상품3  G0003              농심 올리브 짜파게티 40개  2500  2247     2  23200  25190.0  28410.0  1020.0
# 발주2 상품1  G0005   맥심 화이트골드 커피믹스 11.7g x 320p   730   210    10  30040  32090.0  37500.0  2100.0
#     상품2  G0006       빙그레 바나나맛우유 240ml X 8개입  3400  7500  9030    400      NaN      NaN     NaN
#     상품3  G0007                 비비고 순살 고등어구이  1005   601    30   5100   7380.0   9140.0   860.0
#     상품4  G0008                   해찬들 재래식 된장  1500  1300    14   3400   5210.0   7600.0  1030.0

print(df.loc[:, ['가격']])
#             가격
#           매입원가     공급가격     판매가격   적립포인트
# 발주1 상품1  24700  28800.0  33720.0  1250.0
#     상품2  17510  19580.0  22320.0   900.0
#     상품3  23200  25190.0  28410.0  1020.0
# 발주2 상품1  30040  32090.0  37500.0  2100.0
#     상품2    400      NaN      NaN     NaN
#     상품3   5100   7380.0   9140.0   860.0
#     상품4   3400   5210.0   7600.0  1030.0
print(df.loc["발주2", "상품명"])
#                              상품명
# 상품1            CJ 햇반 205g X 36개입
# 상품2  오뚜기 3분 카레 약간매운맛 200g X 24개입
# 상품3              농심 올리브 짜파게티 40개

# ================================================================================================================================
# Column selection, addition, deletion (칼럼단위 연산)
# ================================================================================================================================
df = pd.DataFrame(
    {
        "one" : [1, 2, 3],
        "two" : [1, 2, 3],
    }
    , index=['A', 'B', 'C']
)
print(df)
#    one  two
# A    1    1
# B    2    2
# C    3    3
df['three'] = df['one'] * df['two']
print(df)
#    one  two  three
# A    1    1      1
# B    2    2      4
# C    3    3      9
df['flag'] = df['three'] > 5
print(df)
#    one  two  three   flag
# A    1    1      1  False
# B    2    2      4  False
# C    3    3      9   True
del df['two']
print(df)
#    one  three   flag
# A    1      1  False
# B    2      4  False
# C    3      9   True

# ▶▶▶ 스칼라 값을 대입하면 해당 칼럼을 그 값으로 채운다
df['foo'] = 'bar'
print(df)
#    one  three   flag  foo
# A    1      1  False  bar
# B    2      4  False  bar
# C    3      9   True  bar

# ▶▶▶ 1 행을 추가한다
df.loc['D', :] = [4, 16, True, 'bar']
print(df)
#    one  three   flag  foo
# A  1.0    1.0  False  bar
# B  2.0    4.0  False  bar
# C  3.0    9.0   True  bar
# D  4.0   16.0   True  bar

# ▶▶▶ list로 형변환 안하면 순서 뒤집히는게 안된다..
df['one_trunc'] = list(df['one'])[::-1]
print(df)
#    one  three   flag  foo  one_trunc
# A  1.0    1.0  False  bar        4.0
# B  2.0    4.0  False  bar        3.0
# C  3.0    9.0   True  bar        2.0
# D  4.0   16.0   True  bar        1.0
df['one_trunc'] = df['one'][:2]
print(df)
#    one  three   flag  foo  one_trunc
# A  1.0    1.0  False  bar        1.0
# B  2.0    4.0  False  bar        2.0
# C  3.0    9.0   True  bar        NaN
# D  4.0   16.0   True  bar        NaN

# ▶▶▶ 기본적으로 칼럼은 가장 끝에 삽입된다 insert 함수로 특정한 위치에 칼럼을 삽입할 수 있다
df.insert(1, "two", -df['one'])
print(df)
#    one  two  three   flag  foo  one_trunc
# A  1.0 -1.0    1.0  False  bar        1.0
# B  2.0 -2.0    4.0  False  bar        2.0
# C  3.0 -3.0    9.0   True  bar        NaN
# D  4.0 -4.0   16.0   True  bar        NaN
