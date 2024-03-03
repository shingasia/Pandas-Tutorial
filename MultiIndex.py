import numpy as np
import pandas as pd



# ==================================================================================================================================
# MultiIndex 만들기 (계층적 인덱스를 만드는 기능)
# MultiIndex는 값이 유니크한(중복X) 튜플의 배열로 생각할 수 있다. 다음과 같은 메서드로 만들 수 있다.
# MultiIndex.from_arrays()
# MultiIndex.from_tuples()
# MultiIndex.from_product()
# MultiIndex.from_frame()
# ==================================================================================================================================


ingredient = [
    ['Vegetable', 'Vegetable', 'Vegetable', 'Vegetable', 'Vegetable', 'Fruit', 'Fruit', 'Fruit', 'Fruit'],
    ['Paprika', 'Pumpkin', 'Onion', 'Garlic', 'Mushroom', 'Lime', 'Peach', 'Blueberry', 'Avocado'],
]

tuples_ingredient = list(zip(*ingredient))
print(tuples_ingredient) # 튜플로 이루어진 리스트
# [('Vegetable', 'Paprika'), ('Vegetable', 'Pumpkin'), ('Vegetable', 'Onion'), ('Vegetable', 'Garlic'), ('Vegetable', 'Mushroom'), ('Fruit', 'Lime'), ('Fruit', 'Peach'), ('Fruit', 'Blueberry'), ('Fruit', 'Avocado')]
index_ingredient = pd.MultiIndex.from_tuples(tuples_ingredient, names=['first', 'second'])
print(index_ingredient)
# MultiIndex([('Vegetable',   'Paprika'),
#             ('Vegetable',   'Pumpkin'),
#             ('Vegetable',     'Onion'),
#             ('Vegetable',    'Garlic'),
#             ('Vegetable',  'Mushroom'),
#             (    'Fruit',      'Lime'),
#             (    'Fruit',     'Peach'),
#             (    'Fruit', 'Blueberry'),
#             (    'Fruit',   'Avocado')],
#            names=['first', 'second'])


s = pd.Series(np.random.randn(9), index=index_ingredient)
print(s)
# first      second   
# Vegetable  Paprika      0.291560
#            Pumpkin     -0.248265
#            Onion       -1.591213
#            Garlic      -0.391712
#            Mushroom     0.662608
# Fruit      Lime        -0.077690
#            Peach        0.852715
#            Blueberry   -0.686671
#            Avocado      2.110510


iterables = [["bar", "baz", "foo", "qux"], ["one", "two"]]
print(pd.MultiIndex.from_product(iterables, names=['first', 'second']))
# MultiIndex([('bar', 'one'),
#             ('bar', 'two'),
#             ('baz', 'one'),
#             ('baz', 'two'),
#             ('foo', 'one'),
#             ('foo', 'two'),
#             ('qux', 'one'),
#             ('qux', 'two')],
#            names=['first', 'second'])


df = pd.DataFrame(
    [["bar", "one"], ["bar", "two"], ["foo", "one"], ["foo", "two"]],
    columns=["first", "second"],
)
print(df)
#   first second
# 0   bar    one
# 1   bar    two
# 2   foo    one
# 3   foo    two
print(pd.MultiIndex.from_frame(df))
# MultiIndex([('bar', 'one'),
#             ('bar', 'two'),
#             ('foo', 'one'),
#             ('foo', 'two')],
#            names=['first', 'second'])



goods = [
    ['카테고리']*5 + ['수량']*3 + ['날짜']*2,
    ['채소', '과일', '쌀/잡곡', '수산물', '음료/커피/차']+['재고수량', '판매수량', '반품수량']+['발주요청', '입고'],
]

print(pd.MultiIndex.from_tuples(tuple(zip(*goods))))
# MultiIndex([('카테고리',      '채소'),
#             ('카테고리',      '과일'),
#             ('카테고리',    '쌀/잡곡'),
#             ('카테고리',     '수산물'),
#             ('카테고리', '음료/커피/차'),
#             (  '수량',    '재고수량'),
#             (  '수량',    '판매수량'),
#             (  '수량',    '반품수량'),
#             (  '날짜',    '발주요청'),
#             (  '날짜',      '입고')],
#            )

df = pd.DataFrame(
    [
        [1100, 2100, 3100, 4100, 5100]+[9000, 6800, 25]+[np.nan, np.nan],
        [1200, 2200, 3200, 4200, 5200]+[10000, 7500, 56]+[np.nan, np.nan],
        [1300, 2300, 3300, 4300, 5300]+[8760, 5020, 23]+[np.nan, np.nan],
    ],
    columns=goods,
    index=['마트1', '마트2', '마트3']
)

print(df)
#                                           카테고리                          수량           날짜
#        채소    과일  쌀/잡곡   수산물 음료/커피/차   재고수량  판매수량 반품수량 발주요청  입고
# 마트1  1100    2100     3100     4100         5100       9000      6800       25      NaN   NaN
# 마트2  1200    2200     3200     4200         5200      10000      7500       56      NaN   NaN
# 마트3  1300    2300     3300     4300         5300       8760      5020       23      NaN   NaN

df[('날짜', '발주요청')] = pd.date_range('20190203', periods=3)
df[('날짜', '입고')] = pd.date_range(start='2019-02-05', end='2019-02-20', periods=3)
print(df)
#                                           카테고리                          수량                                 날짜
#        채소    과일  쌀/잡곡   수산물 음료/커피/차   재고수량  판매수량 반품수량       발주요청                  입고
# 마트1  1100    2100     3100     4100         5100       9000      6800       25     2019-02-03   2019-02-05 00:00:00
# 마트2  1200    2200     3200     4200         5200      10000      7500       56     2019-02-04   2019-02-12 12:00:00
# 마트3  1300    2300     3300     4300         5300       8760      5020       23     2019-02-05   2019-02-20 00:00:00

print(df[('수량', '반품수량')])
# 마트1    25
# 마트2    56
# 마트3    23
# Name: (수량, 반품수량), dtype: int64



print(df.loc[['마트3', '마트1'],:])
#                                           카테고리                          수량                                 날짜
#        채소    과일  쌀/잡곡   수산물 음료/커피/차   재고수량  판매수량 반품수량       발주요청                  입고
# 마트3  1300    2300     3300     4300         5300       8760      5020       23     2019-02-05   2019-02-20 00:00:00
# 마트1  1100    2100     3100     4100         5100       9000      6800       25     2019-02-03   2019-02-05 00:00:00

print(df.loc['마트2', ('카테고리', '음료/커피/차')]) # 5200




