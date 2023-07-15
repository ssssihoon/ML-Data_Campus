import pandas as pd

df1 = pd.DataFrame({'A' : [1, 2, 3], 'B' : [11, 12, 13], 'C' : [21, 22, 23]})
df2 = pd.DataFrame({'B' : [14, 15, 16], 'A' : [4, 5, 6], 'C' : [24, 25, 26]})
print(pd.concat([df1, df2], ignore_index=True))
