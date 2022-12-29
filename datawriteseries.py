import numpy as np
import pandas as pd
import sys
if __name__ == '__main__':
    data = pd.read_csv('data/ex5.csv')
    print(data)
    #series also has to_csv method
    dates = pd.date_range('1/1/2000', periods=7)
    ts = pd.Series(np.arange(7), index=dates)
    ts.to_csv('data/out/tseries.csv')

    