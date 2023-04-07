
import numpy as np
if __name__ == '__main__':
    F = np.array([1, 1, 2, 3, 5, 8, 13, 21])  # print the first element of F
    print(F[0])
    # print the last element of F
    print(F[-1])

    A = np.array([[3.4, 8.7, 9.9],
                  [1.1, -7.8, -0.7],
                  [4.1, 12.3, 4.8]])
    print(A[1][0])
    print(A[1][1])
    print(A[2][2])
    #We assume that you are familar with the slicing of lists and tuples. The syntax is the same in numpy for one- dimensional arrays, but it can be applied to multiple dimensions as well.
    #The general syntax for a one-dimensional array A looks like this:
    #A[start:stop:step]
    S = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(S[2:5])
    print(S[:4])
    print(S[6:])

    X = np.arange(28).reshape(4, 7)
    print(X)




