import pandas as pd

mydataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2]
}

print("dataset is: \n{}\ntype of dataset is: {}".format(mydataset, type(mydataset)))

myvar = pd.DataFrame(mydataset)
print("dataset is: \n{}\ntype of dataset is: {}".format(myvar, type(myvar)))

# PANDAS SERIES
print("\n***********************************************************")
print("Create simple Pandas series from list \n")
a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)
print(myvar[0])

print("\n***********************************************************")
print("Create simple Pandas series from list with own labels \n")
a = [1, 7, 2]
print("tip", type(a[0]))
myvar = pd.Series(a, index=['x', 'y', 'z'])
print(myvar)
print(myvar['y'])

print("\n***********************************************************")
print("Dict in series \n")
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)
print('Create a Series using only data from "day1" and "day2" \n')
myvar = pd.Series(calories, index=["day1", "day2"])
print(myvar)

print("\n***********************************************************")
print("Data frames from two series \n")
data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index=['x', 'y', 'z'])
print(df)

df = pd.DataFrame(data)
print(df)

print("\n***********************************************************")
print("Print first row from Data Frame \n")
print(df.loc[0])
print("type: ", type(df.loc[0]))

print("\n***********************************************************")
print("Print first and second row from Data Frame \n")
print("Data: ", df.loc[[0, 1]])

# PANDAS READ CSV

pd.options.display.max_rows = 60  # defone max number of displayed rows in dataframe
df = pd.read_csv("generic-food.csv")
print(df)
print(pd.options.display.max_rows)

print("\n***********************************************************")
print(" \n")
df = pd.read_csv("generic-food.csv")
print(df)

print("\n***********************************************************")
print("Read json or json file \n")
import pandas as pd

data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

df = pd.DataFrame(data)

print(df)
print(df.info())


df.to_csv(r'data.csv', index=False, header=True)

df = pd.read_csv("generic-food.csv")
print(df.info())

# PANDAS - CLEANING EMPTY CELLS
print("\n***********************************************************")
print("Pandas - Cleaning Empty Cells \n")
df = pd.read_csv("data1.csv")
print(df)

# print("\n***********************************************************")
# print(" \n")
#
# print("\n***********************************************************")
# print(" \n")
#
# print("\n***********************************************************")
# print(" \n")
#
# print("\n***********************************************************")
# print(" \n")
#
# print("\n***********************************************************")
# print(" \n")
#
# print("\n***********************************************************")
# print(" \n")
#
# print("\n***********************************************************")
# print(" \n")
#
# print("\n***********************************************************")
# print(" \n")
#
# print("\n***********************************************************")
# print(" \n")
#
# print("\n***********************************************************")
# print(" \n")
#
# print("\n***********************************************************")
# print(" \n")
#
# print("\n***********************************************************")
# print(" \n")
#
# print("\n***********************************************************")
# print(" \n")
#
# print("\n***********************************************************")
# print(" \n")
#

