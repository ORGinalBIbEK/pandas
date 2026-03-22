import pandas as pd
df = pd.read_json("example2.json")

print(df.to_string())