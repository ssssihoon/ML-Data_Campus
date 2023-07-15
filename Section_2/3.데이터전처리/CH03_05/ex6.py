import pandas as pd

index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'g', 'h', 'i']
df = pd.DataFrame({'a' : [i for i in range(1, 11)], 'b' : [i for i in range(11, 21)], 'c' : [i for i in range(21, 31)]}, index = index)
print(df.iloc[:5, [0, 2]])