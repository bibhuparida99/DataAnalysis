import numpy as np
import pandas as pd
if __name__ == '__main__':
    obj = pd.Series(range(4), index=['d', 'a', 'b', 'c'])
    #print(obj)
    obj1= obj.sort_index()
    #obj.sort_values()
    print(obj1)
    print(obj)
    #With a DataFrame, you can sort by index on either axis:
    frame = pd.DataFrame(np.arange(8).reshape((2, 4)),
               index = ['three', 'one'],
               columns = ['d', 'a', 'b', 'c'])
    frame.sort_index()
    print(frame)
    frame2= frame.sort_index(axis=0)
    print(frame2)

