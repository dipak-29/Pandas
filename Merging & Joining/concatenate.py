"""
concatenation means dataframe lai combine garna ie
vertically (row)
horizontally(column)

pd.concat([df1, df2], axis=0, ignore_index=True)

[df1, df2] = 2 data frames
axis=0 rowwise stacking

ignore_index= True reset the index  in result(renumbers rows from 0,1,2,...)

"""

import pandas as pd

#region1
df_region1 = pd.DataFrame(
    {
        'customerid': [1,2],
        'name': ['gopal', 'raju']
    }
)

#region2
df_region2 = pd.DataFrame(
    {
        'customerid': [3,4],
        'name': ['shyam', 'baburao']
    }
)

#concatenate vetrically
df_concat = pd.concat([df_region1, df_region2], axis=0, ignore_index= True)
print(df_concat)

#concate Horizontally
df_concat = pd.concat([df_region1, df_region2], axis=1, ignore_index= True)
print(df_concat)
