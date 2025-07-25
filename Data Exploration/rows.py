"""
#head() is a method in pandas that returns the first n rows of a DataFrame.
head(n) 5

#tail() is similar but returns the last n rows.
tail(n) 5
if n is not specified, it defaults to 5.
"""

import pandas as pd

df = pd.read_json("Data Resources/sample_Data.json")

print('Display 5 rows of first:')
print(df.head())  # Display the first 5 rows

print('Display 10 rows of last:')
print(df.tail(10))  # Display the last 10 rows