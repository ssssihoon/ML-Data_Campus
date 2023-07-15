import pandas as pd

df = pd.DataFrame({'구매순서' : [1, 2, 3, 4, 5], 'ID' : [1, 1, 2, 4, 1], '구매월' : [1, 1, 2, 2, 3], '금액' : [1000, 1500, 2000, 3000, 4000], '수수료' : [100, 150, 200, 300, 400]})
df2 = (df.groupby(by = ['ID'])['금액'].agg([sum, len]))
(df2.reset_index(inplace=True))
print(df2)