import matplotlib.pyplot as plt

x1 = [1, 2, 3]
y1 = [1, 2, 3]
x2 = [1, 2, 3]
y2 = [1, 50, 200]


fig, axe1 = plt.subplots()
axe2 = axe1.twinx()
axe1.plot(x1, y1, color = 'blue')
axe2.plot(x2, y2, color = 'red')
print(plt.show())