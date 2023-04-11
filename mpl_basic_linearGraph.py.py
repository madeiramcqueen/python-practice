import matplotlib.pyplot as plt

# graph a basic linear graph
x_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_values = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

plt.style.use("seaborn-v0_8-dark")
fig, ax = plt.subplots()
# ax.scatter(x_values, y_values) # scatter plot, points are not connected
lines = plt.plot(x_values, y_values)  # linear graph

plt.show()
