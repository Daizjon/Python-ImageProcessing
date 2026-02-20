# Nonlinear Rank Filters

This module explores **nonlinear spatial filtering techniques**, with emphasis on rank-based filters and robust noise reduction methods.

Unlike linear convolution filters, nonlinear filters operate on ordered neighborhood values and are especially effective for removing impulse (salt-and-pepper) noise.



## Topics Covered

### 1. Noise Modeling
- Salt-and-pepper noise generation
- Gaussian noise (in previous modules)
- Image type conversion (uint8 vs float)



### 2. Rank-Based Filters

Neighborhood statistics computed from sorted values:

- Mean filter
- Alpha-trimmed mean filter
- Median filter
- Min / Max filters
- Local gradient (max - min)



### 3. Alpha-Trimmed Mean Filtering

Removes extreme values in a neighborhood before averaging.

Useful when:
- Noise contains outliers
- You want a compromise between mean and median filtering

Includes:
- Pure Python implementation
- Optimized Cython implementation (for performance comparison)



### 4. Structuring Footprints

Custom kernel masks:
- Box kernel
- Disk kernel

Used to define the neighborhood region for rank operations.



### 5. scikit-image Rank Filters

Demonstrates built-in nonlinear filters from:

`skimage.filters.rank`

Examples include:
- Geometric mean
- Local entropy
- Majority filter
- Contrast enhancement



## Files

- `nonlinear-rank.ipynb`  
  Pure Python implementations of rank filters and comparisons.

- `nonlinear-cython.ipynb`  
  Alpha-trimmed mean filter implemented using Cython for speed.

- `images/`  
  Example images used for demonstration.



## Key Concepts

- Nonlinear filtering vs linear convolution
- Order statistics
- Neighborhood masking (footprints)
- Robust noise suppression
- Performance optimization with Cython
- Rank-based contrast enhancement



## Requirements

Install dependencies:

```bash
pip install numpy matplotlib scikit-image scipy jupyter cython
```



## Running

From this folder:

```bash
jupyter notebook
```

Open either notebook and run cells sequentially.



## Notes

- `skimage.filters.rank` functions require **uint8 images**, which is why `img_as_ubyte()` is used.
- Alpha-trimmed mean filtering balances between mean filtering (smooth but noise-sensitive) and median filtering (robust but may remove detail).
- Cython cells must be executed in a proper Jupyter environment with Cython installed.
- Boundary handling uses `mode='reflect'` during padding.



This module builds toward morphological operations and segmentation techniques.
