import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

# Read data from the .dat file
with open('1.dat', 'r') as file:
    lines = file.readlines()

# Extract data from each line using list comprehension
data = [list(map(float, line.split())) for line in lines]

# Unpack data using numpy array operations
x_values, y1_values, y2_values = np.array(data).T

# Plot the data for the first GP
plt.figure(figsize=(8, 8))

plt.plot(x_values, y1_values, 'ro-', markersize=0, linewidth=0.3)
plt.stem(x_values, y1_values, basefmt='b-', linefmt='-', markerfmt='ro')
plt.title('General Term of Geometric Progression')
plt.xlabel('n')
plt.ylabel('x_1(n)')

plt.gca().xaxis.set_major_locator(MultipleLocator(1))

plt.grid(True)
plt.savefig('../figs/plot1.png')
plt.show()

# Plot the data for the second GP
plt.figure(figsize=(8, 8))

plt.plot(x_values, y2_values, 'ro-', markersize=0, linewidth=0.3)
plt.stem(x_values, y2_values, basefmt='b-', linefmt='-', markerfmt='ro')
plt.title('General Term of Geometric Progression')
plt.xlabel('n')
plt.ylabel('x_2(n)')

plt.gca().xaxis.set_major_locator(MultipleLocator(1))

plt.grid(True)
plt.savefig('../figs/plot2.png')
plt.show()

