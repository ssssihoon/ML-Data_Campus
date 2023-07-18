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
chart = sns.barplot(data = df, x = '누적관객', y = '영화제목', order = df.sort_values('누적관객', ascending = False).영화제목, color="blue")

xlabels = ['{:,.0f}'.format(i) + '만 명' for i in chart.get_xticks() / 10000]
chart.set_xticklabels(xlabels)

plt.xlabel("누적관객", fontsize = 15)
plt.ylabel("영화제목", fontsize = 15)
plt.title("영화 별 누적 관객수", fontsize = 20)

print(plt.show())