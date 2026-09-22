from train import train
from score import score
import pandas as pd
import numpy as np
import sys

#k: smoothing parameter!
k = 1

highest_mean = 0
best_k = 0


data0 = pd.read_csv('data0.csv',index_col=0)
data1 = pd.read_csv('data1.csv',index_col=0)
data2 = pd.read_csv('data2.csv',index_col=0)
data3 = pd.read_csv('data3.csv',index_col=0)

#initially true, once these matrices are generated, will go false forever
generate_count_matrices = True
matrices = []
for k in np.arange(5,12,1.0):
    data0 = pd.read_csv('data0.csv',index_col=0)
    #print(f'Cross validating on smoothing parameter k={k}')
    splits = [data0,data1,data2,data3]
    accuracies = []
    
    
    cycle = 0 #which turn of cross val it is
    for dev in splits:
        train_set = pd.concat([i for i in splits if i is not dev], ignore_index=True)
        if generate_count_matrices:
            #generate the count matrices
            matrices.append(train(train_set,k,out=True))
            if cycle == 3:
                generate_count_matrices=False
        else:
            #load in previously generated count matrices
            train(train_set,k,N_matrix=matrices[cycle],out=False)
        accuracies.append(score(dev))
        cycle += 1
    
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

        

print(f'best mean ({highest_mean}) for k={best_k}')
