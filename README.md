## Overview

The 'protein localization classifier' is a trigram based classifier which
takes an amino acid sequence as an input and predicts the localization of the
corresponding protein in the cell.

The classifier uses ten separate amino acid-level trigram character models, 
each one trained on a localization-filtered subset of DeepLoc 2.0's protein
localization dataset. Thus there is one trigram model for each localization. Novel
sequences are then passed through each of the ten models, yielding ten different
negative log likelihoods. The lowest of these is selected by the classifier as the
predicted localization.

The trigram models were implemented as simple count matrices from which a 
probability matrix was calculated.

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

## Data
Training data is the Swiss-Prot train/validation set from **DeepLoc 2.0**:
[services.healthtech.dtu.dk/services/DeepLoc-2.0](https://services.healthtech.dtu.dk/services/DeepLoc-2.0/)

Thumuluri V., Almagro Armenteros J.J., Johansen A.R., Nielsen H., Winther O.
(2022). DeepLoc 2.0: multi-label subcellular localization prediction using
protein language models. *Nucleic Acids Research*, 50(W1), W228–W234.
[doi.org/10.1093/nar/gkac278](https://doi.org/10.1093/nar/gkac278)

## How to run

First navigate to repo through CLI. First run `partition_data.py` to split the 
dataset into five separate, homology aware partitions. The first three (0–2) 
are used as the training set, 3 is used as dev set, and 4 as test set.

Once the data is partitioned, `localization_split_and_train.py` concatenates the 
training set, splits it along localizations, and trains ten trigram models, one
on each localization subset. This step is essential since the trained models are
not included in the repo. Should only take a minute or two.

To have the model classify a given sequence, open `classifier.py` and enter
the sequence as a string on line 20. Delete the placeholder sequence first.

To repeat cross validation, use `localization_split_and_train.py` and 
`dev_testing.py`. Run the former to train the model, and the latter to get
an accuracy on the dev set. To change the only hyperparameter, go into 
`Trigram_Class.py` and change the constant which terminates line 37. From my
own testing, 7 achieved the best accuracy, but between 5–15 were all comparable.

To get a test accuracy, just run `final_test.py`

## AI Usage

I used claude code to upload the MIT license, for python syntax and biology reference(in particular for a pandas refresher), and as a general sanity check at the end. All code and design were my own in both concept and execution.
