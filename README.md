# UlyssesNER-Br: a Corpus of Brazilian Legislative Documents for Named Entity Recognition
Repository at paper "UlyssesNER-Br", presented in International Conference on the Computational Processing of Portuguese ― PROPOR 2022.

## Abstract & Keywords
The amount of legislative documents produced within the past decade has risen dramatically, making it difficult for law practitioners to consult and update legislation. Named Entity Recognition (NER) systems have the untapped potential to extract information from legal documents, which can improve information retrieval and decision-making processes. We introduce the UlyssesNER-Br, a corpus of Brazilian Legislative Documents for NER with quality baselines. The presented corpus consists of bills and legislative consultations from Brazilian Chamber of Deputies. We implemented Conditional Random Field (CRF) and Hidden Markov Model (HMM) models, and the promising F1-score of 80.8% in the analysis by categories and 81.04% in the analysis by types, was achieved with the CRF model. The entities with the best average F1-score results were “FUNDlei” and “DATA”, and the ones with the worst results were “EVENTO” and “PESSOAgrupoind”. The corpus was also evaluated using a BiLSTM-CRF and Glove architectures provided by the pioneering state-of-the-art paper, achieving F1-score of 76.89% in the analysis by categories and 59.67% in the analysis by types. 

*Keywords*: Annotation Schema · Named Entity Recognition · Legal Information Retrieval.

## Authors
Hidelberg O. Albuquerque, Rosimeire Costa, Gabriel Silvestre, Ellen Souza, Nádia F. F. da Silva, Douglas Vitório, Gyovana Moriyama, Lucas Martins, Luiza Soezima, Augusto Nunes, Felipe Siqueira, João P. Tarrega, Joao V. Beinotti, Marcio Dias, Matheus Silva, Miguel Gardini, Vinicius Silva, Andrré C. P. L. F. de Carvalho and Adriano L. I. Oliveira.

## Paper:
Paper: https://link.springer.com/chapter/10.1007/978-3-030-98305-5_1

## Acknowledgements
This research is carried out in the context of the Ulysses Project, of the Brazilian Chamber of Deputies. Ellen Souza and Nadia Félix are supported by FAPESP , agreement between USP and the Brazilian Chamber of Deputies. André C. P. L. F. de Carvalho and Adriano L. I. Oliveira are supported by CNPq. To the Brazilian Chamber of Deputies and to research funding agencies, to which we express our gratitude for supporting the research.

> **_NOTE:_**  We were recently informed about the presence of duplication in some sentences in the UlyssesNER-BR corpus. After careful verification, we confirmed that there was indeed a duplication of a specific document.
> In response to this observation, we conducted a detailed review of the annotations in these documents. We note that, despite the presence of redundant content, the consistency of the annotations remained unchanged.
> We thank the UFRGS collaborators Rafael O. Nunes, Dennis G. Balreira, Andre S. Spritzer and Carla Maria D.S. Freitas for alerting us to this issue. This interaction is essential for us to continue improving the quality and accuracy of our work.

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
