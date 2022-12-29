import numpy as np
import pandas as pd
import sys
if __name__ == '__main__':
    data = pd.read_csv('data/ex5.csv')
    print(data)
    #Using DataFrame’s to_csv method, we can write the data out to a comma-separated file:
    data.to_csv('data/out/out.csv')
    #writing to sys.stdout so it prints the text result to the console
    data.to_csv(sys.stdout, sep='!')
    data.to_csv(sys.stdout, na_rep='NULL')
    data.to_csv(sys.stdout, index=False, header=False)
