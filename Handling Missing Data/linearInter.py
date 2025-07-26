import pandas as pd

data = {
    'Time':[1,2,3,4,5],
    'value': [10, None, 30, None, 50]
}

df = pd.DataFrame(data)
print('Before interpolation')
print(df)

df['value'] = df['value']. interpolate(method='linear')
print('After interpolation')
print(df)

"""
1- timer series data
2- numeric data with trends
3- avoid dropping rows

4- cannot work except numerical data like name
5- assumes predictable patterns which might not be appropriate always
"""