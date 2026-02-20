# Spectral Restoration and Deconvolution

This module explores image restoration using frequency-domain deconvolution techniques, with emphasis on the Wiener filter.

It demonstrates how blurred and noisy images can be partially recovered when the degradation model is known.



## Problem Model

We assume the degradation model:

g = h * f + n

Where:

- f → original image  
- h → blur kernel (point spread function)  
- n → additive white noise  
- g → observed degraded image  

The goal is to estimate f from g.



## Parametric Wiener Filter

The Wiener filter estimates the original image in Fourier space by minimizing mean squared error.

General frequency-domain formulation:

F̂(u,v) = [ H*(u,v) / ( |H(u,v)|² + γ · R(u,v) ) ] · G(u,v)

Where:

- H → Fourier transform of blur kernel  
- G → Fourier transform of degraded image  
- γ → regularization parameter  
- R → noise/signal spectral model  

Three restoration strategies are demonstrated:

1. Constant approximation (PSNR-based scalar)
2. Known signal-to-noise ratio
3. Estimated power spectral ratio Sff / Snn



## What This Module Demonstrates

### Gaussian Blur Simulation

- Constructing a 2D Gaussian blur kernel
- Convolving the image with blur
- Adding controlled white Gaussian noise

### Wiener Deconvolution

- Restoration with no noise
- Restoration with additive white noise
- Restoration using:
  - Constant PSNR approximation
  - Known variance ratio
  - Full spectral power ratio

### Regularization

The filter can penalize high-frequency amplification using:

- Laplacian-based spectral weighting
- Power spectral density estimation

This prevents instability when |H(u,v)| is small.



## Concepts Reinforced

- Convolution theorem
- Frequency-domain inversion
- Ill-posed inverse problems
- Regularization in Fourier space
- Noise amplification during deconvolution
- Importance of spectral estimation



## Images Used

Located in the images/ folder:

- parrot.png

Used for:
- Blur simulation
- Noise injection
- Visual restoration comparison



## Requirements

pip install numpy matplotlib scipy scikit-image



## Learning Outcomes

After completing this module, you should understand:

- Why naive inverse filtering fails
- How Wiener filtering stabilizes inversion
- How noise power affects restoration
- The role of regularization in frequency space
- How to simulate controlled image degradation



## Position in Course Progression

This module builds directly on:

- Fourier Analysis
- Spectral Filtering
- Frequency-Domain Image Processing

It represents the culmination of frequency-domain methods applied to real-world image degradation problems.

