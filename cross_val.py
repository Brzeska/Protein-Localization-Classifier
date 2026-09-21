from train import train
from score import score
import pandas as pd
import numpy as np
import sys

#k: smoothing parameter!
k = 1

for k in np.arange(5,12,1.0):
    highest_mean = 0
    best_k = 0
    #print(f'Cross validating on smoothing parameter k={k}')

    data0 = pd.read_csv('data0.csv',index_col=0)
    data1 = pd.read_csv('data1.csv',index_col=0)
    data2 = pd.read_csv('data2.csv',index_col=0)
    data3 = pd.read_csv('data3.csv',index_col=0)

    splits = [data0,data1,data2,data3]
    accuracies = []
    
    
    cycle = 1 #which turn of cross val it is
    for dev in splits:
        #print()
        #print()
        #print(f'cross validation round {cycle}')
        #print('building training set...')
        train_set = pd.concat([i for i in splits if i is not dev], ignore_index=True)
        #print('training trigrams...')
        train(train_set,k)
        #print('finished training!')
        #print(f'evaluating score on held out dev set {cycle}...')
        accuracies.append(score(dev))
        #print(f'running accuracy scores: {accuracies}')
        #print('starting next round!')
        cycle += 1
        #print()
        #print()
    
    current_mean = np.mean(accuracies)
    if current_mean > highest_mean:
        highest_mean = current_mean
        best_k = k
        print(f'new best mean ({current_mean}) for k={k}')
        print()

    print(f'smoothing factor: {k}')
    print(f'accuracies: {accuracies}')
    print(f'average accuracy: {current_mean}')
    print()

        

print(f'best mean ({current_mean}) for k={k}')
