import pandas as pd

df = pd.DataFrame({'a' : [i for i in range(1, 11)], 'b' : [i for i in range(11, 21)], 'c' : [i for i in range(21, 31)]})
print(df[(df['a'] <= 3) | (df['a'] >= 7)])