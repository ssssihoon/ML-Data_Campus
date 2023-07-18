import matplotlib.pyplot as plt
import seaborn as sns
sns.set(rc={'figure.figsize':(15, 5)})
import pandas as pd

df = sns.load_dataset('iris')
sns.jointplot(data = df, x = 'sepal_width', y = 'sepal_length')
print(plt.show())