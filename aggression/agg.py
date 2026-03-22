import pandas as pd
data = pd.read_csv("example.csv")

print(data.mean(numeric_only=True))

print(data.sum(numeric_only=True))

print(data.min(numeric_only=True))

print(data.count())


#for single column

print(data.loc[0:11, "marks"].mean(numeric_only=True))
print(data.loc[0:11, ["age"]].mean(numeric_only=True))

print("\n")

#grouping
group = data.groupby("course")
print(group["age"].max(numeric_only=True))

group2 = data.groupby("course")
print(group2["marks"].max(numeric_only=True))

group3=data.groupby("course")
print(group3["marks"].sum(numeric_only=True))
