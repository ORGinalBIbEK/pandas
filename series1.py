import pandas as pd
#series is just a one dimesinonal array with index and values.

data1 = [1, 2, 3]
data2=["A", "B", "C"]
data3=[True, False, True]

series1=pd.Series(data1, index=["a", "b", "c"]) #we can also specify the index of the series.
series2=pd.Series(data2)
series3=pd.Series(data3)

print(series1)
print(series1.loc["a"]) #we can access the values of the series using the index.
print(series1.iloc[0]) #we can also access the values of the series using the position.
print(series2.loc[0]) #we can access the values of the series using the index.
print(series3)


#filter by value
data4=[100,200,300,400,500]
series=pd.Series(data4,index=["a","b","c","d","e"])
filtered_series=series[series<250]
print(filtered_series)