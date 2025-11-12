---
title: 'TAUNet: a triple-attention-based multi-modality MRI fusion U-net for cardiac
  pathology segmentation'
authors:
- Dapeng Li
- Yanjun Peng
- Yanfei Guo
- Jindong Sun
date: '2022-06-01'
publishDate: '2025-11-12T15:43:53.131156Z'
publication_types:
- article-journal
publication: '*Complex & Intelligent Systems*'
doi: 10.1007/s40747-022-00660-6
abstract: Automated segmentation of cardiac pathology in MRI plays a signiﬁcant role
  for diagnosis and treatment of some cardiac disease. In clinical practice, multi-modality
  MRI is widely used to improve the cardiac pathology segmentation, because it can
  provide multiple or complementary information. Recently, deep learning methods have
  presented implausible performance in multi-modality medical image segmentation.
  However, how to fuse the underlying multi-modality information effectively to segment
  the pathology with irregular shapes and small region at random locations, is still
  a challenge task. In this paper, a triple-attention-based multi-modality MRI fusion
  U-Net was proposed to learn complex relationship between different modalities and
  pay more attention on shape information, thus to achieve improved pathology segmentation.
  First, three independent encoders and one fusion encoder were applied to extract
  speciﬁc and multiple modality features. Secondly, we concatenate the modality feature
  maps and use the channel attention to fuse speciﬁc modal information at every stage
  of the three dedicate independent encoders, then the three single modality feature
  maps and channel attention feature maps are together concatenated to the decoder
  path. Spatial attention was adopted in decoder path to capture the correlation of
  various positions. Once more, we employ shape attention to focus shape-dependent
  information. Lastly, the training approach is made efﬁcient by introducing deep
  supervision mechanism with object contextual representations block to ensure precisely
  boundary prediction. Our proposed network was evaluated on the public MICCAI 2020
  Myocardial pathology segmentation dataset which involves patients suffering from
  myocardial infarction. Experiments on the dataset with three modalities demonstrate
  the effectiveness of fusion mode of our model, and attention mechanism can integrate
  various modality information well. We demonstrated that such a deep learning approach
  could better fuse complementary information to improve the segmentation performance
  of cardiac pathology.
tags:
- Medical Image Segmentation
- U-shaped Neural Network
- Cardiac
links:
- name: URL
  url: https://link.springer.com/10.1007/s40747-022-00660-6
---
