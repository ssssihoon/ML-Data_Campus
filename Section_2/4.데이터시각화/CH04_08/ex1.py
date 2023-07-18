import matplotlib.pyplot as plt
import seaborn as sns
sns.set(rc={'figure.figsize':(10, 5)})
import pandas as pd

df = sns.load_dataset('flights')
sns.lineplot(data = df, x = 'year', y = 'passengers', hue = "month")
plt.xticks(df['year'])
print(plt.show())