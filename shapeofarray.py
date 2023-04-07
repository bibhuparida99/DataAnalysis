
import numpy as np
if __name__ == '__main__':
    ndarray= np.array([[67, 63, 87],
                [77, 69, 59],
                [85, 87, 99],
                [79, 72, 71],
                [63, 89, 93],
                [68, 92, 78]])
    print(ndarray.shape)
    print(np.shape(ndarray))
    ndarray.shape= (3,6)
    print(ndarray)
    print(ndarray.shape)

