import pandas as pd

"""
USEFULL PANDAS METHODS
import panadas as pd - pd shortcat uses as pandas

df = pd.series(<data>) Load data into pandas series
df = pd.DataFrame(<data>)
  <data> could be 'dictionari', 'list', 'nested list', 'tuple' 
df.loc[<row index>] - show indexed row
df = pd.read_csv("<csv file>") - read csv file to DataFrame
df.to_string() - print entire DataFrame
pd.options.display.max_rows - check system maximum rows to display DataFrame
pd.options.display.max_rows = 9999 - set system maximum rows to display DataFrame
df1 = pd.read_json('<file.json>') - load json file into DataFrame
df1.to_csv("<filename.csv>") - write json to csv file 

"""

pd.options.display.max_rows = 200
df = pd.read_json("data.json")
df.to_csv("data1.csv")
print(df.to_string)
