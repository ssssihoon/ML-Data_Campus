import matplotlib.pyplot as plt

x1 = [1, 2, 3]
y1 = [1, 2, 3]
x2 = [1, 2, 3]
y2 = [1, 100, 200]

fig, axe1 = plt.subplots(nrows = 1, ncols= 2)
axe1[0].plot(x1, y1, color = 'blue')
axe1[1].plot(x2, y2, color = 'red')
print(plt.show())