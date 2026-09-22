from Trigram_Class import Trigram_Model
import pickle

def train(data, k, N_matrix=None,out=False):
    '''
    Splits the passed data along localization and trains
    Bespoke trigram model on each localization split
    If a list of ten count matrices is passed via N_matrix,
    The trigrams will use these matrices instead of generating
    their own (good to avoid regeneration during hyperparameter
    tuning). if out is set to true, a corresponding 10-long list
    of count matrices is returned.

    Note: on next refactor, make this loop based instead
    of ten almost-repeating blocks of code.
    '''

    alphabet = open('proteinogenics.txt').read().splitlines()
    alphabet += ['X','B']

    #Cytoplasm
    cytoplasm_split = data[data["Cytoplasm"] == 1.0]
    data_split = cytoplasm_split["Sequence"].tolist()
    cytoplasm_trigram = Trigram_Model(data_split,alphabet,k,N_matrix=N_matrix[0] if N_matrix is not None else None)
    f = open('cytoplasm_trigram.pkl', 'wb')
    pickle.dump(cytoplasm_trigram,f)
    f.close()

    #Nucleus
    nucleus_split = data[data["Nucleus"] == 1.0]
    data_split = nucleus_split["Sequence"].tolist()
    nucleus_trigram = Trigram_Model(data_split,alphabet,k,N_matrix=N_matrix[1] if N_matrix is not None else None)
    f = open('nucleus_trigram.pkl', 'wb')
    pickle.dump(nucleus_trigram,f)
    f.close()

    #Extracellular
    extracellular_split = data[data["Extracellular"] == 1.0]
    data_split = extracellular_split["Sequence"].tolist()
    extracellular_trigram = Trigram_Model(data_split,alphabet,k,N_matrix=N_matrix[2] if N_matrix is not None else None)
    f = open('extracellular_trigram.pkl', 'wb')
    pickle.dump(extracellular_trigram,f)
    f.close()

    #Cell membrane
    cellmembrane_split = data[data["Cell membrane"] == 1.0]
    data_split = cellmembrane_split["Sequence"].tolist()
    cellmembrane_trigram = Trigram_Model(data_split,alphabet,k,N_matrix=N_matrix[3] if N_matrix is not None else None)
    f = open('cellmembrane_trigram.pkl', 'wb')
    pickle.dump(cellmembrane_trigram,f)
    f.close()

    #Mitochondrion
    mitochondrion_split = data[data["Mitochondrion"] == 1.0]
    data_split = mitochondrion_split["Sequence"].tolist()
    mitochondrion_trigram = Trigram_Model(data_split,alphabet,k,N_matrix=N_matrix[4] if N_matrix is not None else None)
    f = open('mitochondrion_trigram.pkl', 'wb')
    pickle.dump(mitochondrion_trigram,f)
    f.close()

    #Plastid
    plastid_split = data[data["Plastid"] == 1.0]
    data_split = plastid_split["Sequence"].tolist()
    plastid_trigram = Trigram_Model(data_split,alphabet,k,N_matrix=N_matrix[5] if N_matrix is not None else None)
    f = open('plastid_trigram.pkl', 'wb')
    pickle.dump(plastid_trigram,f)
    f.close()

    #Endoplasmic reticulum
    endoplasmicreticulum_split = data[data["Endoplasmic reticulum"] == 1.0]
    data_split = endoplasmicreticulum_split["Sequence"].tolist()
    endoplasmicreticulum_trigram = Trigram_Model(data_split,alphabet,k,N_matrix=N_matrix[6] if N_matrix is not None else None)
    f = open('endoplasmicreticulum_trigram.pkl', 'wb')
    pickle.dump(endoplasmicreticulum_trigram,f)
    f.close()

    #Lysosome/Vacuole
    lysosome_vacuole_split = data[data["Lysosome/Vacuole"] == 1.0]
    data_split = lysosome_vacuole_split["Sequence"].tolist()
    lysosome_vacuole_trigram = Trigram_Model(data_split,alphabet,k,N_matrix=N_matrix[7] if N_matrix is not None else None)
    f = open('lysosome_vacuole_trigram.pkl', 'wb')
    pickle.dump(lysosome_vacuole_trigram,f)
    f.close()

    #Golgi apparatus
    golgi_apparatus_split = data[data["Golgi apparatus"] == 1.0]
    data_split = golgi_apparatus_split["Sequence"].tolist()
    golgi_apparatus_trigram = Trigram_Model(data_split,alphabet,k,N_matrix=N_matrix[8] if N_matrix is not None else None)
    f = open('golgi_apparatus_trigram.pkl', 'wb')
    pickle.dump(golgi_apparatus_trigram,f)
    f.close()

    #Peroxisome
    peroxisome_split = data[data["Peroxisome"] == 1.0]
    data_split = peroxisome_split["Sequence"].tolist()
    peroxisome_trigram = Trigram_Model(data_split,alphabet,k,N_matrix=N_matrix[9] if N_matrix is not None else None)
    f = open('peroxisome_trigram.pkl', 'wb')
    pickle.dump(peroxisome_trigram,f)
    f.close()

    if out:
        matrices = []
        matrices.append(cytoplasm_trigram.return_counts())
        matrices.append(nucleus_trigram.return_counts())
        matrices.append(extracellular_trigram.return_counts())
        matrices.append(cellmembrane_trigram.return_counts())
        matrices.append(mitochondrion_trigram.return_counts())
        matrices.append(plastid_trigram.return_counts())
        matrices.append(endoplasmicreticulum_trigram.return_counts())
        matrices.append(lysosome_vacuole_trigram.return_counts())
        matrices.append(golgi_apparatus_trigram.return_counts())
        matrices.append(peroxisome_trigram.return_counts())
        
        return matrices
