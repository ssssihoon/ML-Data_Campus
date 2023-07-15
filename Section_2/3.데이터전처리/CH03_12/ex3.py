import pandas as pd

df1 = pd.DataFrame({'A' : [1, 2, 3], 'B' : [11, 12, 13], 'C' : [21, 22, 23], 'D' : [31, 32, 33]})
df2 = pd.DataFrame({'A' : [4, 5, 6], 'B' : [14, 15, 16], 'C' : [24, 25, 26], 'E' : [41, 42, 43]})
print(pd.concat([df2, df1], join = 'inner', ignore_index = True))
