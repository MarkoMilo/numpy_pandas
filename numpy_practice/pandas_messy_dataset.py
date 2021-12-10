import pandas as pd


"""
Pandas - Cleaning Data
Data Cleaning
Data cleaning means fixing bad data in your data set.

Bad data could be:
    * Empty cells
    * Data in wrong format
    * Wrong data
    * Duplicates
In this tutorial you will learn how to deal with all of them.
In this script we will work with messy dataset(dirtydata.csv)
"""



"""
mode() - = the value that appears most frequently.
median() - the value in the middle, after you have sorted all values ascending.
mean() - the average value (the sum of all values divided by number of values).
fillna(<value>) - overwrite DataFrame NaN values vith <value>
df.loc[7, 'Duration'] = 45 - Replace the 8th value in column 'Duration' with value 45
list(df.columns.values) - listo of column names
df.to_csv("<filename.csv>") - Write Dataframe to <filename.csv> file
print(df.duplicated()) - show duplicates
df.drop_duplicates(inplace = True) - remove dupliactes
"""

print("\n********************************************************************\n"
      "Remove all null values and store the data in the new dataframe  \n")
df = pd.read_csv("dirtydata.csv")
newdf = df.dropna()
print("Input dataset:\n{}".format(df))
print("Output dataset:\n{}".format(newdf))

print(df.columns.values)
print(type(df.columns.values))


print("\n********************************************************************\n"
      "Replace all NaN(missing) values from dataframe with Mean, median, or mode\n")
df = pd.read_csv("dirtydata.csv")
x = df["Calories"].mean()
print(x)
df["Calories"].fillna(x, inplace=True)
print(df)

x = df["Calories"].median()
print(x)
df["Calories"].fillna(x, inplace=True)
print(df)

print("\n********************************************************************\n"
      " \n")
df = pd.read_csv('dirtydata.csv')
df['Date'] = pd.to_datetime(df['Date'])
print(df)

print("\n********************************************************************\n"
      "Replace value 450 in row 7\n |7 | 450 | 2020-12-08 | 104 | 134 | 253.3 | \n")
dff = df.loc[7, 'Duration'] = 45
print(dff)


# print("\n********************************************************************\n"
#       " \n")
#
#
# print("\n********************************************************************\n"
#       " \n")
#
#
# print("\n********************************************************************\n"
#       " \n")
#
#
# print("\n********************************************************************\n"
#       " \n")
#
#
