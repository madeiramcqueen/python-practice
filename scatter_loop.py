import matplotlib.pyplot as plt

# Use a loop to configure and display data calculations

x_values = range(1, 1001)
y_values = [x**2 for x in x_values] # calculate the square root of each x value, using a list comprehension, the result is the y_value

plt.style.use("seaborn-v0_8-dark")
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.PuRd, s=10)

# Set chart title and label axis
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set range for each axis
ax.axis([0, 1100, 0, 1100000])

plt.show()