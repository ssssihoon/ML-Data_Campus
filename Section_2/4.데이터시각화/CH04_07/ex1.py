import matplotlib.pyplot as plt
import seaborn as sns
sns.set(rc={'figure.figsize':(10, 5)})
import pandas as pd

df = sns.load_dataset('iris')
sns.lmplot(data = df, x = 'sepal_width', y = 'sepal_length', hue = "species")
print(plt.show())