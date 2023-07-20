import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def function1(x):
    if x < 20:
        return 1
    elif x < 40:
        return 2
    elif x < 50:
        return 3
    else:
        return 4

df = sns.load_dataset('titanic')
train_df = df[:800]
test_df = df[800:]
names = train_df.columns
train_df = train_df.drop(names[4::], axis=1)
test_df = test_df.drop(names[4::], axis=1)
train_df["age"] = train_df.groupby(['pclass']).age.transform(lambda x: x.fillna(x.mean()))
test_df["age"] = test_df.groupby(['pclass']).age.transform(lambda x: x.fillna(x.mean()))
map_dict = {'female': 0, 'male': 1}

train_df['sex'] = train_df['sex'].map(map_dict).astype(int)
test_df['sex'] = test_df['sex'].map(map_dict).astype(int)
train_df['age'] = train_df['age'].apply(function1)
test_df['age'] = test_df['age'].apply(function1)

print(test_df)