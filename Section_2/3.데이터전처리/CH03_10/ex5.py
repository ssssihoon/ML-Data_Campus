import pandas as pd

df = pd.DataFrame({'a': [1, 1, 3, 4, 5], 'b': [2, 3, 2, 3, 4], 'c': [3, 4, 7, 6, 4]})

df['d'] = [1, 3, 6, 4, 8]
df['e'] = 1
df['f'] = df['a'] + df['b'] - df['c']
df.drop(['d', 'e', 'f'], axis=1, inplace=True)
df = df._append({'a': 6, 'b': 7, 'c': 8}, ignore_index=True)
print(df)
