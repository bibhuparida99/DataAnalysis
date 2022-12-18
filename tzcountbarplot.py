import json
from pandas import DataFrame, Series
import pandas as pd
import matplotlib.pyplot as plt

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    path = '/Users/bibhu/Documents/DataAnalysis/python/usagov_bitly_data2012-03-16-1331923249.txt'
    records = [json.loads(line) for line in open(path)]
    #print(records[0]['tz'])
    #count timezone
    #time_zones = [rec['tz'] for rec in records]
    time_zones = [rec['tz'] for rec in records if 'tz' in rec]
    #print(time_zones[:10])
    #create frame with records
    frame = DataFrame(records)
    clean_tz = frame['tz'].fillna('Missing')
    clean_tz[clean_tz == ''] = 'Unknown'
    tz_counts = clean_tz.value_counts()
    #print(tz_counts)
    #horizontal bar plot can be accomplished using the plot method on the
    tz_counts[:10].plot(kind='barh', rot=0)
    plt.show()



