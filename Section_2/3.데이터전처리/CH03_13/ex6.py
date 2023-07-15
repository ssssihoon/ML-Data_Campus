import pandas as pd

df1 = pd.DataFrame({'ID' : [1, 2, 3, 4, 5], '성별' : ['F', 'M', 'F', 'M', 'F'], '나이' : [20, 30, 40, 25, 42]})
df2 = pd.DataFrame({'ID' : [3, 4, 5, 6, 7], '키' : [160.5, 170.3, 180.1, 142.3, 153.7], '몸무게' : [45.1, 50.3, 72.1, 38, 42]})
print(pd.merge(df2, df1, how = 'outer', on = 'ID'))
