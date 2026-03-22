import pandas as pd 

data = pd.read_csv("pokeamon.csv")

#1. drop the irrelevant columns
dt=data.drop(columns=["No"])
print(dt)
#data=data.loc[0:11].drop(columns=["No"])
#print(data)

#2.handle missing data
#data=data.dropna(subset=["Type2"])
#print(data)

data=data.fillna({("Type2"): "None"})
print(data)

#3. fix inconsistent data   
data["Type1"]=data["Type1"].replace({"Grass":"GRASS",
                                     "Fire":"FIRE",
                                     "Water":"WATER"})
print(data.to_string())


#4.standardize data
data["Name"]=data["Name"].str.lower()
print(data.to_string())

data["Legendary"]=data["Legendary"].replace({0:"No",1:"Yes"}) #.astype(bool)
print(data.to_string())


