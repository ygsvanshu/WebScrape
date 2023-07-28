import numpy as np

years = [2016,2017,2018,2019,2020,2021,2022,2023]
rounds = [1,2,3,4,5,6]

for year in years:
    for round_name in rounds:
        try:
            data = np.load('{}/round{}.npy'.format(year,round_name))
            print(data[:5])
        except Exception as e:
            print(e)