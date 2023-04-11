import matplotlib.pyplot as plt

# graph a basic linear graph
# x_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# y_values = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# plt.style.use("seaborn-v0_8-dark")
# fig, ax = plt.subplots()
# # ax.scatter(x_values, y_values) # scatter plot, points are not connected
# lines = plt.plot(x_values, y_values)  # linear graph

# # add labels
# ax.set_title("Basic Linear Graph Practice")
# ax.set_xlabel("X values")
# ax.set_ylabel("Y values")

# plt.show()

# values
x_values = [1, 2, 3]
y_values = [2, 4, 1]

# style and type of graph
plt.style.use("seaborn")
fig, ax = plt.subplots()
lines = plt.plot(x_values, y_values)

# add labels
ax.set_title("Basic Graphing Practice")
ax.set_xlabel("X values", size=15)
ax.set_ylabel("Y values", size=15)

plt.show()
