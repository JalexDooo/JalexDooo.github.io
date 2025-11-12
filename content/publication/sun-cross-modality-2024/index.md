---
title: The cross-modality survival prediction method of glioblastoma based on dual-graph
  neural networks
authors:
- Jindong Sun
- Yanjun Peng
date: '2024-11-01'
publishDate: '2025-11-12T15:43:53.147671Z'
publication_types:
- article-journal
publication: '*Expert Systems with Applications*'
doi: 10.1016/j.eswa.2024.124394
abstract: Glioma, the highly lethal malignant brain tumor originating from abnormal
  proliferation of glial cells, exhibits a varied overall survival rate influenced
  by multiple factors. Accurate prediction rate of survival periods assist physicians
  in selecting the most suitable treatment plans to improve patient overall survival
  (OS) rates. The paper proposes a dual-graph neural network (GNN) with manually constructed
  feature relational graph for OS prediction and inference of different survival periods
  in glioblastoma based on cross-modality data. Specifically, five radiomic features
  from magnetic resonance imaging are extracted to construct two sets of feature relational
  graphs. The main GNN is utilized to extract comprehensive features, including age,
  brain MRI features, and radiomics features of gliomas. The branch GNN additionally
  extracts radiomics features specific to gliomas, constraining the feature weights
  of the main GNN through attention mechanisms. Pretraining an autoencoder to extract
  deep features from patient text information. The text features and image features
  are then reorganized based on features from different modalities through a transformer
  decoder. Finally, a multi-layer perceptron is utilized for regression and classification,
  thus enabling the classification and prediction of patient survival. The proposed
  method achieved an accuracy of 0.586 for classifying and predicting the survival
  of glioma patients in the short, medium, and long term on the BraTS20 dataset, outperforming
  state-of-the-art methods.
tags:
- /unread
- /未读
links:
- name: URL
  url: https://linkinghub.elsevier.com/retrieve/pii/S0957417424012600
---
