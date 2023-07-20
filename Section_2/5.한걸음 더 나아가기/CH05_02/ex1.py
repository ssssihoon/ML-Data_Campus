import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = sns.load_dataset('titanic')
train_df = df[:800]
test_df = df[800:]

df1 = train_df[['age', 'survived']].groupby(['age'], as_index=False).mean().sort_values(by='survived', ascending=False)
a = sns.FacetGrid(train_df, col='survived', row = 'pclass')
a.map(plt.hist, 'age', bins = 20)
print(plt.show())