import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

# Read data from the .dat file
with open('1.dat', 'r') as file:
    lines = file.readlines()

# Extract data from each line
x_values = []
y1_values = []
y2_values = []

for line in lines:
    values = line.split()
    x_values.append(float(values[0]))
    y1_values.append(float(values[1]))
    y2_values.append(float(values[2]))
    
# Plot the data
plt.figure(figsize=(8, 8))

# Plot for the first GP
plt.plot(x_values, y1_values, 'ro-', markersize=0, linewidth=0.3)
plt.stem(x_values, y1_values, basefmt='b-', linefmt='-', markerfmt='ro')
plt.title('General Term of Geometric Progression')
plt.xlabel('n')
plt.ylabel('Term Value')

plt.gca().xaxis.set_major_locator(MultipleLocator(1))

plt.grid(True)
plt.savefig('../figs/plot1.png')
plt.show()

# Plot for the second GP
plt.plot(x_values, y2_values, 'ro-', markersize=0, linewidth=0.3)
plt.stem(x_values, y2_values, basefmt='b-', linefmt='-', markerfmt='ro')
plt.title('General Term of Geometric Progression')
plt.xlabel('n')
plt.ylabel('Term Value')

plt.gca().xaxis.set_major_locator(MultipleLocator(1))

plt.grid(True)
plt.savefig('../figs/plot2.png')

plt.show()
