import pandas as pd
import numpy as np
import random

a = []
b = []

for i in range(100):
    a.append(random.randint(1,3))
    b.append(random.randint(1,3))
df = pd.DataFrame({'품목' : a, '크기' : b})
df['금액'] = df['품목'] * df['크기'] * 500
df['수수료'] = df['금액'] * 0.1
fruit_name = {1 : '토마토', 2 : '바나나', 3 : '사과'}
fruit_size = {1 : '소', 2 : '중', 3 : '대'}
df['품목'] = df['품목'].map(fruit_name)
df['크기'] = df['크기'].map(fruit_size)
df2 = pd.pivot_table(df, values = '금액', index = ['품목'], columns = ['크기'], aggfunc = ( 'count', 'sum'))
print(df2)
