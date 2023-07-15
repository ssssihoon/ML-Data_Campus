import pandas as pd

df = pd.DataFrame({'a' : [1, 2, 3, 4,5]})
def case_function(x):
    if x == 1:
        return 'one'
    elif x == 2:
        return 'two'
    elif x == 3:
        return 'three'
    elif x == 4:
        return 'four'
    elif x == 5:
        return 'five'

df['d'] = df['a'].apply(case_function)

a = {1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five'}
df['e'] = df['a'].map(a)
print(df)