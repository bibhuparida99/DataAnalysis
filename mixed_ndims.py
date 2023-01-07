import pandas as pd
if __name__ == '__main__':
    print(__name__, type(__name__))
    #You can concatenate a mix of Series and DataFrame objects.
    # The Series will be transformed to DataFrame with the column name as the name of the Series.
    df1 = pd.DataFrame(
        {
            "A": ["A0", "A1", "A2", "A3"],
            "B": ["B0", "B1", "B2", "B3"],
            "C": ["C0", "C1", "C2", "C3"],
            "D": ["D0", "D1", "D2", "D3"],
        },
        index=[0, 1, 2, 3],
    )
    s1 = pd.Series(["X0", "X1", "X2", "X3"], name="X")

    result = pd.concat([df1, s1], axis=1)
    print(result)


