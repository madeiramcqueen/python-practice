import matplotlib.pyplot as plt

# line 1 plots
x1 = [10, 20, 30]
y1 = [20, 50, 10]

# line 2 plots
x2 = [10, 40, 20]
y2 = [40, 10, 30]

# add labels
plt.title("Two lines of data")
plt.xlabel("X values")
plt.ylabel("Y values")

lines = plt.plot(x1, y1, color="green")
lines = plt.plot(x2, y2, color="pink")

plt.show()