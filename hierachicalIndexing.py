
import pandas as pd
import numpy as np
if __name__ == '__main__':
    data = pd.Series(np.random.randn(9),
         index = [['a', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd'],
         [1, 2, 3, 1, 3, 1, 2, 2, 3]])
    print(data)
    frame = pd.DataFrame(np.arange(12).reshape((4, 3)),
    index = [['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
    columns = [['Ohio', 'Ohio', 'Colorado'],
               ['Green', 'Red', 'Green']])
    print(frame)




