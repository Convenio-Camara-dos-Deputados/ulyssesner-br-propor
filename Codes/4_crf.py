import operator
import os
import random
import functools
import collections
import joblib
import random
import nltk
import sklearn
import sklearn_crfsuite
import numpy as np
from itertools import chain
from nltk.corpus import PlaintextCorpusReader 
from nltk import sent_tokenize, word_tokenize, pos_tag 
from nltk.stem import WordNetLemmatizer
from sklearn.model_selection import KFold


random.seed(1999)

# nltk.download('averaged_perceptron_tagger')
# nltk.download('punkt')


#função do tamanho da palavra (returna True se for maior que 4)
def length(word):
    if len(word) >= 4: 
        tamanho = True
    else:
        tamanho = False
    return tamanho

teste_tagger = joblib.load('POS_tagger_brill.pkl')
def postag(word):
    phrase = word
    postag = teste_tagger.tag(word_tokenize(phrase))
    return postag[0][1]

#função do tamanho da palavra
def length(word):
    if len(word) >= 5: 
        tamanho = True
    else:
        tamanho = False
    return tamanho

#tamanho da setenca
def tamsent(sent,i):
    conta = []
    valor = []
    for i in range(len(sent)):
        conta.append(sent[i].count(sent[i][0]))
    valor = sum(conta)
    return valor

#frequencia da palavra na sentenca
def freqwordsent(sent,word):
    conta = []
    valor = []
    for j in range(len(sent)):
        conta.append(sent[j].count(word))
    valor = sum(conta)
    return valor


def word2features(sent, i):
    word = sent[i][0]  
    features = {
        'bias': 1.0,
        'word': word,
        'word.lower()': word.lower(),
        'word[-3:]': word[-3:],
        'word[-2:]': word[-2:],
        'word[-1:]': word[-1:],        
        'word[:1]': word[:1],
        'word[:2]': word[:2],
        'word[:3]': word[:3],
        'word.isupper()': word.isupper(),
        'word.istitle()': word.istitle(),
        'word.isdigit()': word.isdigit(),
        'postag': postag(word),
        'postag[:2]': postag(word)[:1],
        'postag[:2]': postag(word)[:2],
        'tamanho': length(word),
        'word.isalnum()' : word.isalnum(),
        'len(word)': len(word),
        'tamanho(sent)': tamsent(sent,i),
        'freqwordsent' : freqwordsent(sent,word),   
    }
    if i > 0:
        word1 = sent[i-1][0]
        features.update({
            '-1:word': word1,
            '-1:word.lower()': word1.lower(),
            '-1:word.istitle()': word1.istitle(),
            '-1:word.isdigit()': word1.isdigit(),
            '-1:word.isupper()': word1.isupper(),
            '-1:postag': postag(word1),
            '-1:postag[:2]': postag(word1)[:1],
            '-1:postag[:2]': postag(word1)[:2],
            '-1:word[-3:]': word1[-3:],
            '-1:word[-2:]': word1[-2:],
            '-1:word[-1:]': word1[-1:],
            '-1:word[:1]': word1[:1],
            '-1:word[:2]': word1[:2],
            '-1:word[:3]': word1[:3],
            '-1:len(word)': len(word1),
            '-1:word.isalnum()' : word1.isalnum(),
        })
    else:
        features['Inicio'] = True

    if i > 1:
        word2 = sent[i-2][0]
        features.update({
            '-2:word': word2,
            '-2:word.lower()': word2.lower(),
            '-2:word.istitle()': word2.istitle(),
            '-2:word.isdigit()': word2.isdigit(),
            '-2:word.isupper()': word2.isupper(),
            '-2:postag': postag(word2),
            '-2:postag[:2]': postag(word2)[:2],
            '-2:word[-3:]': word2[-3:],
            '-2:word[-2:]': word2[-2:],
            '-2:word[-1:]': word2[-1:],
            '-2:word[:1]': word2[:1],
            '-2:word[:2]': word2[:2],
            '-2:word[:3]': word2[:3],
            '-2:len(word)': len(word2),
            '-2:word.isalnum()' : word2.isalnum(),

        })
    if i < len(sent)-1:
        word3 = sent[i+1][0]
        features.update({
            '+1:word': word3,
            '+1:word.lower()': word3.lower(),
            '+1:word.istitle()': word3.istitle(),
            '+1:word.isdigit()': word3.isdigit(),
            '+1:word.isupper()': word3.isupper(),
            '+1:postag': postag(word3),
            '+1:postag[:2]': postag(word3)[:2],
            '+1:word[-3:]': word3[-3:],
            '+1:word[-2:]': word3[-2:],
            '+1:word[-1:]': word3[-1:],
            '+1:word[:1]': word3[:1],
            '+1:word[:2]': word3[:2],
            '+1:word[:3]': word3[:3],
            '+1:len(word)': len(word3),
            '+1:word.isalnum()' : word3.isalnum()
            })
    else:
        features['Final'] = True
   
    if i < len(sent)-2:
        word4 = sent[i+2][0]
        features.update({
            '+2:word': word4,
            '+2:word.lower()': word4.lower(),
            '+2:word.istitle()': word4.istitle(),
            '+2:word.isdigit()': word4.isdigit(),
            '+2:word.isupper()': word4.isupper(),
            '+2:postag': postag(word4),
            '+2:postag[:2]': postag(word4)[:2],
            '+2:word[-3:]': word4[-3:],
            '+2:word[-2:]': word4[-2:],
            '+2:word[-1:]': word4[-1:],
            '+2:word[:1]': word4[:1],
            '+2:word[:2]': word4[:2],
            '+2:word[:3]': word4[:3],
            '+2:len(word)': len(word4),
            '+2:word.isalnum()' : word4.isalnum()
        })     

    return features

def sent2features(sent):
    return [word2features(sent, i) for i in range(len(sent))]

def sent2labels(sent):
    return [label for token, label in sent]

def sent2tokens(sent):
    return [token for token, label in sent]



lista = [
        'bias',
        'word',
        'word.lower()',
        'word[-3:]',
        'word[-2:]',
        'word[-1:]',
        'word[:1]',
        'word[:2]',
        'word[:3]',
        'word.isupper()',
        'word.istitle()',
        'word.isdigit()',
        'postag','postag[:2]',
        'postag[:2]',
        'tamanho',
        'word.isalnum()',
        'len(word)',
        'tamanho(sent)',
        'freqwordsent',
        '-1:word',
        '-1:word.lower()',
        '-1:word.istitle()',
        '-1:word.isdigit()',
        '-1:word.isupper()',
        '-1:postag',
        '-1:postag[:2]',
        '-1:postag[:2]',
        '-1:word[-3:]',
        '-1:word[-2:]',
        '-1:word[-1:]',
        '-1:word[:1]',
        '-1:word[:2]',
        '-1:word[:3]',
        '-1:len(word)',
        '-1:word.isalnum()',
        '-2:word',
        '-2:word.lower()',
        '-2:word.istitle()',
        '-2:word.isdigit()',
        '-2:word.isupper()',
        '-2:postag',
        '-2:postag[:2]',
        '-2:word[-3:]',
        '-2:word[-2:]',
        '-2:word[-1:]',
        '-2:word[:1]',
        '-2:word[:2]',
        '-2:word[:3]',
        '-2:len(word)',
        '-2:word.isalnum()',
        '+1:word',
        '+1:word.lower()',
        '+1:word.istitle()',
        '+1:word.isdigit()',
        '+1:word.isupper()',
        '+1:postag',
        '+1:postag[:2]',
        '+1:word[-3:]',
        '+1:word[-2:]',
        '+1:word[-1:]',
        '+1:word[:1]',
        '+1:word[:2]',
        '+1:word[:3]',
        '+1:len(word)',
        '+1:word.isalnum()',
        '+2:word',
        '+2:word.lower()',
        '+2:word.istitle()',
        '+2:word.isdigit()',
        '+2:word.isupper()',
        '+2:postag',
        '+2:postag[:2]',
        '+2:word[-3:]',
        '+2:word[-2:]',
        '+2:word[-1:]',
        '+2:word[:1]',
        '+2:word[:2]',
        '+2:word[:3]',
        '+2:len(word)',
        '+2:word.isalnum()'
]

# DIR = "./dados-sem-agrupar/PLs/"
# DIR = "./dados-agrupados/PLs/"
DIR = "/home/berg/Insync/bergsiloe-shared-with-me/UFRPE_Shared/Doutorado/Anotações Inception/Anotações_Scripts/Fase2/2_Categorias_Joined/"

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

# divisão do conjunto de dados
train = all_data[:train_size]
test = all_data[train_size:]

# 5-fold no conjunto de treinamento
kfold = KFold(n_splits=5)
train = np.array(train, dtype=object)
i = 1
for t, tt in kfold.split(train):
    to_train = train[t].tolist()
    to_val = train[tt].tolist()
    
    X_train = [sent2features(s) for s in to_train]
    y_train = [sent2labels(s) for s in to_train]

    X_test = [sent2features(s) for s in to_val]
    
    crf = sklearn_crfsuite.CRF(
        algorithm='lbfgs',
        c1=0.9,
        c2=0.4,
        max_iterations=100,
        all_possible_transitions=True
    )
    crf.fit(X_train, y_train)
    
    ycrf = crf.predict(X_test)
    
    crf_file = ""
    for preds, true in zip(ycrf, to_val):
        for j in range(len(preds)):
            crf_file += true[j][0] + " " + true[j][1] + " " + preds[j] + "\n"
        crf_file += "\n"
    with open(f"predictions_file_{i}", "w") as f:
        f.write(crf_file)
    i += 1

# Re-treinamento do modelo no conjunto de treinamento completo
X_train = [sent2features(s) for s in train]
y_train = [sent2labels(s) for s in train]

X_test = [sent2features(s) for s in test]
y_test = [sent2labels(s) for s in test]

crf = sklearn_crfsuite.CRF(
    algorithm='lbfgs',
    c1=0.9,
    c2=0.4,
    max_iterations=100,
    all_possible_transitions=True
)
crf.fit(X_train, y_train)

ycrf = crf.predict(X_test)

# Salva as predições
crf_file = ""
for preds, true in zip(ycrf, test):
    for j in range(len(preds)):
        crf_file += true[j][0] + " " + true[j][1] + " " + preds[j] + "\n"
    crf_file += "\n"
    
with open("/content/predictions_crf/predictions_file_final", "w") as f:
    f.write(crf_file)

#ao final, repetir: 1) pearl, 2) colocar as predições em files_to_metrics, 3) rodar as métricas $) renomear o ultimo arquivo
