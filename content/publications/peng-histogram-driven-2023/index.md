---
title: A histogram-driven generative adversarial network for brain MRI to CT synthesis
authors:
- Yanjun Peng
- Jindong Sun
- Yande Ren
- Dapeng Li
- Yanfei Guo
date: '2023-10-01'
publishDate: '2025-11-12T15:43:53.066159Z'
publication_types:
- article-journal
publication: '*Knowledge-Based Systems*'
doi: 10.1016/j.knosys.2023.110802
abstract: Magnetic Resonance Imaging (MRI) and Computed Tomography (CT) are commonly
  used tools for medical diagnostic assessment. Considering the ionizing radiation
  of CT imaging, estimating CT images from radiation-free MRI would be beneficial
  for medical diagnosis. Although state-of-art generative adversarial networks or
  end-to-end architecture models can generate realistic natural images, it is challenging
  to generate medical CT images with high signal-to-noise ratios and are paired with
  MRI. We propose a histogram-driven generative adversarial network (HisGAN) to address
  this issue, estimate CT images paired with MR, and develop a histogram-based dynamic
  scaling factor to facilitate learning different image styles. By employing an adversarial
  learning strategy to train the end-toend generator, the generator better simulate
  the nonlinear mapping from source to target. For the generator, the proposed method
  applies multiple learnable parameters to adjust the overall weights of the dilated
  convolution layers to ensure sufficient expansive receptive fields for improved
  performance. Additionally, the method utilizes deep residual networks to train randomly
  smoothed generated images and employs adversarial loss to enhance the generation
  of the discriminator, achieving a balance between the generator and the discriminator.
  Our approach can synthesize image details at the pixel level in the target domain
  and has been evaluated using two datasets for MR to CT, T1 to T2, and Flair to T1ce
  modality synthesis tasks. The proposed method outperforms existing generative adversarial
  models applied to medical image synthesis.
tags:
- Medical Image Generation
- GAN
- Brain
featured: True
links:
- name: URL
  url: https://linkinghub.elsevier.com/retrieve/pii/S095070512300552X
---
