import numpy as np
import pandas as pd
from Trigram_Class import Trigram_Model
import pickle


#Goal here is to pick the right smoothing hyper parameter.

#First, load in test set (data4.csv)
test_set = pd.read_csv('data4.csv',index_col=0)

#load in all the trigrams!
cytoplasm_trigram = pickle.load(open('cytoplasm_trigram.pkl','rb'))
nucleus_trigram = pickle.load(open('nucleus_trigram.pkl','rb'))
extracellular_trigram = pickle.load(open('extracellular_trigram.pkl','rb'))
cellmembrane_trigram = pickle.load(open('cellmembrane_trigram.pkl','rb'))
mitochondrion_trigram = pickle.load(open('mitochondrion_trigram.pkl','rb'))
plastid_trigram = pickle.load(open('plastid_trigram.pkl','rb'))
endoplasmicreticulum_trigram = pickle.load(open('endoplasmicreticulum_trigram.pkl','rb'))
lysosome_vacuole_trigram = pickle.load(open('lysosome_vacuole_trigram.pkl','rb'))
golgi_apparatus_trigram = pickle.load(open('golgi_apparatus_trigram.pkl','rb'))
peroxisome_trigram = pickle.load(open('peroxisome_trigram.pkl','rb'))

localizations = [
        'Cytoplasm',
        'Nucleus',
        'Extracellular',
        'Cell membrane',
        'Mitochondrion',
        'Plastid',
        'Endoplasmic reticulum',
        'Lysosome/Vacuole',
        'Golgi apparatus',
        'Peroxisome']


#get sequences and labels
sequences = []
labels = []
predictions = []
ids = []

for i in range(len(test_set)):
    current_labels = []
    for x in range(4,14):
        if test_set.iloc[i,x] == 1.0:
            current_labels.append(localizations[x-4])
    labels.append(current_labels)
    sequence = test_set.iloc[i,14]
    sequences.append(sequence)
    ids.append(test_set.iloc[i,0])
    losses = [cytoplasm_trigram.compute_loss(sequence),
        nucleus_trigram.compute_loss(sequence),
        extracellular_trigram.compute_loss(sequence),
        cellmembrane_trigram.compute_loss(sequence),
        mitochondrion_trigram.compute_loss(sequence),
        plastid_trigram.compute_loss(sequence),
        endoplasmicreticulum_trigram.compute_loss(sequence),
        lysosome_vacuole_trigram.compute_loss(sequence),
        golgi_apparatus_trigram.compute_loss(sequence),
        peroxisome_trigram.compute_loss(sequence)]
    
    minimum_index = 0
    minimum = losses[minimum_index]
    
    for i in range(1,len(losses)):
        if losses[i] < minimum:
            minimum = losses[i]
            minimum_index = i

    classification = localizations[minimum_index]

    predictions.append(classification)

for i in range(len(predictions)):
    print(ids[i],labels[i],predictions[i])


#calculate correct percentage
right = 0
wrong = 0
for i in range(len(test_set)):
    if predictions[i] in labels[i]:
        right += 1
    else:
        wrong += 1

print('right: ',right)
print('wrong: ',wrong)
print(f'score: {right/(right+wrong)}')
