import numpy as np
import pandas as pd
if __name__ == '__main__':
    #If you want to only read a small number of rows (avoiding reading the entire file), specify that with nrows:

    result6 = pd.read_csv('data/ex6.csv', nrows=5)
    print(result6)
    print("*****************************************************")
    #To read a file in pieces, specify a chunksize as a number of rows:
    chunker = pd.read_csv('data/ex6.csv', chunksize=1000)
    print(chunker)
    print(chunker.nrows)
    tot = pd.Series([])
    for piece in chunker:
        tot = tot.add(piece['key'].value_counts(), fill_value=0)
    tot = tot.sort_values(ascending=False)
    print(tot)



