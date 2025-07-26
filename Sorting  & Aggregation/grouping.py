import pandas as pd

data={
    'name':['dipak', 'dinesh', 'pawan','nira', 'raju'],
    'age' : [28, 34, 22, 34, 28],
    'salary':[20000, 50000, 30000, 35000, 70000]
}

df = pd.DataFrame(data)

grouped = df.groupby('age')['salary'].sum()

#grouped = df.groupby('age')['salary'].agg(['mean', 'min', 'max'])

print(grouped)

"""
df.groupby('age)
age = 22 (30000)
age = 28 (20000, 70000)
age = 34 (50000, 35000)

[salary].sum()
it finds the sum under each group

"""