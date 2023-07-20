import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier


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


x_train = train_df.drop(['survived'], axis=1)
y_train = train_df['survived']
x_test = test_df.drop(['survived'], axis=1)
y_test = test_df['survived']

decision_tree = DecisionTreeClassifier()
decision_tree.fit(x_train, y_train)
y_pred = decision_tree.predict(x_test)
y_test_list = list(y_test)

total = 0
for i in range(len(y_pred)):
    if y_pred[i] == y_test_list[i]:
        total += 1
    else:
        pass

