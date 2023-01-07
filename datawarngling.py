
import pandas as pd
import numpy as np
if __name__ == '__main__':
    df = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'],
                         'data1': range(6)})
    #If a column in a DataFrame has k distinct values, you would derive a matrix or
    # Data‐ Frame with k columns containing all 1s and 0s.
    # pandas has a get_dummies function for doing this,
    dummydf = pd.get_dummies(df['key'])
    print(dummydf)

    dummies = pd.get_dummies(df['key'], prefix='key')
    df_with_dummy = df[['data1']].join(dummies)
    print(df_with_dummy)



