import pandas as pd


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

df = pd.read_csv("dirtydata.csv")
x = df["Calories"].mean()
y = df["Maxpulse"].median()
z = df["Pulse"].median()
for i, j in zip(df["Duration"], df["Duration"].index):
    if i > 60:
        print(i)
        k = df.loc[j, i]