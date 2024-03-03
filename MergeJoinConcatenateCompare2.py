import numpy as np
import pandas as pd


# ==================================================================================================================================
# ingore_index = True 로 하면 모든 이름이 삭제된다.
# ==================================================================================================================================

df1 = pd.DataFrame (
    np.arange(0, 6 *4).reshape(6, 4),
    index = map(lambda x : 'R'+str(x), range(-5, 1)),
    columns = ['A', 'B', 'C', 'D']
)

df2 = pd.DataFrame (
    np.arange(12, 32).reshape(5, 4),
    index = map(lambda x : 'R'+str(x), [-3, -2, -1, 0, 1]),
    columns = ['A', 'B', 'C', 'D']
)
df3 = pd.DataFrame (
    np.arange(0 + 24, 4 * 4 + 24).reshape(4, 4),
    index = map(lambda x : 'R'+str(x), range(0, 4)),
    columns = ['A', 'B', 'C', 'D']
)
# ==================================================================================================================================
# concat 개념을 더 확실하게 하자
# df1, df2는 'R-3' ~ 'R0' 까지 인덱스는 같지만 들어있는 값이 다르고,
# df2, df3는 'R0' ~ 'R1' 까지 인덱스 이름, 들어있는 값 모두 같다
# ▶ join 할 때 이름은 앞에있는 것과 이름이 중복되어도 axis 방향으로 무조건 붙인다
# ==================================================================================================================================
print(df1)
#       A   B   C   D
# R-5   0   1   2   3
# R-4   4   5   6   7
# R-3   8   9  10  11
# R-2  12  13  14  15
# R-1  16  17  18  19
# R0   20  21  22  23
print(df2)
#       A   B   C   D
# R-3  12  13  14  15
# R-2  16  17  18  19
# R-1  20  21  22  23
# R0   24  25  26  27
# R1   28  29  30  31
print(df3)
#      A   B   C   D
# R0  24  25  26  27
# R1  28  29  30  31
# R2  32  33  34  35
# R3  36  37  38  39

print(pd.concat([df1, df2, df3], axis = 'columns', join = 'outer'))
#         A     B     C     D     A     B     C     D     A     B     C     D
# R-5   0.0   1.0   2.0   3.0   NaN   NaN   NaN   NaN   NaN   NaN   NaN   NaN
# R-4   4.0   5.0   6.0   7.0   NaN   NaN   NaN   NaN   NaN   NaN   NaN   NaN
# R-3   8.0   9.0  10.0  11.0  12.0  13.0  14.0  15.0   NaN   NaN   NaN   NaN
# R-2  12.0  13.0  14.0  15.0  16.0  17.0  18.0  19.0   NaN   NaN   NaN   NaN
# R-1  16.0  17.0  18.0  19.0  20.0  21.0  22.0  23.0   NaN   NaN   NaN   NaN
# R0   20.0  21.0  22.0  23.0  24.0  25.0  26.0  27.0  24.0  25.0  26.0  27.0
# R1    NaN   NaN   NaN   NaN  28.0  29.0  30.0  31.0  28.0  29.0  30.0  31.0
# R2    NaN   NaN   NaN   NaN   NaN   NaN   NaN   NaN  32.0  33.0  34.0  35.0
# R3    NaN   NaN   NaN   NaN   NaN   NaN   NaN   NaN  36.0  37.0  38.0  39.0

print(pd.concat([df1, df2, df3], axis = 'columns', join = 'outer', ignore_index = True)) # ignore_index = True 이면 연결 axis의 인덱스 값을 사용X
#        0     1     2     3     4     5     6     7     8     9     10    11
# R-5   0.0   1.0   2.0   3.0   NaN   NaN   NaN   NaN   NaN   NaN   NaN   NaN
# R-4   4.0   5.0   6.0   7.0   NaN   NaN   NaN   NaN   NaN   NaN   NaN   NaN
# R-3   8.0   9.0  10.0  11.0  12.0  13.0  14.0  15.0   NaN   NaN   NaN   NaN
# R-2  12.0  13.0  14.0  15.0  16.0  17.0  18.0  19.0   NaN   NaN   NaN   NaN
# R-1  16.0  17.0  18.0  19.0  20.0  21.0  22.0  23.0   NaN   NaN   NaN   NaN
# R0   20.0  21.0  22.0  23.0  24.0  25.0  26.0  27.0  24.0  25.0  26.0  27.0
# R1    NaN   NaN   NaN   NaN  28.0  29.0  30.0  31.0  28.0  29.0  30.0  31.0
# R2    NaN   NaN   NaN   NaN   NaN   NaN   NaN   NaN  32.0  33.0  34.0  35.0
# R3    NaN   NaN   NaN   NaN   NaN   NaN   NaN   NaN  36.0  37.0  38.0  39.0

print(pd.concat([df1, df2, df3], axis = 1, join = 'inner')) # 중복되는 라벨이 'R0' 뿐이다
#      A   B   C   D   A   B   C   D   A   B   C   D
# R0  20  21  22  23  24  25  26  27  24  25  26  27

print(pd.concat([df1, df2, df1], axis = 1, join = 'outer'))
#         A     B     C     D     A     B     C     D     A     B     C     D
# R-5   0.0   1.0   2.0   3.0   NaN   NaN   NaN   NaN   0.0   1.0   2.0   3.0
# R-4   4.0   5.0   6.0   7.0   NaN   NaN   NaN   NaN   4.0   5.0   6.0   7.0
# R-3   8.0   9.0  10.0  11.0  12.0  13.0  14.0  15.0   8.0   9.0  10.0  11.0
# R-2  12.0  13.0  14.0  15.0  16.0  17.0  18.0  19.0  12.0  13.0  14.0  15.0
# R-1  16.0  17.0  18.0  19.0  20.0  21.0  22.0  23.0  16.0  17.0  18.0  19.0
# R0   20.0  21.0  22.0  23.0  24.0  25.0  26.0  27.0  20.0  21.0  22.0  23.0
# R1    NaN   NaN   NaN   NaN  28.0  29.0  30.0  31.0   NaN   NaN   NaN   NaN
print(pd.concat([df1, df2, df1], axis = 1, join = 'inner')) # 중복되는 라벨이 'R-3' ~ 'R0' 이다
#       A   B   C   D   A   B   C   D   A   B   C   D
# R-3   8   9  10  11  12  13  14  15   8   9  10  11
# R-2  12  13  14  15  16  17  18  19  12  13  14  15
# R-1  16  17  18  19  20  21  22  23  16  17  18  19
# R0   20  21  22  23  24  25  26  27  20  21  22  23


print(pd.concat([df1, df2, df3, df2], axis = 0, join = 'outer', keys=['OUT1', 'OUT2', 'OUT3']))
#            A   B   C   D
# OUT1 R-5   0   1   2   3
#      R-4   4   5   6   7
#      R-3   8   9  10  11
#      R-2  12  13  14  15
#      R-1  16  17  18  19
#      R0   20  21  22  23
# OUT2 R-3  12  13  14  15
#      R-2  16  17  18  19
#      R-1  20  21  22  23
#      R0   24  25  26  27
#      R1   28  29  30  31
# OUT3 R0   24  25  26  27
#      R1   28  29  30  31
#      R2   32  33  34  35
#      R3   36  37  38  39

print(pd.concat([df1, df2, df3, df2], axis = 0, join = 'outer', keys=['OUT1', 'OUT2', 'OUT3', 'OUT4']))
#            A   B   C   D
# OUT1 R-5   0   1   2   3
#      R-4   4   5   6   7
#      R-3   8   9  10  11
#      R-2  12  13  14  15
#      R-1  16  17  18  19
#      R0   20  21  22  23
# OUT2 R-3  12  13  14  15
#      R-2  16  17  18  19
#      R-1  20  21  22  23
#      R0   24  25  26  27
#      R1   28  29  30  31
# OUT3 R0   24  25  26  27
#      R1   28  29  30  31
#      R2   32  33  34  35
#      R3   36  37  38  39
# OUT4 R-3  12  13  14  15
#      R-2  16  17  18  19
#      R-1  20  21  22  23
#      R0   24  25  26  27
#      R1   28  29  30  31


print(len(df1.index) + len(df2.index) + len(df3.index)) # 15
print(
    pd.concat(
        [df1, df2, df3, df3] # 4개 ==> 'ROW0' ~ 'ROW3' 까지 라벨링 된다
        , axis = 0
        , join = 'outer'
        , keys=(
            map(lambda x : 'ROW'+str(x), range(len(df1.index) + len(df2.index) + len(df3.index)))
        )
    )
)
#            A   B   C   D
# ROW0 R-5   0   1   2   3
#      R-4   4   5   6   7
#      R-3   8   9  10  11
#      R-2  12  13  14  15
#      R-1  16  17  18  19
#      R0   20  21  22  23
# ROW1 R-3  12  13  14  15
#      R-2  16  17  18  19
#      R-1  20  21  22  23
#      R0   24  25  26  27
#      R1   28  29  30  31
# ROW2 R0   24  25  26  27
#      R1   28  29  30  31
#      R2   32  33  34  35
#      R3   36  37  38  39
# ROW3 R0   24  25  26  27
#      R1   28  29  30  31
#      R2   32  33  34  35
#      R3   36  37  38  39



