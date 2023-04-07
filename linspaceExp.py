import numpy as np
if __name__ =='__main__':

    #linspace(start, stop, num=50, endpoint=True, retstep=False)
    #defult values in interval is 50
    #50 values in 1 to 10
    print(np.linspace(1,10))
    #5 values between 1 to 10
    print(np.linspace(1,10,5))
    print(np.linspace(0,10,5))
    #We haven't discussed one interesting parameter so far.
    # If the optional parameter 'retstep' is set, the function will also return
    # the value of the spacing between adjacent values. So, the function will return a tuple ('samples', 'step'):

    samples,spacing = np.linspace(1,20,6, retstep=True)
    print(spacing)
    samples, spacing = np.linspace(1, 20, 6, endpoint=True,  retstep=True)
    print(spacing)
    print(samples)
    samples, spacing = np.linspace(1, 20, 6, endpoint=False,  retstep=True)
    print("this is endpoint false result not including last value")
    print(spacing)
    print(samples)
