import pandas as pd
import numpy as np

a = {'company' : ['abc', '회사', 123], '직원수' : [400, 10, 6], '위치' : ['Seoul', np.NaN , 'Busan']}
# NONE값을 사용하기 위해 numpy를 이용 (np)
df1 = pd.DataFrame(a)
print(df1)
