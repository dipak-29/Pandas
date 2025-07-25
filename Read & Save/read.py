#read data from CSV/excel/json file into a dataframe


import pandas as pd



#df = pd.read_csv("sales_data_sample.csv", encoding="latin1")

#df = pd.read_excel("supermarket.ods", engine='odf')

df = pd.read_json("Data Resources/sample_Data.json")

print(df)

#gcsfs 