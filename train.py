from Trigram_Class import Trigram_Model
import pickle

def train(data, k):
    alphabet = open('proteinogenics.txt').read().splitlines()
    alphabet += ['X','B']

    #Cytoplasm
    cytoplasm_split = data[data["Cytoplasm"] == 1.0]
    data_split = cytoplasm_split["Sequence"].tolist()
    cytoplasm_trigram = Trigram_Model(data_split,alphabet,k)
    f = open('cytoplasm_trigram.pkl', 'wb')
    pickle.dump(cytoplasm_trigram,f)
    f.close()

    #Nucleus
    nucleus_split = data[data["Nucleus"] == 1.0]
    data_split = nucleus_split["Sequence"].tolist()
    nucleus_trigram = Trigram_Model(data_split,alphabet,k)
    f = open('nucleus_trigram.pkl', 'wb')
    pickle.dump(nucleus_trigram,f)
    f.close()


    #Extracellular
    extracellular_split = data[data["Extracellular"] == 1.0]
    data_split = extracellular_split["Sequence"].tolist()
    extracellular_trigram = Trigram_Model(data_split,alphabet,k)
    f = open('extracellular_trigram.pkl', 'wb')
    pickle.dump(extracellular_trigram,f)
    f.close()

    #Cell membrane
    cellmembrane_split = data[data["Cell membrane"] == 1.0]
    data_split = cellmembrane_split["Sequence"].tolist()
    cellmembrane_trigram = Trigram_Model(data_split,alphabet,k)
    f = open('cellmembrane_trigram.pkl', 'wb')
    pickle.dump(cellmembrane_trigram,f)
    f.close()

    #Mitochondrion
    mitochondrion_split = data[data["Mitochondrion"] == 1.0]
    data_split = mitochondrion_split["Sequence"].tolist()
    mitochondrion_trigram = Trigram_Model(data_split,alphabet,k)
    f = open('mitochondrion_trigram.pkl', 'wb')
    pickle.dump(mitochondrion_trigram,f)
    f.close()

    #Plastid
    plastid_split = data[data["Plastid"] == 1.0]
    data_split = plastid_split["Sequence"].tolist()
    plastid_trigram = Trigram_Model(data_split,alphabet,k)
    f = open('plastid_trigram.pkl', 'wb')
    pickle.dump(plastid_trigram,f)
    f.close()

    #Endoplasmic reticulum
    endoplasmicreticulum_split = data[data["Endoplasmic reticulum"] == 1.0]
    data_split = endoplasmicreticulum_split["Sequence"].tolist()
    endoplasmicreticulum_trigram = Trigram_Model(data_split,alphabet,k)
    f = open('endoplasmicreticulum_trigram.pkl', 'wb')
    pickle.dump(endoplasmicreticulum_trigram,f)
    f.close()

    #Lysosome/Vacuole
    lysosome_vacuole_split = data[data["Lysosome/Vacuole"] == 1.0]
    data_split = lysosome_vacuole_split["Sequence"].tolist()
    lysosome_vacuole_trigram = Trigram_Model(data_split,alphabet,k)
    f = open('lysosome_vacuole_trigram.pkl', 'wb')
    pickle.dump(lysosome_vacuole_trigram,f)
    f.close()

    #Golgi apparatus
    golgi_apparatus_split = data[data["Golgi apparatus"] == 1.0]
    data_split = golgi_apparatus_split["Sequence"].tolist()
    golgi_apparatus_trigram = Trigram_Model(data_split,alphabet,k)
    f = open('golgi_apparatus_trigram.pkl', 'wb')
    pickle.dump(golgi_apparatus_trigram,f)
    f.close()

    #Peroxisome
    peroxisome_split = data[data["Peroxisome"] == 1.0]
    data_split = peroxisome_split["Sequence"].tolist()
    peroxisome_trigram = Trigram_Model(data_split,alphabet,k)
    f = open('peroxisome_trigram.pkl', 'wb')
    pickle.dump(peroxisome_trigram,f)
    f.close()

