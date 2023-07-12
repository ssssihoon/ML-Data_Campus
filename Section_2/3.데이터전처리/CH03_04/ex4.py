import pandas as pd

df = pd.DataFrame({'a' : [1, 2, 3, 1, 2, 3], 'b' : [4, 5, 6, 6, 7, 8], 'c' : [7, 8, 9, 10, 11, 12]})
a = df['a']
print(df['a','b'])