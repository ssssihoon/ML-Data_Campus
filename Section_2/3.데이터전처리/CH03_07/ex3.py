import pandas as pd

df = pd.DataFrame({'a' : [2, 3, 2, 7, 4], 'b' : [2, 1, 3, 5, 3], 'c' : [1, 1, 2, 3, 5]})

df.sort_values(by = ['a', 'b'], inplace = True)
print(df)