#dropna() drops the missing column and row  values
#df.dropna(axis=o, inplace=True)
#axis=o - removes row missing value and 1 - removes colums missing value

import pandas as pd

data = {
    "Name": ['Ram', None, 'hari', 'Sita', 'Gita', 'Mohan','raj','Rita'],
    "Age": [28, None, 22, 30, 29, 40, 35, 27],
    "salary": [50000, None, 45000, 70000, 80000, 90000, 75000, 65000],
    "performance score": [85, None, 75, 95, 80, 88, 92, 78]
}

df = pd.DataFrame(data)
print(df)

df.dropna(inplace=True)
print(df)
