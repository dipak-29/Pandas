import pandas as pd

data = {
    "Name": ['Ram', 'Shyam', 'hari', 'Sita', 'Gita', 'Mohan','raj','Rita'],
    "Age": [28, 34, 22, 30, 29, 40, 35, 27],
    "salary": [50000, 60000, 45000, 70000, 80000, 90000, 75000, 65000],
    "performance score": [85, 90, 75, 95, 80, 88, 92, 78]
}

df = pd.DataFrame(data)

#display the data frame
print('Sample DataFrame:')
print(df)

#select single column
print('Names (single comuln returns a series):')
name = df["Name"]
print(name)

#select multiple columns
print('Names and Age (multiple columns returns a DataFrame):')
subset = df[["Name", "salary"]]
print(subset)