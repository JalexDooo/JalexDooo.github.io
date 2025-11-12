---
title: 'DMCA-GAN: dual multilevel constrained attention GAN for MRI-based hippocampus
  segmentation'
authors:
- Xue Chen
- Yanjun Peng
- Dapeng Li
- Jindong Sun
date: '2023-12-01'
publishDate: '2025-11-12T15:43:53.107031Z'
publication_types:
- article-journal
publication: '*Journal of Digital Imaging*'
doi: 10.1007/s10278-023-00854-5
abstract: Precise segmentation of the hippocampus is essential for various human brain
  activity and neurological disorder studies. To overcome the small size of the hippocampus
  and the low contrast of MR images, a dual multilevel constrained attention GAN for
  MRI-based hippocampus segmentation is proposed in this paper, which is used to provide
  a relatively effective balance between suppressing noise interference and enhancing
  feature learning. First, we design the dual-GAN backbone to effectively compensate
  for the spatial information damage caused by multiple pooling operations in the
  feature generation stage. Specifically, dual-GAN performs joint adversarial learning
  on the multiscale feature maps at the end of the generator, which yields an average
  Dice coefficient (DSC) gain of 5.95% over the baseline. Next, to suppress MRI high-frequency
  noise interference, a multilayer information constraint unit is introduced before
  feature decoding, which improves the sensitivity of the decoder to forecast features
  by 5.39% and effectively alleviates the network overfitting problem. Then, to refine
  the boundary segmentation effects, we construct a multiscale feature attention restraint
  mechanism, which forces the network to concentrate more on effective multiscale
  details, thus improving the robustness. Furthermore, the dual discriminators D1
  and D2 also effectively prevent the negative migration phenomenon. The proposed
  DMCA-GAN obtained a DSC of 90.53% on the Medical Segmentation Decathlon (MSD) dataset
  with tenfold cross-validation, which is superior to the backbone by 3.78%.
tags:
- /unread
- /未读
links:
- name: URL
  url: https://link.springer.com/10.1007/s10278-023-00854-5
---
