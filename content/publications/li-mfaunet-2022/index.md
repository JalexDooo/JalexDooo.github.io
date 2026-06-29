---
title: 'MFAUNet: multiscale feature attentive U‐net for cardiac MRI structural segmentation'
authors:
- Dapeng Li
- Yanjun Peng
- Yanfei Guo
- Jindong Sun
date: '2022-03-01'
publishDate: '2025-11-12T15:43:53.155716Z'
publication_types:
- article-journal
publication: '*IET Image Processing*'
doi: 10.1049/ipr2.12406
abstract: The accurate and robust automatic segmentation of cardiac structures in
  magnetic resonance imaging (MRI) is signiﬁcant in calculating cardiac clinical functional
  indices, and diagnosing heart diseases. Most U-Net based methods use pooling, transposed
  convolution, and skip connection operations to integrate the multiscale features
  for improved segmentation in cardiac MRI. However, this architecture lacks adequate
  semantic connection between the channel and spatial information, and robustness
  in segmenting objects with signiﬁcant shape variations. In this paper, a new multiscale
  feature attentive U-Net for cardiac MRI structural segmentation method is proposed.
  An attention mechanism is adopted after concatenating the multi-level features to
  aggregate different scale features and determine on which features to focus. Cascade
  and parallel dilated convolution is also employed in the decoder blocks and skip
  connection is employed to enhance the ability of sensing receptive ﬁelds for multiscale
  context information. Furthermore, deep supervision approach with a loss function
  that combines the dice and cross-entropy losses to reduce overﬁtting and ensure
  better prediction is introduced. The proposed method was evaluated on three public
  cardiac datasets. The experimental results indicate that the method achieved competitive
  segmentation performance with the three datasets, which veriﬁes the robustness and
  generalisability of the proposed network. In comparison with conventional U-Net
  methods, the model leverages attention mechanism and dilated convolution block,
  which increases the semantic connection between the channel and the spatial information,
  and improves the robustness of the right ventricle segmentation performance. From
  the view of the Dice scores and segmentation results, the multiscale feature attentive
  U-Net method is one of effective methods in segmenting cardiac MRI structures.
tags:
- Medical Image Segmentation
- U-shaped Neural Network
- Cardiac
links:
- name: URL
  url: https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/ipr2.12406
---
