import pandas as pd

earned={"Day 1":1000, "Day 2":1200, "Day 3":1120}
series=pd.Series(earned)
print(series)
print(series["Day 1"]) #we can access the values of the series using the index. 
print(series.loc["Day 1"]) #we can also access the values of the series using the loc method.
series.loc["Day 4"]=1300 #we can also add new values to the series using the loc method.
print(series)
series.loc["Day 2"]+=50
print(series[series>=1200]) #print the values in the series that are greater than or equal to 1200
print(series)