# Spatial Filtering & Smoothing

This module covers spatial-domain image filtering techniques using convolution and kernel-based methods. The focus is on smoothing, denoising, sharpening, and basic statistical noise reduction.



## Topics Covered

### 1. Linear Filtering
- Convolution using custom kernels
- Box (mean) filtering
- Gaussian smoothing
- Boundary handling modes (`reflect`, `constant`, `nearest`, etc.)
- Separable Gaussian kernels

### 2. Image Smoothing
- Blur via box kernel
- Blur via Gaussian kernel
- Comparison of smoothing methods

### 3. Unsharp Masking (Sharpening)
- High-frequency emphasis
- Controlled sharpening with scaling factor
- Clipping and stability considerations

### 4. Noise Modeling & Reduction
- Gaussian noise injection
- Statistical averaging to reduce variance
- Demonstration of noise convergence as N increases



## Files

- `linear-smoothing.ipynb`  
  Convolution-based smoothing, Gaussian kernels, separable filters, and unsharp masking.

- `point-averaging.ipynb`  
  Noise modeling and reduction via repeated averaging.

- `images/`  
  Image assets used in the notebooks.



## Key Concepts

- Convolution in the spatial domain
- Kernel normalization
- Gaussian vs box filtering
- Separable convolution efficiency
- Noise variance reduction via averaging
- Sharpening through high-frequency boosting



## Requirements

Install dependencies:

```bash
pip install numpy matplotlib scikit-image scipy jupyter
```



## Running

From this folder:

```bash
jupyter notebook
```

Open either notebook and run all cells sequentially.



## Notes

- Images are typically converted to float format (`0.0–1.0`).
- Convolution boundary behavior affects output results.
- Averaging reduces noise variance proportionally to `1/N`.



This module builds directly into edge detection, frequency-domain filtering, and advanced restoration techniques.
