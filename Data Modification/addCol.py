#adding column to a dataframe

import pandas as pd


data = {
    "Name": ['Ram', 'Shyam', 'hari', 'Sita', 'Gita', 'Mohan','raj','Rita'],
    "Age": [28, 34, 22, 30, 29, 40, 35, 27],
    "salary": [50000, 60000, 45000, 70000, 80000, 90000, 75000, 65000],
    "performance score": [85, 90, 75, 95, 80, 88, 92, 78]
}

df = pd.DataFrame(data)
print(df)

# Adding a new column by assignment
#square brackets , df["column_name"] = value or some_data

df["Bonus"] = df["salary"] * 0.1  # Adding a new column 'Bonus' which is 10% of 'salary'
print(df)

#using insert method
#df.insert(location, "column_name", some_data)

df.insert(0, "Employee ID", [10, 20,30,40,50,60,70,80])
print(df)