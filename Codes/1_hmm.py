'''
This file was developed as part of the project reported in the paper below. 
If you use our work, please cite our paper.

- Title: UlyssesNER-Br: a Corpus of Brazilian Legislative Documents for Named Entity Recognition
- Authors: Hidelberg O. Albuquerque, Rosimeire Costa, Gabriel Silvestre, Ellen Souza, Nádia F. F. da Silva, Douglas Vitório, Gyovana Moriyama, Lucas Martins, Luiza Soezima, Augusto Nunes, Felipe Siqueira, João P. Tarrega, Joao V. Beinotti, Marcio Dias, Matheus Silva, Miguel Gardini, Vinicius Silva, Andrré C. P. L. F. de Carvalho and Adriano L. I. Oliveira.
- In: International Conference on the Computational Processing of Portuguese ― PROPOR 2022 (March 2022)
'''

'''
Please, pay attention:
The size of the training and test sets will appear in the terminal, save these numbers. 
This will generate 6 files named "predictions_file_something"
'''

import operator
import os
import random
import functools
import collections
import nltk
import numpy as np
from nltk.tag.hmm import HiddenMarkovModelTrainer
from sklearn.model_selection import KFold

random.seed(1999)

#UPDATE the directory
DIR = "./dados-sem-agrupar/PLs/"
all_files = os.listdir(DIR)

def process_conll_file(location:str)->list:
    with open(location, "r") as f:
        data = f.read()
    data = data.split("\n\n")
    data = list(map(lambda x:x.split("\n"), data))
    data.pop()
    data = list(map(lambda x:[operator.itemgetter(*[0, -1])(y.split(" ")) for y in x], data))
    return data

def combine_files(locations:list)->list:
    extended = []
    for f in locations:
        f = DIR + f
        extended.extend(process_conll_file(f))
    return extended

all_data = combine_files(all_files)
random.shuffle(all_data)

train_size = int(0.75*len(all_data))

train = all_data[:train_size]
test = all_data[train_size:]

print(f"Tamanho do treino: {len(train)}")
print(f"Tamanho do teste: {len(test)}")

# Remove o rótulo do conjunto de teste
def retrieve_sents(data:list)->list:
    return list(map(lambda x:[w for w,t in x], data))

# 5-fold no conjunto de treinamento
kfold = KFold(n_splits=5)
train = np.array(train, dtype=object)
i = 1
for t, tt in kfold.split(train):
    to_train = train[t].tolist()
    to_val = train[tt].tolist()
    unlab_test = retrieve_sents(to_val)
    hmm = HiddenMarkovModelTrainer().train_supervised(to_train)
    yhmm = hmm.tag_sents(unlab_test)
    hmm_file = ""
    for preds, true in zip(yhmm, to_val):
        for j in range(len(preds)):
            hmm_file += true[j][0] + " " + true[j][1] + " " + preds[j][1] + "\n"
        hmm_file += "\n"
    with open(f"predictions_file_{i}", "w") as f:
        f.write(hmm_file)
    i += 1
    
unlab_test = retrieve_sents(test)
train = train.tolist()
hmm = HiddenMarkovModelTrainer().train_supervised(train)
yhmm = hmm.tag_sents(unlab_test)
hmm_file = ""
for preds, true in zip(yhmm, test):
    for j in range(len(preds)):
        hmm_file += true[j][0] + " " + true[j][1] + " " + preds[j][1] + "\n"
    hmm_file += "\n"
with open("predictions_file_final", "w") as f:
    f.write(hmm_file)
