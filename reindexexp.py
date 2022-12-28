import json

import numpy as np
import pandas as pd
if __name__ == '__main__':
    obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
    print(obj)
    obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
    print(obj2)

    frame = pd.DataFrame(np.arange(9).reshape((3, 3)),
                        index = ['a', 'c', 'd'],
                     columns = ['Ohio', 'Texas', 'California'])
    print(frame)
    frame2 = frame.reindex(['a', 'b', 'c', 'd'])
    print(frame2)
    






