# UlyssesNER-Br: Codes
## Requirements
- Python 3
- Pearl 

## Instructions
1. The file ```0_EDA.ipynb``` performs the initial statistical analyses. The file should be executed, updating the DIR directory initially.
2. The file ```1_hmm.py``` run the training using Hidden Markov Model (HMM). The size of the training and test sets will appear in the terminal, save these numbers. This will generate files named "predictions_file_something".
3. The file ```2_conlleval.perl``` evaluates the results of processing CoNLL-2000 shared task (author: Erik Tjong Kim Sang). <br> Run the following command in terminal:
```
perl 2_conlleval.perl < predictions_file_something_1 > scores_file_1
perl 2_conlleval.perl < predictions_file_something_2 > scores_file_2
(..)
perl 2_conlleval.perl < predictions_file_final > scores_file_final
```
4. The file ```3_metrics.py``` extracts the overall metrics from the file generated by the 2_conlleval.perl script. At the end, a latex line will appear on the screen, save it. Rename the scores_file_final file to "scores_modelused_myname" or another one of your choice.
5. The file ```nltk_data``` folder and the ```4_crf.py``` file are used to the training using Conditional Random Fields (CRF). The folder which should be in the default location where nltk downloads external files. After that, run the ```4_crf.py``` file, updating the DIR directory initially
6. Repeat steps 3 and 4, renaming the generated files again.
- The generated files will have the results found.

## Authors
Hidelberg O. Albuquerque, Rosimeire Costa, Gabriel Silvestre, Ellen Souza, Nádia F. F. da Silva, Douglas Vitório, Gyovana Moriyama, Lucas Martins, Luiza Soezima, Augusto Nunes, Felipe Siqueira, João P. Tarrega, Joao V. Beinotti, Marcio Dias, Matheus Silva, Miguel Gardini, Vinicius Silva, Andrré C. P. L. F. de Carvalho and Adriano L. I. Oliveira.

## Citation
If you use our work, please cite:
```
@inproceedings{UlyssesNER-Br,
  title={UlyssesNER-Br: A Corpus of Brazilian Legislative Documents for Named Entity Recognition}, 
  author={Albuquerque, Hidelberg O. and Costa, Rosimeire and Silvestre, Gabriel and Souza, Ellen and da Silva, Nádia F. F. and Vitório, Douglas and Moriyama, Gyovana and Martins, Lucas and Soezima, Luiza and Nunes, Augusto and Siqueira, Felipe and Tarrega, João P. and Beinotti, Joao V. and Dias, Marcio and Silva, Matheus and Gardini, Miguel and Silva, Vinicius and de Carvalho, André C. P. L. F. and Oliveira, Adriano L. I.},
  booktitle={Computational Processing of the Portuguese Language},
  year={2022},
  publisher={Springer International Publishing},
  isbn={978-3-030-98305-5},
  doi={https://doi.org/10.1007/978-3-030-98305-5_1}
}
```
