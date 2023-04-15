import matplotlib.pyplot as plt

# Referenced Data: https://www.digitalinformationworld.com/2020/08/what-gender-pay-gap-looks-like-at-google-facebook-apple-and-other-top-tech-companies.html

# tech companies plotted data
companies = ["Ebay", "Apple", "Facebook", "Microsoft", "Google", "PayPal", "Oracle", "Visa", "Cisco", "Adobe"]
female_salaries = [114.5, 109, 112, 113.5, 109, 106.5, 104.5, 112, 103, 125]


# add labels and type of graph
fig, ax = plt.subplots()
colors = ["Green"]
plt.bar(companies, female_salaries, color=colors)
plt.title("Gender Pay Gaps in Major Tech Companies")
plt.xlabel("Female vs Male")
plt.ylabel("Annual Salaries")
legend_drawn_flag = True

plt.show()