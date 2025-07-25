#step-1 sample data frame 

import pandas as pd

data = {
    "Name": ['Ram', 'Shyam', 'hari', 'Sita', 'Gita', 'Mohan','raj','Rita'],
    "Age": [28, 34, 22, 30, 29, 40, 35, 27],
    "salary": [50000, 60000, 45000, 70000, 80000, 90000, 75000, 65000],
    "performance score": [85, 90, 75, 95, 80, 88, 92, 78]
}

df = pd.DataFrame(data)

print('Sample DataFrame:')
print(df)

print('\nDescriptive statistics:')
print(df.describe())  # Display descriptive statistics for numerical columns