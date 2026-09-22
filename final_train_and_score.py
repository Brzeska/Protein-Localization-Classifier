from Trigram_Class import Trigram_Model
from train import train
from score import score
import pandas as pd
import numpy as np

#config:
k = 7.0 #change to optimal smoothing factor (run cross_val.py to find)

#grab train/dev datasets to make the big final training dataset
data0 = pd.read_csv('data0.csv',index_col=0)
data1 = pd.read_csv('data1.csv',index_col=0)
data2 = pd.read_csv('data2.csv',index_col=0)
data3 = pd.read_csv('data3.csv',index_col=0)

#concatenate
data = pd.concat([data0,data1,data2,data3])

#grab test set
data4 = pd.read_csv('data4.csv',index_col=0)

train(data,k)
print(f'final score: {score(data4,True)}')

