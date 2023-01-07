
import pandas as pd
import numpy as np
if __name__ == '__main__':
 df1 = pd.DataFrame(
        {
            "A": ["A0", "A1", "A2", "A3"],
            "B": ["B0", "B1", "B2", "B3"],
            "C": ["C0", "C1", "C2", "C3"],
            "D": ["D0", "D1", "D2", "D3"],
        },
        index=[0, 1, 2, 3],
    )

df2 = pd.DataFrame(
        {
            "A": ["A4", "A5", "A6", "A7"],
            "B": ["B4", "B5", "B6", "B7"],
            "C": ["C4", "C5", "C6", "C7"],
            "D": ["D4", "D5", "D6", "D7"],
        },
        index=[4, 5, 6, 7],
    )

df3 = pd.DataFrame(
        {
            "A": ["A8", "A9", "A10", "A11"],
            "B": ["B8", "B9", "B10", "B11"],
            "C": ["C8", "C9", "C10", "C11"],
            "D": ["D8", "D9", "D10", "D11"],
        },
        index=[8, 9, 10, 11],
    )

df4 = pd.DataFrame(
    {
        "B": ["B2", "B3", "B6", "B7"],
        "D": ["D2", "D3", "D6", "D7"],
        "F": ["F2", "F3", "F6", "F7"],
    },
    index=[2, 3, 6, 7],
)

frames = [df3,df2,df1]
result1 = pd.concat(frames)
#result1
print(result1)

# associate specific keys with each of the pieces of the chopped up DataFrame.
# We can do this using the keys argument:
result2 = pd.concat(frames, keys=["x", "y", "z"])
print(result2)

#select out each chunk by key
print(result2.loc["y"])
print("RESULT3  ########################################################################")

result3 = result = pd.concat([df1, df4], axis=1)
print(result3)
print("########################################################################")
result4 = result = pd.concat([df1, df4])
print(result4)
print("#################################@@@@@@@@@@@@@@@@@")
result5 = pd.concat([df1, df4], ignore_index=True, sort=False)
print(result5)

row_operation = pd.concat([df1, df4], axis=1, join="inner")
print(row_operation)

column_operation = pd.concat([df1, df4], axis=0, join="inner")
print(column_operation)




