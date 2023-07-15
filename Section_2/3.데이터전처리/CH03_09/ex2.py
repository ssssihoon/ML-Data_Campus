import pandas as pd

df = pd.DataFrame({'판매일' : ['5/11/21', '5/12/21', '5/13/21', '5/14/21', '5/15/21'], '판매량' : ['10', '15', '20', '25', '30'], '방문자수' : ['10','-', '17', '23', '25'], '기온' : ['24.1', '24.3', '24.8', '25', '25.4']})
df['방문자수'] = pd.to_numeric(df['방문자수'], errors='coerce')
df.fillna(0, inplace = True)
df = df.astype(({'방문자수' : 'int'}))
print(df)