import pandas as pd

df = pd.read_csv("example.csv") #read csv file and create a dataframe

print(df)
print(df.to_string()) #print the entire dataframe without truncation

print(df.loc[0:11,"id":"age"]) #loc is used to select rows and columns by label
