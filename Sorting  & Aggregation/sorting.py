"""

#sorting data in 1 column - sort_values()
#df.sort_values(by='column name', True/False, inplace= True)
#df.sort_index(axis=1)
"""

import pandas as pd

data={
    'name':['dipak', 'dinesh', 'pawan'],
    'age' : [28, 34, 22],
    'salary':[10000, 20000, 30000]
}

df = pd.DataFrame(data)
print(df)

df.sort_values(by='age', ascending=True, inplace=True)
print('Sorted by descending')
print(df)


