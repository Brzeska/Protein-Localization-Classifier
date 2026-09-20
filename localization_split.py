import numpy as np
import pandas as pd
from Trigram_Class import Trigram_Model
import pickle

#data{0-2}.csv are training
#data3.csv is dev
#data4.csv is test


#load in training data
data0 = pd.read_csv('data0.csv',index_col=0)
data1 = pd.read_csv('data1.csv',index_col=0)
data2 = pd.read_csv('data2.csv',index_col=0)

#concatenate into one dataframe
data = pd.concat([data0,data1,data2])

#There are ten localization labels: 
#Cytoplasm
#Nucleus
#Extracellular
#Cell membrane
#Mitochondrion
#Plastid
#Endoplasmic reticulum
#Lysosome/Vacuole
#Golgi apparatus
#Peroxisome

alphabet = open('proteinogenics.txt').read().splitlines()
alphabet += ['U','X']

#Cytoplasm
cytoplasm_split = data[data["Cytoplasm"] == 1.0]
data = cytoplasm_split["Sequence"].tolist()
cytoplasm_trigram = Trigram_Model(data,alphabet)
f = open('cytoplasm_trigram.pkl', 'wb')
pickle.dump(cytoplasm_trigram,f)
f.close()


