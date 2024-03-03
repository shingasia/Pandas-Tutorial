import numpy as np
import pandas as pd

# ==================================================================================================================================
# SQL 스타일로 DataFrame 또는 이름있는 Series joining/merging (근데 DB 제품마다 FULL OUTER JOIN은 될 수도 있고 안 될 수도 있다)
# 여기서 등장하는 '인덱스'라는 용어는 SELECT 빠르게 하는 그 인덱스가 아니고, 그냥 행(row)를 인덱스라고 적어둔것임
# pandas.merge(
#     left,                       ▶ A DataFrame or named Series object.
#     right,                      ▶ Another DataFrame or named Series object.
#     how='inner',                ▶ {'left', 'right', 'outer', 'inner', 'cross'}, default 'inner'
#                                    left  : 왼쪽 프레임의 키를 기준으로 조인 SQL의 LEFT OUTER JOIN, 키 순서 유지
#                                    right : 오른쪽 프레임의 키를 기준으로 조인 SQL의 RIGHT OUTER JOIN,  키 순서 유지
#                                    outer : 두 프레임의 키를 합집합으로 조인 SQL의 FULL OUTER JOIN, 사전순으로 키 정렬
#                                    inner : 두 프레임의 키를 교집합으로 조인 SQL의 INNER JOIN, 왼쪽 키의 순서를 유지
#                                    cross : 두 프레임의 카티션 곱(cartesian product) 연산을 수행, 왼쪽 키의 순서를 유지
#     on=None,                    ▶ 두 프레임 모두 가지고 있는 column 또는 인덱스 레벨 이름, 기본값은 두 프레임의 중복되는 칼럼들이다
#     left_on=None,               ▶ 키로 사용할 왼쪽 DataFrame/Series의 columns 또는 인덱스 레벨, 
#                                    (칼럼 이름, 인덱스 레벨 이름, 또는 길이가 왼쪽 DataFrame/Series와 같은 배열도 가능)
#     right_on=None,
#     left_index=False,
#     right_index=False,
#     sort=False, suffixes=('_x', '_y'),
#     copy=True,
#     indicator=False,
#     validate=None               ▶ "one_to_one" or "1:1": checks if merge keys are unique in both left and right datasets. 지정된 병합 키가 좌, 우 데이터에서 유일한 값인지 체크
#                                    "one_to_many" or "1:m": checks if merge keys are unique in left dataset.                지정된 병합 키가 왼쪽 데이터에서 유일한 값인지 체크
#                                    "many_to_one" or "m:1": checks if merge keys are unique in right dataset.               지정된 병합 키가 오른쪽 데이터에서 유일한 값인지 체크
#                                    "many_to_many" or "m:m": allowed, but does not result in checks.                        체크 안 함
# )
# ==================================================================================================================================


df1 = pd.DataFrame (
    {
        "key1": np.random.choice([1,2,3,], 10),
        "key2": np.random.choice([1,2,3,], 10),
        "A": map(lambda x : "A"+str(x), range(0, 10)),
        "B": map(lambda x : "B"+str(x), range(0, 10)),
    }
)
df2 = pd.DataFrame (
    {
        "key1": np.random.choice([1,2,3,], 20),
        "key2": np.random.choice([1,2,3,], 20),
        "C": map(lambda x : "C"+str(x), range(0, 20)),
        "D": map(lambda x : "D"+str(x), range(0, 20)),
    }
)

print(df1)
#    key1  key2   A   B
# 0     2     2  A0  B0
# 1     1     2  A1  B1
# 2     1     3  A2  B2
# 3     1     3  A3  B3
# 4     3     1  A4  B4
# 5     1     3  A5  B5
# 6     2     1  A6  B6
# 7     1     2  A7  B7
# 8     1     3  A8  B8
# 9     1     2  A9  B9
print(df2)
#     key1  key2    C    D
# 0      3     2   C0   D0
# 1      3     2   C1   D1
# 2      3     3   C2   D2
# 3      1     3   C3   D3
# 4      2     3   C4   D4
# 5      2     3   C5   D5
# 6      3     3   C6   D6
# 7      3     2   C7   D7
# 8      1     1   C8   D8
# 9      2     1   C9   D9
# 10     2     2  C10  D10
# 11     1     2  C11  D11
# 12     3     1  C12  D12
# 13     1     2  C13  D13
# 14     1     3  C14  D14
# 15     2     1  C15  D15
# 16     3     2  C16  D16
# 17     2     2  C17  D17
# 18     3     3  C18  D18
# 19     1     2  C19  D19
print(
    pd.merge(
        left  = df1,
        right = df2,
        how   = 'inner',
        on = ['key1', 'key2']
    )
)
#     key1  key2   A   B    C    D
# 0      2     2  A0  B0  C10  D10
# 1      2     2  A0  B0  C17  D17
# 2      1     2  A1  B1  C11  D11
# 3      1     2  A1  B1  C13  D13
# 4      1     2  A1  B1  C19  D19
# 5      1     2  A7  B7  C11  D11
# 6      1     2  A7  B7  C13  D13
# 7      1     2  A7  B7  C19  D19
# 8      1     2  A9  B9  C11  D11
# 9      1     2  A9  B9  C13  D13
# 10     1     2  A9  B9  C19  D19
# 11     1     3  A2  B2   C3   D3
# 12     1     3  A2  B2  C14  D14
# 13     1     3  A3  B3   C3   D3
# 14     1     3  A3  B3  C14  D14
# 15     1     3  A5  B5   C3   D3
# 16     1     3  A5  B5  C14  D14
# 17     1     3  A8  B8   C3   D3
# 18     1     3  A8  B8  C14  D14
# 19     3     1  A4  B4  C12  D12
# 20     2     1  A6  B6   C9   D9
# 21     2     1  A6  B6  C15  D15
