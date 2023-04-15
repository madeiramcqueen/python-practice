import matplotlib.pyplot as plt

# Plot first five cubic numbers
input_values = [1, 2, 3, 4, 5]  # input values
cube_values = [1, 8, 27, 64, 125]  # output values, cubes

plt.style.use("seaborn-v0_8-dark")  # add styling to graph
fig, ax = plt.subplots()
lines = plt.plot(input_values, cube_values)  # show data in linear graph form
# ax.scatter(input_values, cube_values, c=cube_values, cmap=plt.cm.BuGn, s=10) # add colormap to enhance visualization of data (shows a color gradient from starting point to ending point)

# Set chart title and label axis
ax.set_title("Cubic Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

# Set range for each axis
ax.axis([0, 6, 0, 130])

plt.show()
