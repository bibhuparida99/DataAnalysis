import json

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    path = '/Users/bibhu/Documents/DataAnalysis/python/usagov_bitly_data2012-03-16-1331923249.txt'
    records = [json.loads(line) for line in open(path)]
    #print(records[0]['tz'])
    #count timezone
    #time_zones = [rec['tz'] for rec in records]
    time_zones = [rec['tz'] for rec in records if 'tz' in rec]
    print(time_zones[:10])
    print(time_zones[:20])
