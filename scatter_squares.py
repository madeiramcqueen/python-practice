# Use scatter() to plot a single point

import matplotlib.pyplot as plt

# plt.style.use("seaborn")
# fig, ax = plt.subplots()
# ax.scatter(2, 4)
# ax.scatter(3, 6)

# Plotting a series of points using scatter()
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.style.use("seaborn-v0_8-dark")
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=100)

# Set chart title and x and y axis labels
ax.set_title("Scatter Plot", fontsize=24)
ax.set_xlabel("X values", fontsize=14)
ax.set_ylabel("Y values", fontsize=14)

plt.show()
