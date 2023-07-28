import numpy as np
import csv

# years = [2016,2017,2018,2019,2020,2021,2022,2023]
# rounds = [1,2,3,4,5,6]

years = [2023]
rounds = [4,5]

for year in years:
    for round_name in rounds:
        try:
            csvfile = open('{}/round{}.csv'.format(year,round_name))
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            data = list(reader)
            for d in data:
                if (len(d)!=7):
                    data.remove(d)

            data = np.array(data)

            data_filter1 = data[:,2] == 'AI'
            data_filter2 = data[:,2] == 'OS'

            data_filter  = np.logical_or(data_filter1,data_filter2)
            data = data[data_filter]

            data_filter1 = data[:,4] == 'NA'
            data_filter2 = data[:,4] == 'Gender-Neutral'

            data_filter  = np.logical_or(data_filter1,data_filter2)
            data = data[data_filter]

            np.save('{}/round{}'.format(year,round_name),data)
            print('Read data for {}, round {} -> {}'.format(year,round_name,data.shape))
        
        except Exception as e:
            print(e)
