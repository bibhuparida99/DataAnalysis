import pandas as pd
import numpy as np

if __name__ == '__main__':
    data = pd.DataFrame(np.arange(6).reshape((2, 3)),
        index = pd.Index(['Ohio', 'Colorado'], name='state'),
        columns = pd.Index(['one', 'two', 'three'],
        name = 'number'))

    result = data.stack()
print(data)
print(result)
unstackedresult = result.unstack()
print(unstackedresult)