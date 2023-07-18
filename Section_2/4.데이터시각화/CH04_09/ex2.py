import matplotlib.pyplot as plt
import seaborn as sns
sns.set(rc={'figure.figsize':(10, 5)})
import pandas as pd

df = sns.load_dataset('flights')
df1 = df.pivot_table(index = 'month', columns= 'year', values= 'passengers')
sns.heatmap(df1, cmap="Blues", annot= True)


fig, (ax, cbar_ax) = plt.subplots(2)
# fig는 도화지
# ax는 데이터
ax = sns.heatmap(df1, ax = ax, cbar_ax = cbar_ax, cbar_kws={"orientation" : "horizontal"})

print(plt.show())