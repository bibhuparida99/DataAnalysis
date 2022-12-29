import numpy as np
import pandas as pd
if __name__ == '__main__':
    pd.options.display.max_rows = 10
    #Before we look at a large file, we make the pandas display settings more compact:
    #we write above option code

    #result6 = pd.read_csv('data/ex6.csv')
    #result6 = pd.read_csv('data/ex6.csv', nrows=5)
    #print(result6)
    parsed = pd.read_csv('data/csv_mindex.csv',
                         index_col=['key1', 'key2'])
    print(parsed)




