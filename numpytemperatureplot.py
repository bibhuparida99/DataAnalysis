import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    cvalues = [20.1, 20.8, 21.9, 22.5, 22.7, 22.3, 21.8, 21.2, 20.9, 20.1]
    #to one dim array
    C = np.array(cvalues)
    CinFarenhit = (C*9/5+32)
    print(C)
    print(CinFarenhit)

    #to plot grapgh

    plt.plot(C)
    plt.show()