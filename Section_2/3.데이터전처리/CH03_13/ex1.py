import pandas as pd

df1 = pd.DataFrame({'ID' : [1, 2, 3], '성별' : ['F', 'M', 'F'], '나이' : [20, 30, 40]})
df2 = pd.DataFrame({'ID' : [1, 2, 3], '키' : [160.5, 170.3, 180.1], '몸무게' : [45.1, 50.3, 72.1]})
print(pd.concat([df1, df2], axis = 1))
