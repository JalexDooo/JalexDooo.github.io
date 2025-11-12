---
title: 'DSLN: dual-tutor student learning network for multiracial glaucoma detection'
authors:
- Yanfei Guo
- Yanjun Peng
- Jindong Sun
- Dapeng Li
- Bin Zhang
date: '2022-07-01'
publishDate: '2025-11-12T15:43:53.115027Z'
publication_types:
- article-journal
publication: '*Neural Computing and Applications*'
doi: 10.1007/s00521-022-07078-8
abstract: 'Accurate early glaucoma detection is crucial to prevent further vision
  loss. However, using the off-the-shelf models against fundus image datasets of different
  races may lead to degraded performance due to domain shift. To address the issue,
  this paper proposes a dual-tutor student learning network (DSLN) for multiracial
  glaucoma detection. The proposed DSLN consists of an inter-image tutor, an intra-image
  tutor, student model and backbone network, which combines the advantages of domain
  adaptation and semi-supervised learning. The inter-image tutor uses CycleGAN for
  style transfer to reduce the appearance differences between labeled source domain
  and labeled target domain images, and transfers the learned knowledge to the student
  model by minimizing knowledge distillation loss. The intra-image tutor adopts the
  exponential moving average to leverage the unlabeled target domain and transfers
  the knowledge to the student model by minimizing prediction consistency loss. Moreover,
  the student model not only directly learns knowledge from the labeled target domain
  images, but also learns the intra-image knowledge and inter-image knowledge transfer
  by two tutors. Furthermore, the backbone integrates the context features of the
  local optic disc region and global fundus image via modiﬁed ResNet50. We conduct
  extensive experiments on three scenarios constructed from nine public fundus image
  datasets of three races. Comprehensive experimental results show that the proposed
  DSLN framework outperforms the state-of-the-art models and has good robustness and
  generalization: it can effectively overcome domain shift and accurately detect glaucoma
  from multi-ethnic fundus images.'
tags:
- /unread
- /未读
links:
- name: URL
  url: https://link.springer.com/10.1007/s00521-022-07078-8
---
