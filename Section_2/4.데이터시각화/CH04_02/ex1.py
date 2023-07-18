import matplotlib.pyplot as plt

x1 = [1, 2, 3]
y1 = [1, 2, 3]
x2 = [1, 2, 3]
y2 = [1, 4, 7]
plt.plot(x1, x2, color = 'blue', label = 'data1')
plt.plot(x2, y2, color = 'red', label = 'data2')
plt.legend()
print(plt.show())