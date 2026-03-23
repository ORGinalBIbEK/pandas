import pandas as pd

data=pd.read_csv("movies.csv")

print("First 5 Rows:")
print(data.head())

print("\n Dataset Info:")
print(data.info())

print("\n Summary Statistics:")
print(data.describe())

top_movie=data.loc[data["rating"]>8.0]
print("\n Top Rated Movies:")
print(top_movie)

industry=data.groupby("industry")["rating"].mean()
print("\n Average rating by industry is")
print(industry)

avg_rating=data.groupby("genre")["rating"].mean()
print("\nAverage rating by genre is ",avg_rating)


#average runtime by genre

avg_genre=data.groupby("genre")["runtime_min"].mean()
print("\n Average runtime by genre is ",avg_genre)


# Get top 5 rated movies
top5 = data.nlargest(5, "rating")

print(top5[["movie", "industry", "genre", "year", "rating"]])


# Get top 5 longest runtime movies
longest_runtime= data.nlargest(5,"runtime_min" )
print(longest_runtime[["movie", "industry", "genre", "year", "runtime_min"]])


# Find the index of the smallest runtime
smallest_index = data["runtime_min"].idxmin()

# Get the full row
smallest_movie = data.loc[smallest_index]

# Print selected columns
print(smallest_movie[["movie", "industry", "genre", "year", "runtime_min"]])
