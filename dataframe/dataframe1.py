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
print(df)

#add new row to the dataframe
new_row = pd.DataFrame([{"Name":"Suman","Age": 35, "City": "Pokhara"}], 
                       index=["d"])
multiple_rows = pd.DataFrame([{"Name":"Sarthak", "Age":30, "City":"kanchanpur"},
                              {"Name":"Achyut","Age": 28, "City":"Dharan"}],index=["e","f"])
df=pd.concat([df,new_row,multiple_rows])
print(df)