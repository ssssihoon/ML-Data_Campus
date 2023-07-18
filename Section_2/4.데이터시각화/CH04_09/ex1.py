import matplotlib.pyplot as plt
import seaborn as sns
sns.set(rc={'figure.figsize':(10, 5)})
import pandas as pd

df = sns.load_dataset('flights')
df1 = df.pivot_table(index = 'month', columns= 'year', values= 'passengers')
sns.heatmap(df1, cmap="Blues", annot= True)
print(plt.show())