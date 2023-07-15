import pandas as pd

df = pd.DataFrame({'a' : [1, 2, 3, 4,5]})
df['b'] = 0
a = df[df['a'] < 2]
df['b'][a.index] = '2미만'
a = df[(df['a'] >= 2)&(df['a'] < 4)]
df['b'][a.index] = '4미만'
a = df[(df['a'] >= 4)]
df['b'][a.index] = '4이상'
print(df)