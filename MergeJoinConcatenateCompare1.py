import numpy as np
import pandas as pd

# ==================================================================================================================================
# 객체 연결하기
# concat() 함수는 다른 차원의 인덱스(만약 있다면)에 선택적으로 설정된 로직(union 또는 intersection)을 수행하는 동안
# axis를 따라 연결 작업을 수행하는 무거운 작업을 모두 수행한다.
# 위에서 "만약 있다면"이라고 한 이유는 Series는 연결 가능한 차원(axis)가 1개만 있기 때문.... 그냥 예제를 통해 습득하자
# ==================================================================================================================================


df1 = pd.DataFrame(
    {
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    },
)

df2 = pd.DataFrame (
    {
        "A": ["A4", "A5", "A6", "A7"],
        "B": ["B4", "B5", "B6", "B7"],
        "C": ["C4", "C5", "C6", "C7"],
        "D": ["D4", "D5", "D6", "D7"],
    },
)

df3 = pd.DataFrame (
    {
        "A": ["A8", "A9", "A10", "A11"],
        "B": ["B8", "B9", "B10", "B11"],
        "C": ["C8", "C9", "C10", "C11"],
        "D": ["D8", "D9", "D10", "D11"],
    },
)

result = pd.concat([df1, df2, df3])
print(result)
#       A    B    C    D
# 0    A0   B0   C0   D0
# 1    A1   B1   C1   D1
# 2    A2   B2   C2   D2
# 3    A3   B3   C3   D3
# 4    A4   B4   C4   D4
# 5    A5   B5   C5   D5
# 6    A6   B6   C6   D6
# 7    A7   B7   C7   D7
# 8    A8   B8   C8   D8
# 9    A9   B9   C9   D9
# 10  A10  B10  C10  D10
# 11  A11  B11  C11  D11

# ==================================================================================================================================
# ▶▶▶ pandas.concat(objs, axis=0, join='outer', ignore_index=False, keys=None, levels=None, names=None, verify_integrity=False, sort=False, copy=True)
# objs         : Series 또는 DataFrame의 시퀀스 또는 매핑
#                만약 dict가 전달되면 정렬된 키가 키 인수로 사용된다 전달되지 않으면 값이 선택된다(아래 참조)
# axis         : 연결할 축(차원) 0/'index', 1/'columns' 기본은 0
# join         : 인덱스들을 처리한는 방법 'inner', 'outer' 기본은 'outer' (SQL과 다르다)
# ignore_index : boolean True이면, 연결 축의 인덱스 값을 사용하지 않겠다는 뜻이다 결과적으로 0, ..., n-1 이라는 레이블이 지정된다.
#                연결 축에 의미있는 인덱싱 정보가 없는 객체를 연결할 때 유용하다(다른 축의 인덱스 값은 join에서 여전히 존중된다)
# key          : 시퀀스, 전달된 키를 가장 바깥쪽 레벨로 하여 계층적 인덱스를 만든다
# ==================================================================================================================================

result = pd.concat([df1, df2, df3], keys=['x', 'y', 'z'])
print(result)
#        A    B    C    D
# x 0   A0   B0   C0   D0
#   1   A1   B1   C1   D1
#   2   A2   B2   C2   D2
#   3   A3   B3   C3   D3
# y 0   A4   B4   C4   D4
#   1   A5   B5   C5   D5
#   2   A6   B6   C6   D6
#   3   A7   B7   C7   D7
# z 0   A8   B8   C8   D8
#   1   A9   B9   C9   D9
#   2  A10  B10  C10  D10
#   3  A11  B11  C11  D11

print(result.loc['y'])
#     A   B   C   D
# 0  A4  B4  C4  D4
# 1  A5  B5  C5  D5
# 2  A6  B6  C6  D6
# 3  A7  B7  C7  D7
print(result.loc[('z', 3)])
# A    A11
# B    B11
# C    C11
# D    D11
# Name: (z, 3), dtype: object


# ==================================================================================================================================
# 여러 DataFrame을 함께 붙일 때 다른 축(연결 되는 축 제외)을 처리하는 방법을 선택할 수 있다.
# 다음 두 가지 방법으로 수행할 수 있다.
# 1) DataFrame 모두의 합집합(join='outer')으로 취하는 방법으로 데이터 손실이 전혀 없고 기본 옵션이다.
# 2) join='inner'를 사용한는 방법
# ==================================================================================================================================


df4 = pd.DataFrame (
    {
        "B": ["B2", "B3", "B6", "B7"],
        "D": ["D2", "D3", "D6", "D7"],
        "F": ["F2", "F3", "F6", "F7"],
    },
    index=[2, 3, 6, 7],
)
print(df1)
#     A   B   C   D
# 0  A0  B0  C0  D0
# 1  A1  B1  C1  D1
# 2  A2  B2  C2  D2
# 3  A3  B3  C3  D3
print(df4)
#     B   D   F
# 2  B2  D2  F2
# 3  B3  D3  F3
# 6  B6  D6  F6
# 7  B7  D7  F7


result = pd.concat([df1, df4], axis = 1) # axis = 'columns', join='outer' 와 같다
print(result)
#      A    B    C    D    B    D    F
# 0   A0   B0   C0   D0  NaN  NaN  NaN
# 1   A1   B1   C1   D1  NaN  NaN  NaN
# 2   A2   B2   C2   D2   B2   D2   F2
# 3   A3   B3   C3   D3   B3   D3   F3
# 6  NaN  NaN  NaN  NaN   B6   D6   F6
# 7  NaN  NaN  NaN  NaN   B7   D7   F7

result = pd.concat([df1, df4], axis = 1, join='inner') # 중복되는 라벨이 2, 3 이다
print(result)
#     A   B   C   D   B   D   F
# 2  A2  B2  C2  D2  B2  D2  F2
# 3  A3  B3  C3  D3  B3  D3  F3

result = pd.concat([df1, df4], axis = 'columns', join='outer').reindex(df1.index)
print(result)
#     A   B   C   D    B    D    F
# 0  A0  B0  C0  D0  NaN  NaN  NaN
# 1  A1  B1  C1  D1  NaN  NaN  NaN
# 2  A2  B2  C2  D2   B2   D2   F2
# 3  A3  B3  C3  D3   B3   D3   F3

result = pd.concat([df1, df4.reindex(df1.index)], axis = 1, join='outer')
print(result)
#     A   B   C   D    B    D    F
# 0  A0  B0  C0  D0  NaN  NaN  NaN
# 1  A1  B1  C1  D1  NaN  NaN  NaN
# 2  A2  B2  C2  D2   B2   D2   F2
# 3  A3  B3  C3  D3   B3   D3   F3

df1 = pd.DataFrame (
    {
        "A": map(lambda x : 'A'+str(x), range(0, 6)),
        "B": map(lambda x : 'B'+str(x), range(0, 6)),
        "C": map(lambda x : 'C'+str(x), range(0, 6)),
        "D": map(lambda x : 'D'+str(x), range(0, 6)),
        "E": map(lambda x : 'E'+str(x), range(0, 6)),
    },
    index=list('012345'),
)

df2 = pd.DataFrame (
    {
        "B": map(lambda x : 'B'+str(x), range(3, 8)),
        "D": map(lambda x : 'D'+str(x), range(3, 8)),
        "E": map(lambda x : 'E'+str(x), range(3, 8)),
        "F": map(lambda x : 'F'+str(x), range(3, 8)),
    },
    index=list('34567')
)
df3 = pd.DataFrame (
    {
        "X": map(lambda x : 'X'+str(x), range(-2, 2)),
        "Y": map(lambda x : 'Y'+str(x), range(-2, 2)),
        "Z": map(lambda x : 'Z'+str(x), range(-2, 2)),
    },
    index=range(-2, 2)
)

print(df1)
#     A   B   C   D   E
# 0  A0  B0  C0  D0  E0
# 1  A1  B1  C1  D1  E1
# 2  A2  B2  C2  D2  E2
# 3  A3  B3  C3  D3  E3
# 4  A4  B4  C4  D4  E4
# 5  A5  B5  C5  D5  E5
print(df2)
#     B   D   E   F
# 3  B3  D3  E3  F3
# 4  B4  D4  E4  F4
# 5  B5  D5  E5  F5
# 6  B6  D6  E6  F6
# 7  B7  D7  E7  F7
print(df3)
#       X    Y    Z
# -2  X-2  Y-2  Z-2
# -1  X-1  Y-1  Z-1
# 0    X0   Y0   Z0
# 1    X1   Y1   Z1
result = pd.concat([df1, df2, df3], axis = 1, join='outer')
print(result)
#       A    B    C    D    E    B    D    E    F    X    Y    Z
# 0    A0   B0   C0   D0   E0  NaN  NaN  NaN  NaN  NaN  NaN  NaN
# 1    A1   B1   C1   D1   E1  NaN  NaN  NaN  NaN  NaN  NaN  NaN
# 2    A2   B2   C2   D2   E2  NaN  NaN  NaN  NaN  NaN  NaN  NaN
# 3    A3   B3   C3   D3   E3   B3   D3   E3   F3  NaN  NaN  NaN
# 4    A4   B4   C4   D4   E4   B4   D4   E4   F4  NaN  NaN  NaN
# 5    A5   B5   C5   D5   E5   B5   D5   E5   F5  NaN  NaN  NaN
# 6   NaN  NaN  NaN  NaN  NaN   B6   D6   E6   F6  NaN  NaN  NaN
# 7   NaN  NaN  NaN  NaN  NaN   B7   D7   E7   F7  NaN  NaN  NaN
# -2  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN  X-2  Y-2  Z-2
# -1  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN  X-1  Y-1  Z-1
# 0   NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN   X0   Y0   Z0
# 1   NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN   X1   Y1   Z1
result = pd.concat([df2, df3, df1], axis = 1, join='outer')
print(result)
#       B    D    E    F    X    Y    Z    A    B    C    D    E
# 3    B3   D3   E3   F3  NaN  NaN  NaN   A3   B3   C3   D3   E3
# 4    B4   D4   E4   F4  NaN  NaN  NaN   A4   B4   C4   D4   E4
# 5    B5   D5   E5   F5  NaN  NaN  NaN   A5   B5   C5   D5   E5
# 6    B6   D6   E6   F6  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN
# 7    B7   D7   E7   F7  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN
# -2  NaN  NaN  NaN  NaN  X-2  Y-2  Z-2  NaN  NaN  NaN  NaN  NaN
# -1  NaN  NaN  NaN  NaN  X-1  Y-1  Z-1  NaN  NaN  NaN  NaN  NaN
# 0   NaN  NaN  NaN  NaN   X0   Y0   Z0  NaN  NaN  NaN  NaN  NaN
# 1   NaN  NaN  NaN  NaN   X1   Y1   Z1  NaN  NaN  NaN  NaN  NaN
# 0   NaN  NaN  NaN  NaN  NaN  NaN  NaN   A0   B0   C0   D0   E0
# 1   NaN  NaN  NaN  NaN  NaN  NaN  NaN   A1   B1   C1   D1   E1
# 2   NaN  NaN  NaN  NaN  NaN  NaN  NaN   A2   B2   C2   D2   E2
result = pd.concat([df2, df1, df2], axis = 1, join='outer')
print(result)
#      B    D    E    F    A    B    C    D    E    B    D    E    F
# 3   B3   D3   E3   F3   A3   B3   C3   D3   E3   B3   D3   E3   F3
# 4   B4   D4   E4   F4   A4   B4   C4   D4   E4   B4   D4   E4   F4
# 5   B5   D5   E5   F5   A5   B5   C5   D5   E5   B5   D5   E5   F5
# 6   B6   D6   E6   F6  NaN  NaN  NaN  NaN  NaN   B6   D6   E6   F6
# 7   B7   D7   E7   F7  NaN  NaN  NaN  NaN  NaN   B7   D7   E7   F7
# 0  NaN  NaN  NaN  NaN   A0   B0   C0   D0   E0  NaN  NaN  NaN  NaN
# 1  NaN  NaN  NaN  NaN   A1   B1   C1   D1   E1  NaN  NaN  NaN  NaN
# 2  NaN  NaN  NaN  NaN   A2   B2   C2   D2   E2  NaN  NaN  NaN  NaN
result = pd.concat([df3, df1, df2], axis = 1, join = 'outer')
print(result)
#       X    Y    Z    A    B    C    D    E    B    D    E    F
# -2  X-2  Y-2  Z-2  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN
# -1  X-1  Y-1  Z-1  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN
# 0    X0   Y0   Z0  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN
# 1    X1   Y1   Z1  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN
# 0   NaN  NaN  NaN   A0   B0   C0   D0   E0  NaN  NaN  NaN  NaN
# 1   NaN  NaN  NaN   A1   B1   C1   D1   E1  NaN  NaN  NaN  NaN
# 2   NaN  NaN  NaN   A2   B2   C2   D2   E2  NaN  NaN  NaN  NaN
# 3   NaN  NaN  NaN   A3   B3   C3   D3   E3   B3   D3   E3   F3
# 4   NaN  NaN  NaN   A4   B4   C4   D4   E4   B4   D4   E4   F4
# 5   NaN  NaN  NaN   A5   B5   C5   D5   E5   B5   D5   E5   F5
# 6   NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN   B6   D6   E6   F6
# 7   NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN   B7   D7   E7   F7


