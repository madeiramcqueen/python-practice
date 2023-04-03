# Use scatter() to plot a single point

import matplotlib.pyplot as plt

plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.scatter(2, 4)

# Set chart title and x and y axis labels
ax.set_title("Scatter Plot", fontsize=24)
ax.set_xlabel("X values", fontsize=14)
ax.set_ylabel("Y values", fontsize=14)

plt.show()
