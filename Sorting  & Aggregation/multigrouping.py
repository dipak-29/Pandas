import pandas as pd

data={
    'name':['dipak', 'dinesh', 'pawan','nira', 'raju'],
    'age' : [28, 34, 22, 34, 28],
    'salary':[20000, 50000, 30000, 35000, 70000]
}

df = pd.DataFrame(data)

grouped = df.groupby(['age','name'])['salary'].sum()
print(grouped)