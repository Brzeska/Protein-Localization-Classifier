#Classical trigram character model with explicit probability matrix
#and model smoothing

import numpy as np
import matplotlib.pyplot as plt
import torch

#chars = open('proteinogenics.txt').read()
#print(chars)

class Trigram_Model:
    def __init__(self,data,alphabet,k):
        
        self.data = data #data should be passed as word/sequence list
        self.k = k #smoothing hyperparameter

        #alphabet should be passed as list
        #could be derived from data, but an explicit pass ensures
        #no discrepancies between different class instantiations
        self.alphabet = list(alphabet)
        self.alphabet += '.' #buffer character for start/end of sequence
        
        #construct bigram list
        self.bigrams = []
        for i in self.alphabet:
            for j in self.alphabet:
                self.bigrams.append(i+j)

        #construct mappings of bigrams to indices
        self.btoi = {s:i for i,s in enumerate(self.bigrams)}
        self.itob = {i:s for i,s in enumerate(self.bigrams)}

        #construct mappings of characters to indices
        self.ctoi = {s:i for i,s in enumerate(self.alphabet)}
        self.itoc = {i:s for i,s in enumerate(self.alphabet)}

        #Construct count matrix, initialized as ones for model smoothing
        self.N = torch.ones((len(self.alphabet)**2,len(self.alphabet)),dtype=torch.int32)*k

        #Start populating count matrix with instances
        for seq in self.data:
            chs = ['.','.'] + list(seq) + ['.']
            for ch1, ch2, ch in zip(chs, chs[1:],chs[2:]):
                bi = ch1 + ch2
                self.N[self.btoi[bi],self.ctoi[ch]]+=1

        #Derive probability matrix from count matrix
        self.P = torch.zeros((len(self.alphabet)**2,len(self.alphabet)))
        self.P += self.N/self.N.sum(1,keepdim=True)

    def display(self):
        print(self.alphabet)
        print(f'length: {len(self.alphabet)}')
        print(self.bigrams)
        print(f'length: {len(self.bigrams)}')
        print(self.P)
        #print(self.N)

    def compute_loss(self,sequence):
        normalization = len(sequence)
        p_sum = 0
        for i in zip(sequence,sequence[1:],sequence[2:]):
            bigram_index = self.btoi[i[0] + i[1]]
            label_index = self.ctoi[i[2]]
            label_probability = float(self.P[bigram_index,label_index])
            nll = -np.log(label_probability)
            p_sum += nll
        return p_sum/normalization
            

    def show_probability(self):
        '''
        prints a heat map of probability matrix
        '''
        plt.imshow(self.P, cmap='hot',aspect='auto',interpolation='nearest') 
        plt.colorbar()
        plt.show()
