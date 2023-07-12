import pandas as pd


a = {'company' : ['abc', '회사', 123], '직원수' : [400, 10, 6]}
df = pd.DataFrame(a)
print(df)