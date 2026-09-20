import numpy as np
import pandas as pd
from Trigram_Class import Trigram_Model
import pickle


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

#ubiquitin
sequence = 'MAAGGAEGGPGPSAAMGDCAEIKSQFRTREGFYKLLPGDATRRSGPTSAQTPAPPQPTQPPPGPAAASGPGAAGPASSPPPAGPGPGPALPAVRLSLVRLGDPDGAGEPPSTPSGLGAGGDRVCFNLGRELYFYPGCCRSGSQRSIDLNKPIDKRIYKGTQPTCHDFNQFTAATETISLLVGFSAGQVQYLDLIKKDTSKLFNEERLIDKTKVTYLKWLPESESLFLASHASGHLYLYNVSHPCTSTPPQYSLLKQGEGFAVYAAKSKAPRNPLAKWAVGEGPLNEFAFSPDGRHLACVSQDGCLRVFHFDSMLLRGLMKSYFGGLLCVCWSPDGRYVVTGGEDDLVTVWSFTEGRVVARGHGHKSWVNAVAFDPYTTRAEEAASASADGDPSGEEEEPEVTSSDTGAPVSPLPKAGSITYRFGSAGQDTQFCLWDLTEDVLSPHPSLARTRTLPGTPGATPPASGSSRAGETGAGPLPRSLSRSNSLPHPAGGGKAGGPSASMEPGIPFSIGRFATLTLQERRDRGAEKEHKRYHSLGNISRGGSGGNSSNDKLSGPAPRSRLDPAKVLGTALCPRIHEVPLLEPLVCKKIAQERLTVLLFLEDCIITACQEGLICTWARPGKAFTDEETEAQAGQASWPRSPSKSVVEGISSQPGSSPSGTVV'

print(cytoplasm_trigram.compute_loss(sequence))
print(nucleus_trigram.compute_loss(sequence))
print(extracellular_trigram.compute_loss(sequence))
print(cellmembrane_trigram.compute_loss(sequence))
print(mitochondrion_trigram.compute_loss(sequence))
print(plastid_trigram.compute_loss(sequence))
print(endoplasmicreticulum_trigram.compute_loss(sequence))
print(lysosome_vacuole_trigram.compute_loss(sequence))
print(golgi_apparatus_trigram.compute_loss(sequence))
print(peroxisome_trigram.compute_loss(sequence))
