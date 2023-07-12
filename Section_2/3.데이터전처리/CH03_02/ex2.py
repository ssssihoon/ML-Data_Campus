import pandas as pd
df = pd.DataFrame({'a' : [1, 2, 3], 'b' : [4, 5, 6], 'c' : [7, 8, 9]})
df.columns = ['d', 'e', 'f']
df.columns = ['디', 'e', '에프']
print(df)