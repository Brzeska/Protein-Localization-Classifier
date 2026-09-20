The 'protein localization classifier' is a trigram based classifier which
takes an amino acid sequence as an input and predicts the localization of the
corresponding protein in the cell.

The classifier uses ten separate amino acid-level trigram character models, 
each one trained on a localization-filtered subset of DeepLoc 2.0's protein
localization dataset. Thus there is one trigram model for each localization. Novel
sequences are then passed through each of the ten models, yielding ten different
negative log likelihoods. The lowest of these is selected by the classifier as the
predicted localization.

The trigram models were implemented as simple count matrices from which a probabilit 
matrix was calculated.

Cross validation yielded maximum dev accuracy when the count matrix was initialized
with model smoothing factor k=7. Further improvements could likely be made by having
multiple smoothing factors which are not uniform across the different trigram models.

Best dev accuracy was 51.14%, and the test accuracy for the same hyperparameter was
51.19%. This is considerably worse than state of the art protein language models,
which score ~75–80% on this dataset. However, it is considerably better than 
random guessing (~10%) or other naive strategies like 'cytoplasm only' (~35%). A
suboptimal accuracy is also to be expected given that a trigram model is by nature
blind to large scale structure in the data.

The primary goals of this project were achieved: to work with a real biological
dataset, and to create a model which was more informative than a completely naive
approach.
