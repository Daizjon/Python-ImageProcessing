# Grayscale Morphology and Reconstruction

This module explores advanced **morphological image processing** techniques, focusing on:

- Grayscale dilation and erosion
- Opening and closing (max–min filtering)
- Top-hat transformation (shading correction)
- Morphological gradients
- Morphological reconstruction
- Hole filling and border clearing


## Contents

### morphology-grayscale.ipynb
Morphology: Grayscale Methods

Demonstrates:

- Otsu thresholding
- Grayscale dilation (max filtering)
- Grayscale erosion (min filtering)
- Opening and closing operations
- Top-hat transformation for illumination correction
- Binary and grayscale textural segmentation
- Morphological gradients (edge extraction via dilation–erosion difference)

Key Concepts:

- Structuring elements (`disk`, `square`)
- Effect of structuring element size
- Difference between binary and grayscale morphology
- Using morphology for segmentation refinement


### morphology-reconstruction.ipynb
Morphology via Reconstruction

Demonstrates:

- Reconstruction-based hole filling
- Reconstruction-based border clearing
- Marker and mask concepts
- Iterative geodesic dilation
- Shape-preserving morphological processing

Key Concepts:

- Reconstruction vs. standard dilation
- Preserving connected components
- Removing border-touching objects
- Filling internal cavities without overgrowing shapes


## Images / Assets

The notebooks reference image files such as:

- rice_grains.png
- blob_mixture.gif
- text.gif
- blobs.png

Ensure your relative paths match your repository structure (many cells reference `../../images/...`).


## Requirements

Install dependencies:

pip install numpy matplotlib scikit-image scipy


## How to Run

jupyter notebook

Open each notebook and run cells sequentially.


## Notes

- Structuring element size strongly affects results.
- Large disks are useful for background correction (top-hat).
- Reconstruction is more shape-aware than naive dilation.
- Thresholding before morphology often improves segmentation.
