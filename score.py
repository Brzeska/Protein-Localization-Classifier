from Trigram_Class import Trigram_Model
import pickle
import torch

def score(data,confmat=False):
    '''
    scores accuracy of a pregenerated model
    confmat (false by default) determines whether to generate a confusion matrix
    '''
    print(type(data))

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
    
    if confmat:
        conf_counts = torch.zeros((10,10),dtype=torch.int32)

    for i in range(len(data)):
        
        #for data instance, collect all labels with 1.0 (possibly more than one)
        current_labels = [] 
        for x in range(4,14):
            if data.iloc[i,x] == 1.0:
                current_labels.append(localizations[x-4])
        
        #save to labels
        labels.append(current_labels)
        
        #get sequence
        sequence = data.iloc[i,14]
        sequences.append(sequence)
        
        #get id
        ids.append(data.iloc[i,0])
        
        #get losses
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

        #find minimum loss: this defines classification
        minimum_index = 0
        minimum = losses[minimum_index]
        for i in range(1,len(losses)):
            if losses[i] < minimum:
                minimum = losses[i]
                minimum_index = i
        
        classification = localizations[minimum_index]
        
        #log to classifications
        predictions.append(classification)
        
        #update confusion counts matrix
        if confmat:
            #
            #rows are gt, what is the row?
            #rows are position of elements of current_labels in localizations
            rowVals = []
            for cl in current_labels:
                rowVals.append(localizations.index(cl))
            
            #columns are model predictions, what is the prediction?
            column = localizations.index(classification)

            for rv in rowVals:
                conf_counts[rv,column] += 1
            
            per_class_accuracies = []
            conf_probs = conf_counts/conf_counts.sum(1,keepdim=True)
            for i in range(len(localizations)):
                per_class_accuracies.append(conf_probs[i,i].item())


    #calculate correct percentage
    right = 0
    wrong = 0
    for i in range(len(data)):
        if predictions[i] in labels[i]:
            right += 1
        else:
            wrong += 1

    if confmat:
        print(localizations)
        print(conf_counts)
        print()
        print(conf_counts/conf_counts.sum(1,keepdim=True))
        print(per_class_accuracies)


        for i in range(len(localizations)):
            print(f'model accuracy for class {localizations[i]}: {per_class_accuracies[i]} (number of instances {conf_counts.sum(1,keepdim=False)[i]})')
    return right/(right+wrong)
