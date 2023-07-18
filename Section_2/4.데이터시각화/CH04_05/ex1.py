import matplotlib.pyplot as plt
plt.rcParams['font.family'] = ['AppleGothic', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

import seaborn as sns
import pandas as pd

movie_title = ['크루엘라', '극장판 귀멸의 칼날', '학교 가는 길']
audience = [664308, 2099131, 20067]

data = {'영화제목' : movie_title, '누적관객' : audience}
df = pd.DataFrame(data)

sns.barplot(data = df, x = '영화제목', y = '누적관객')
print(plt.show())