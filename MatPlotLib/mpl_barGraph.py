import matplotlib.pyplot as plt

country = ["A", "B", "C", "D", "E"]
gdp_per_capita = [45000, 42000, 52000, 49000, 47000]


# customize color per country
colors = ["Blue", "Green", "Purple", "Pink", "Yellow", "Brown"]

# add labels and type of graph
plt.bar(country, gdp_per_capita, color=colors)
plt.title("Country & GDP Per Capita")
plt.xlabel("Country")
plt.ylabel("GDP Per Capita")

plt.show()
