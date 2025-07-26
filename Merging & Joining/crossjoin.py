
"""
cross join
1df = n rows
2df = m rows

newdf = m*n rows

"""

import pandas as pd

df1 = pd.DataFrame(
    {
        'A': ['A1', 'A2']
    }
)

df2 = pd.DataFrame(
    {
        'B': ['B1', 'B2', 'B3']
    }
)
cross = pd.merge(df1, df2, how='cross')
print(cross)

