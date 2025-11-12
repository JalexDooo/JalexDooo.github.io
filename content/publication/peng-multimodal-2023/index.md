---
title: The multimodal MRI brain tumor segmentation based on AD-net
authors:
- Yanjun Peng
- Jindong Sun
date: '2023-02-01'
publishDate: '2025-11-12T15:43:53.082435Z'
publication_types:
- article-journal
publication: '*Biomedical Signal Processing and Control*'
doi: 10.1016/j.bspc.2022.104336
abstract: Multimodal glioma images provide different features of tumor boundaries
  based on magnetic resonance imaging (MRI), where multimodal features are often challenging
  to extract for deep learning segmentation methods. Disturbance between features
  of different modes is an important factor restricting multimodal learning. To efficiently
  extract multimodal features, we propose an automatic weighted dilated convolutional
  network (AD-Net) to learn multimodal brain tumor features through channel feature
  separation learning. Specifically, the auto-weight dilated convolutional unit (AD
  unit) utilizes dual-scale convolutional feature maps to acquire channel separation
  features. We employ two learnable parameters to fuse dual-scale convolutional feature
  maps in encoding layers, and the two learnable parameters are automatically adjusted
  with the back propagation of the gradient. We adopt the Jensen–Shannon divergence
  to constrain the distribution of its feature map, which in turn regularizes the
  weights of the entire down-sampling. In addition, we use the training technique
  of deep supervision to achieve fast fitting. Our proposed method got dice scores
  of 0.90, 0.80, and 0.76 for the whole tumor (WT), the tumor core (TC), and the enhancing
  tumor (ET) on the BraTS20 dataset. The experimental results showed good performance
  with the AD-Net network.
tags:
- /unread
- /未读
links:
- name: URL
  url: https://linkinghub.elsevier.com/retrieve/pii/S174680942200790X
---
