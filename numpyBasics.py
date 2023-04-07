import numpy as np

if __name__ == '__main__':
    my_arr = np.arange(1000000)
    #print(my_arr)

    my_list = list(range(1000000))
    my_arr2 = my_arr * 2

    my_list2 = [x * 2 for x in my_list]
