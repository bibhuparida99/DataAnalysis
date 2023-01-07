
from collections import OrderedDict
from pandas import DataFrame
import pandas as pd
import numpy as np
if __name__ == '__main__' :
    table = OrderedDict((
        ("Item", ['Item0', 'Item0', 'Item1', 'Item1']),
        ('CType', ['Gold', 'Bronze', 'Gold', 'Silver']),
        ('USD', ['1$', '2$', '3$', '4$']),
        ('EU', ['1€', '2€', '3€', '4€'])
    ))
    d = DataFrame(table)
    print(d)
    print("the pivot table")
    print("***************************************************************")
    p = d.pivot(index='Item', columns='CType', values='USD')
    print(p)
    # multi column pivot
    pm = d.pivot(index='Item',columns='CType')
    print(pm)
    print("********************************")
    print(p.USD)
    print("********************************")
    print(p.USD.Bronze)
    print("********************************")
    print(p.USD.Gold)
    print("********************************")
    print(pm.EU.Gold)

    ###############################################
    ##############################################

    #pivot will fail in floowing case

    table = OrderedDict((
        ("Item", ['Item0', 'Item0', 'Item0', 'Item1']),
        ('CType', ['Gold', 'Bronze', 'Gold', 'Silver']),
        ('USD', ['1', '2', '3', '4']),
        ('EU', ['1€', '2€', '3€', '4€'])
    ))
    d = DataFrame(table)
    p = d.pivot(index='Item', columns='CType', values='USD')
