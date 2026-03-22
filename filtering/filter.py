import pandas as pd
df= pd.read_csv("example.csv") #read csv file and create a dataframe

#print(df)

find= df[df["age"]==20]
print(find)

courses=df[df["course"]=="Python"]
print(courses)

and_example= df[(df["age"]==20) & 
                (df["course"]=="Python")]
print(and_example)

or_example = df[(df["age"]==20) | (df["course"]=="Python")]
print(or_example)
