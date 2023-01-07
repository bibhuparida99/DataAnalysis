
import pandas as pd
import numpy as np
if __name__ == '__main__':
    df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
          'data1': range(7)})

    df2 = pd.DataFrame({'key': ['a', 'b', 'd'],
         'data2': range(3)})
    joined_data = pd.merge(df1,df2)
    print(joined_data)
    ##########################################################################


    df3 = pd.DataFrame({'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                                 'data1': range(7)})
    df4 = pd.DataFrame({'rkey': ['a', 'b', 'd'],
                                 'data2': range(3)})
    pd.merge(df3, df4, left_on='lkey', right_on='rkey')



    #outer join
outer_joined = pd.merge(df1, df2, how='outer')
print(outer_joined)
##########################################################################
left_joined = pd.merge(df1, df2, how='left')
print(left_joined)
##########################################################################
right_joined = pd.merge(df1, df2, how='right')
print(right_joined)
##########################################################################
inner_joined = pd.merge(df1, df2, how='inner')
print(inner_joined)
##########################################################################
output_joined = pd.merge(df1, df2, how='outer')
print(output_joined)
##########################################################################











