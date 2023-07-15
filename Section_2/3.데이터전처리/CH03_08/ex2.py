import pandas as pd
import numpy as np

df = pd.DataFrame({'a': [1, 1, 3, 4, np.nan], 'b': [2, 3, np.nan, np.nan, 4], 'c': [np.nan, 4, 1, 1, 4]})
df.fillna(df.mean(), inplace=True)
print(df)
