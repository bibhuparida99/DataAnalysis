import numpy as np
import pandas as pd
if __name__ == '__main__':
    #In the event that you want to form a hierarchical index from multiple columns,
    # pass a list of column numbers or names:
    parsed = pd.read_csv('data/csv_mindex.csv',
                   index_col = ['key1', 'key2'])
    print(parsed)
    parsed3key = pd.read_csv('data/csv_mindex.csv',
                   index_col = ['key1', 'key2','value1'])
   # print(parsed3key)
   #if there is no specific delimeter
   #you can pass a regular expression as a delimiter for read_table.

    result = pd.read_table('data/ex4.txt', sep='\s+')
    print("*****************************************************")
    #print(result)
    result1 = pd.read_csv('data/ex4.csv', skiprows=[0, 2, 3])
    #print(result1)

    #for missing data
    #pandas uses a set of commonly occurring sentinels, such as NA and NULL:
    result5 = pd.read_csv('data/ex5.csv')
    print(result5)
    #to check null
    print(pd.isnull(result5))


