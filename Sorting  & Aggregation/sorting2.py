#df.sort_values(by=['age', 'salary'], ascending=True, inplace=True)

import pandas as pd

data={
    'name':['dipak', 'dinesh', 'pawan'],
    'age' : [28, 34, 22],
    'salary':[10000, 20000, 30000]
}

df = pd.DataFrame(data)
print(df)

df.sort_values(by=['age', 'salary'], ascending=[True, False], inplace=True)
print('Sorted by descending')
print(df)


