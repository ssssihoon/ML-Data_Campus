import pandas as pd
import numpy as np

df = pd.DataFrame({'a' : [1, 2, 3, 4, 5], 'b' : [2, 3, np.nan,3 ,4], 'c' : [3, 4, 7, 6, 4]})
print(df.isnull())
print(df.isnull().sum())