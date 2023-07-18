import matplotlib.pyplot as plt
import seaborn as sns
sns.set(rc = {"figure.figsize":(10, 5)})
import pandas as pd

df = sns.load_dataset("titanic")
sns.countplot(data = df, x = 'sex')
print(plt.show())