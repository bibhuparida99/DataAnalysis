import numpy as np
import pandas as pd
if __name__ == '__main__':
    s1 = pd.Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])
    s2 = pd.Series([-2.1, 3.6, -1.5, 4, 3.1], index =['a', 'c', 'e', 'f', 'g'])
    s3 = s1 + s2
    print(s3)
    #In the case of DataFrame, alignment is performed on both the rows and the columns:
    df1 = pd.DataFrame(np.arange(9.).reshape((3, 3)), columns=list('bcd'),
         index = ['Ohio', 'Texas', 'Colorado'])
    df2 = pd.DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'),
                           index = ['Utah', 'Ohio', 'Texas', 'Oregon'])

    #Adding these together returns a DataFrame whose index and columns are the unions of the ones in each DataFrame:
    df3= df1+ df2
    #print(df3)
    #
    #Arithmetic methods with fill values
    df4 = pd.DataFrame(np.arange(12.).reshape((3, 4)),
                                    columns = list('abcd'))
    df5 = pd.DataFrame(np.arange(20.).reshape((4, 5)),
                                 columns = list('abcde'))
    df5.loc[1, 'b'] = np.nan
    print(df5)