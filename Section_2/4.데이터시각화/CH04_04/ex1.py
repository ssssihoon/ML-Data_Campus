import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = sns.load_dataset('iris')
sns.scatterplot(data = df, x = 'petal_length', y = 'petal_width')
print(plt.show())