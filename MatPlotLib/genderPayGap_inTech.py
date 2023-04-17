import matplotlib.pyplot as plt
import pandas as pd

# Referenced Data: https://www.digitalinformationworld.com/2020/08/what-gender-pay-gap-looks-like-at-google-facebook-apple-and-other-top-tech-companies.html

# data using pandas formatting
female_salary = {
    "companies": [
        "Ebay",
        "Apple",
        "Facebook",
        "Microsoft",
        "Google",
        "PayPal",
        "Oracle",
        "Visa",
        "Cisco",
        "Adobe",
    ],
    "female_salaries": [114.5, 109, 112, 113.5, 109, 106.5, 104.5, 112, 103, 125],
}

male_salary = {
    "companies": [
        "Ebay",
        "Apple",
        "Facebook",
        "Microsoft",
        "Google",
        "PayPal",
        "Oracle",
        "Visa",
        "Cisco",
        "Adobe",
    ],
    "male_salaries": [119.5, 121, 129, 119, 120, 118, 116, 115, 112.5, 105.5],
}

df1 = pd.DataFrame(female_salary)
df2 = pd.DataFrame(male_salary)

result = pd.merge(df1, df2)

print(result)

# tech companies plotted data
# companies = ["Ebay", "Apple", "Facebook", "Microsoft", "Google", "PayPal", "Oracle", "Visa", "Cisco", "Adobe"]
# female_salaries = [114.5, 109, 112, 113.5, 109, 106.5, 104.5, 112, 103, 125]
# companies = ["Ebay", "Apple", "Facebook", "Microsoft", "Google", "PayPal", "Oracle", "Visa", "Cisco", "Adobe"]
# male_salaries = [119.5, 121, 129, 119, 120, 118, 116, 115, 112.5, 105.5]

# add labels and type of graph
# fig, ax = plt.subplots()
plt.bar(
    result["companies"],
    result["male_salaries"],
    color="Green",
    align="center",
    width=0.4,
)
plt.bar(
    result["companies"],
    result["female_salaries"],
    color="Purple",
    align="edge",
    width=0.4,
)
plt.title("Gender Pay Gaps in Major Tech Companies")
plt.xlabel("Male vs Female")
plt.ylabel("Annual Salaries")
legend_drawn_flag = True

# add legend
plt.legend(["Avg Male Salary", "Avg Female Salary"], loc=0, frameon=legend_drawn_flag)
plt.show()
