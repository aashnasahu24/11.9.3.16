import matplotlib.pyplot as plt
import numpy as np

a = 4
r = -2
start_n = 0
end_n = 10

x = np.arange(start_n, end_n + 1, 1)
y = a*(r**x)
y[x<0]=0

plt.plot(x, y, 'ro-', markersize=0, linewidth=0.5)
# Use plt.stem for the stem plot
plt.stem(x, y, basefmt='b-', linefmt='-', markerfmt='ro')
plt.title('General Term of Geometric Progression')
plt.xlabel('n')
plt.ylabel('Term Value')
plt.grid(True)
plt.savefig('./figs/fig1.png')
plt.show()
