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


#single condition filter
high_salary = df [df['salary'] > 70000 ]
print('Employees with salary greater than 70000:')
print(high_salary)

#multiple condition filter
#filtering rows salary>5000 and age >30

filtered = df[(df['salary'] > 50000) & (df['Age'] > 30)]
print('Employees with salary greater than 50000 and age greater than 30:')
print(filtered)

#using or condition
filtered_or = df[(df['salary'] > 70000) | (df['Age'] < 30)]
print('Employees with salary greater than 70000 or age less than 30:')
print(filtered_or)