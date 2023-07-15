import pandas as pd

df = pd.DataFrame({'a' : [1, 2, 3, 4,5]})
def case_function(x):
    if x < 2:
        return '2 미만'
    elif x < 4:
        return '4 미만'
    else:
        return '4 이상'

df['b'] = df['a'].apply(case_function)
print(df)