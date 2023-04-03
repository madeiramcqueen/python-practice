# Practice using matplotlib to plot a simple line graph representing certain data

import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5] # input values
squares = [1, 4, 9, 16, 25] # output values

plt.style.use("seaborn-v0_8-dark") #add styling to graph
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# Set chart title and label axis
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both', labelsize=14)

plt.show()