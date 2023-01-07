import pandas as pd
import numpy as np
from pandas.core.interchange.dataframe_protocol import DataFrame

if __name__ == "__main__":
    # Row Multi-Index
    row_idx_arr = list(zip(['r0', 'r0'], ['r-00', 'r-01']))
    row_idx = pd.MultiIndex.from_tuples(row_idx_arr)

    # Column Multi-Index
    col_idx_arr = list(zip(['c0', 'c0', 'c1'], ['c-00', 'c-01', 'c-10']))
    col_idx = pd.MultiIndex.from_tuples(col_idx_arr)

    # Create the DataFrame
    d = DataFrame(np.arange(6).reshape(2, 3), index=row_idx, columns=col_idx)
    d = d.applymap(lambda x: (x // 3, x % 3))

    s = d.stack(level=-1)
    print(s)

    s2 = d.stack(level=-2)
    print(s2)
    u = d.unstack(level=-1)
    u = d.unstack(level=-2)
    print(u)
