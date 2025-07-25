# import pandas as pd

# df = pd.read_json("Data Resources/sample_Data.json")

# print('Displaying the info of data set:')
# print(df.info())  # Display concise summary of the DataFrame


import pandas as pd

data = {
    "Name":['Ram','Shyam','hari'],
    "Age": [10,20,30],
    "City": ['kathmandu', 'pokhara', 'jhapa']
}

df = pd.DataFrame(data)

print('Displaying the info of data set:')
print(df.info())