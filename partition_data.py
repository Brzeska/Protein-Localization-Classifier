#reads in the raw data from DeepLoc 2.0 and saves as five separate csv files
#each containing exactly one homology aware partition

import pandas as pd

raw_data = pd.read_csv('Swissprot_Train_Validation_dataset.csv', index_col=0)

splits = [raw_data[raw_data["Partition"] == i] for i in range(5)]

n = 0
for i in splits:
    i.to_csv(f'data{n}.csv')
    n += 1


