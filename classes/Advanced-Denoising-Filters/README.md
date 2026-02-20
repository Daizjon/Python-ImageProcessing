# Advanced Denoising Filters (Bilateral • Diffusion • Non-Local Means)

This folder contains Jupyter notebooks exploring **advanced spatial-domain denoising** techniques for grayscale images.  
Focus: reducing noise while preserving edges and important structure.

## What’s Inside

### `nonlinear-bilateral.ipynb`
Edge-preserving smoothing using **bilateral filtering**, including:
- Mean bilateral filter (`skimage.filters.rank.mean_bilateral`) on `uint8` images
- Gaussian bilateral filter (`skimage.restoration.denoise_bilateral`) on float images
- Line profile + histogram comparisons (original vs noisy vs filtered)

### `nonlinear-diffusion.ipynb`
Iterative denoising using **anisotropic diffusion** (Cython-accelerated), including:
- Two conduction functions (exponential + inverse-quadratic style)
- Neighbor-based updates (4-connected neighborhood)
- Multiple iterations to show progressive smoothing while limiting edge blur

### `nonlinear-nlmeans.ipynb`
Patch-based denoising using **Non-Local Means**, including:
- `skimage.restoration.denoise_nl_means`
- Controls for patch size, search distance, and smoothing strength
- Histogram + difference visualization (denoised vs original)

## Requirements

- Python 3.x
- Jupyter Notebook / JupyterLab
- numpy
- matplotlib
- scikit-image
- scipy
- cython (only needed for the diffusion notebook)

## Running

From this folder:

1. Start Jupyter:
   - `jupyter lab` or `jupyter notebook`

2. Open any notebook and run all cells.

> Note: Some notebooks load shared images via relative paths like `../../images/...`.
> Keep the repository’s shared `images/` folder in place so the examples run without edits.

## Notes

- The bilateral notebook uses both `uint8` and float workflows depending on the function.
- The diffusion notebook uses a Cython cell for speed.
- NL-means parameters can be tuned heavily depending on noise level and texture.
