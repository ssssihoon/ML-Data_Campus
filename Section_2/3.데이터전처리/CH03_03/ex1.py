import pandas as pd
import copy
df = pd.DataFrame({'a' : [1, 2, 3], 'b' : [4, 5, 6], 'c' : [7, 8, 9]})
df2 = copy.deepcopy(df)
df.columns = ['d', 'e', 'f']
df.columns = ['디', 'e', '에프']
print(df)
print(df2)