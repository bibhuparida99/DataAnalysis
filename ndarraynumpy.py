import numpy as np


w3`4353r5x34sw2 9l9]`1  `


if __name__ == '__main__':
    data = np.random.randn(2, 3)
   # print(data)
    data2 = data*10
    data3 = data+data

    #how the data looks now
    #print(data.size)
    #print(data.dtype)
    #print(data3)
    #print(data2)

    data5 = [6, 7.5, 8, 0, 1]
    array1 = np.array(data5)
    print(array1)

    data6 = [[1, 2, 3, 4], [5, 6, 7, 8]]
    array2 = np.array(data6)
    print(array2)

    zeroarray = np.zeros(10)
    print(zeroarray)
    oneaaray = np.ones(200)
    #print(oneaaray)
    rangearray = np.arange(15)
    print(rangearray)



