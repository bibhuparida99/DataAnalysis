import json
import pandas as pd
if __name__ == '__main__':
    obj = pd.Series([4, 7, -5, 3])
    #print(obj)
    #print(obj.values)
    #print(obj.index)

    obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
    #print(obj2)
    #print(obj2['b'])
    sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
    obj3 = pd.Series(sdata)
    #print(obj3)
    states = ['Utah', 'Ohio', 'Oregon', 'Texas']
    obj4 = pd.Series(sdata, index=states)
    print(obj4)
    obj5 = pd.Series(states)
   # print(obj5)

   ####
   #### DATA FRAME

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2],
        'prez':['a', 'b', 'c', 'd', 'e', 'z']}
frame = pd.DataFrame(data)
#print(frame)
frame2 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
                           index=['one', 'two', 'three', 'four',
                               'five', 'six'])
frame2['eastern'] = frame2.state == 'Ohio'
frame2['western'] = frame2.year == 2002
print(frame2)
print(frame2['state'])





