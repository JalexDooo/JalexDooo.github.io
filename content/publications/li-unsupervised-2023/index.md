---
title: Unsupervised deep consistency learning adaptation network for cardiac cross-modality
  structural segmentation
authors:
- Dapeng Li
- Yanjun Peng
- Jindong Sun
- Yanfei Guo
date: '2023-10-01'
publishDate: '2025-11-12T15:43:53.139527Z'
publication_types:
- article-journal
publication: '*Medical and Biological Engineering and Computing*'
doi: 10.1007/s11517-023-02833-y
abstract: Deep neural networks have recently been succeessful in the ﬁeld of medical
  image segmentation; however, they are typically subject to performance degradation
  problems when well-trained models are tested in another new domain with different
  data distributions. Given that annotated cross-domain images may inaccessible, unsupervised
  domain adaptation methods that transfer learnable information from annotated source
  domains to unannotated target domains with different distributions have attracted
  substantial attention. Many methods leverage image-level or pixel-level translation
  networks to align domaininvariant information and mitigate domain shift issues.
  However, These methods rarely perform well when there is a large domain gap. A new
  unsupervised deep consistency learning adaptation network, which adopts input space
  consistency learning and output space consistency learning to realize unsupervised
  domain adaptation and cardiac structural segmentation, is introduced in this paper
  The framework mainly includes a domain translation path and a cross-modality segmentation
  path. In domain translation path, a symmetric alignment generator network with attention
  to cross-modality features and anatomy is introduced to align bidirectional domain
  features. In the segmentation path, entropy map minimization, output probability
  map minimization and segmentation prediction minimization are leveraged to align
  the output space features. The model conducts supervised learning to extract source
  domain features and conducts unsupervised deep consistency learning to extract target
  domain features. Through experimental testing on two challenging cross-modality
  segmentation tasks, our method has robust performance compared to that of previous
  methods. Furthermore, ablation experiments are conducted to conﬁrm the effectiveness
  of our framework.
tags:
- Medical Image Segmentation
- U-shaped Neural Network
- Cardiac
links:
- name: URL
  url: https://link.springer.com/10.1007/s11517-023-02833-y
---
