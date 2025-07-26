"""

df['column name'].mean(),
max()
sum() etc

"""

import pandas as pd

data={
    'name':['dipak', 'dinesh', 'pawan'],
    'age' : [28, 34, 22],
    'salary':[10000, 20000, 30000]
}

df = pd.DataFrame(data)

avg_salary = df['salary'].mean()
print(avg_salary)