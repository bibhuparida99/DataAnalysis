import json
from pandas import DataFrame, Series
import pandas as pd
import numpy as np
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
    results = Series([x.split()[0] for x in frame.a.dropna()])
    #print(results)
    #print(results.value_counts()[:8])
    cframe = frame[frame.a.notnull()]
    #print(cframe)
    #print(frame.a)
    operating_system = np.where(cframe['a'].str.contains('Windows'), 'Windows', 'Not Windows')
    print(operating_system[:5])
    by_tz_os = cframe.groupby(['tz', operating_system])
    #print(by_tz_os)
    agg_counts = by_tz_os.size().unstack().fillna(0)
    #print(agg_counts[:10])
    # Use to sort in ascending order
    indexer = agg_counts.sum(1).argsort()
    #print(indexer)
    count_subset = agg_counts.take(indexer)[-10:]
    print(count_subset)
    count_subset.plot(kind='barh', stacked=True)
   # plt.show()
    normed_subset = count_subset.div(count_subset.sum(1), axis=0)
    normed_subset.plot(kind='barh', stacked=True)
    plt.show()
