import pandas as pd 

data ={
    "Name" : ["Bibek","Shubham","Abiskar"],
    "Age" : [30,40,50]
}

df=pd.DataFrame(data, index=["a","b","c"]) #we can also specify the index of the dataframe.

print(df.loc["a"])

print(df.iloc[0])

#add new column to the dataframe
df["City"]=["Kathmandu","Lalitpur","Bhaktapur"]

