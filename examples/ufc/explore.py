import pandas as pd

# Load the CSV file
df = pd.read_csv("ufc_fights_all.csv")

# See the first 5 rows
print(df.head())

df.shape         # (rows, columns)
df.columns       # list of column names
df.dtypes        # column data types
df.info()        # memory usage + type summary


