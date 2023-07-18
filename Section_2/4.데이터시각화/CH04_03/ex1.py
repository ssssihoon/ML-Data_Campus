import matplotlib.pyplot as plt

x1 = [1, 2, 3]
y1 = [1, 2, 3]
x2 = [1, 2, 3]
y2 = [1, 100, 200]

plt.subplot(2, 1, 1)
plt.plot(x1, y1)
plt.title('data1')

plt.subplot(2, 1, 2)
plt.plot(x2, x1)
plt.title('data2')

print(plt.show())