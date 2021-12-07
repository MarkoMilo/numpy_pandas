import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

print("dataset is: {}\ntype of dataset is: {}".format(mydataset, type(mydataset)))

myvar = pd.DataFrame(mydataset)
print("dataset is: \n{}\ntype of dataset is: {}".format(myvar, type(myvar)))