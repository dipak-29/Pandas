"""
1- how big is your dataset i.e how many rows and columns it has
2- what are the names of the columns

shape and columns both attributes

"""

import pandas as pd

data = {
    "Name": ['Ram', 'Shyam', 'hari', 'Sita', 'Gita', 'Mohan','raj','Rita'],
    "Age": [28, 34, 22, 30, 29, 40, 35, 27],
    "salary": [50000, 60000, 45000, 70000, 80000, 90000, 75000, 65000],
    "performance score": [85, 90, 75, 95, 80, 88, 92, 78]
}

df = pd.DataFrame(data)
print(df)

print(f'shape: {df.shape}')
print(f'column names: {df.columns}')