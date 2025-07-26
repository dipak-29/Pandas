"""
pd.merge(df1, df2, on="common column_name", how="type of join" )

"""
import pandas as pd

#customer dataframe
df_customers = pd.DataFrame(
    {
        'customerid':[1, 2, 3],
        'name': ['ramesh', 'dinesh', 'nabin']
    }
)
#order dataframe
df_orders = pd.DataFrame(
    {
        'customerid': [1,2,4],
        'orderamount' : [250, 450, 350]

    }
)
#merge
# df_merged = pd.merge(df_customers, df_orders, on='customerid', how='inner')
# print('inner join')

# df_merged = pd.merge(df_customers, df_orders, on='customerid', how='outer')
# print('outer join')

# df_merged = pd.merge(df_customers, df_orders, on='customerid', how='left')
# print('left join')

# df_merged = pd.merge(df_customers, df_orders, on='customerid', how='right')
# print('right join')

df_merged = pd.merge(df_customers, df_orders,  how='cross')
print('cross join')



print(df_merged)

