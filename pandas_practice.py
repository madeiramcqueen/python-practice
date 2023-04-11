import pandas

# car data set
carSet = {"cars": ["Volkswagon", "Honda", "Kia"], "passings": [3, 7, 2]}

data = pandas.DataFrame(carSet)
print(data)
