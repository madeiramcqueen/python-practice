import pandas as pd

# car data set
# carSet = {"cars": ["Volkswagon", "Honda", "Kia"], "passings": [3, 7, 2]}

# data = pd.DataFrame(carSet)
# print(data)
# print(pd.__version__)

# # create a simple pandas series
# a = [1, 4, 6, 9]

# myVar = pd.Series(a)
# print(myVar)

# create simple pandas series with labels
# a = [1, 4, 6, 9]

# myVar = pd.Series(a, index=["a", "b", "c", "d"])
# print(myVar)

# use DataFrame
data = {"calories": [420, 380, 390], "duration": [50, 40, 45]}

df = pd.DataFrame(data, index=["day1", "day2", "day3"])

print(df)