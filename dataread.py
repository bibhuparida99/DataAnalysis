import numpy as np
import pandas as pd
if __name__ == '__main__':
    df = pd.read_csv('data/ex1.csv')
    print(df)
    print("###############################")
    #We could also have used read_table and specified the delimiter:
    df1 = pd.read_table('data/ex1.csv', sep=',')
    print(df1)

    #file without header
    #To read this file, you have a couple of options.
    # You can allow pandas to assign default column names, or you can specify names yourself:
    df3= pd.read_csv('data/ex2.csv', header=None)
    print(df3)
    print("###########################>>>>>>")
    #adding a header
    df4 = pd.read_csv('data/ex2.csv', names=['a', 'b', 'c', 'd', 'message'])
    print(df4)
    names = ['a', 'b', 'c', 'd', 'message']
    df5 = pd.read_csv('data/ex2.csv', names=names, index_col='message')
    print(df5)
