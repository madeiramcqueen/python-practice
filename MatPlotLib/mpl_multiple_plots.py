import matplotlib.pyplot as plt

# # line 1 plots
# x1 = [10, 20, 30]
# y1 = [20, 50, 10]

# # line 2 plots
# x2 = [10, 40, 20]
# y2 = [40, 10, 30]

# # add labels
# plt.title("Two lines of data")
# plt.xlabel("X values")
# plt.ylabel("Y values")

# lines = plt.plot(x1, y1, color="green")
# lines = plt.plot(x2, y2, color="pink")

# plt.show()

# october 3-7 plotted data
oct3_x = [3, 4, 5, 6, 7]
oct3_y = [774.25, 776.065002, 769.5, 772.559, 771.998]

oct4_x = [3, 4, 5, 6, 7]
oct4_y = [773.030029, 778.710022, 772.890015, 776.429, 770.93]

oct5_x = [3, 4, 5, 6, 7]
oct5_y = [770.309998, 782.070007, 775.650024, 776.469, 771]

oct6_x = [3, 4, 5, 6, 7]
oct6_y = [779, 780.47998, 775.539978, 776.85, 778]

oct7_x = [3, 4, 5, 6, 7]
oct7_y = [780.659973, 779.659973, 770.75, 775.080017, 777.437847]

# add labels
plt.title("October Data")
plt.xlabel("October Dates")
plt.ylabel("Financial Data Values")
legend_drawn_flag = True

# line graphs per day
fig, ax = plt.subplots()
plt.plot(oct3_x, oct3_y, color="purple")
plt.plot(oct4_x, oct4_y, color="green")
plt.plot(oct5_x, oct5_y, color="orange")
plt.plot(oct6_x, oct6_y, color="yellow")
plt.plot(oct7_x, oct7_y, color="blue")

# add a legend for october dates
plt.legend(
    ["October 3rd", "October 4th", "October 5th", "October 6th", "October 7th"],
    loc=0,
    frameon=legend_drawn_flag,
)

plt.show()
