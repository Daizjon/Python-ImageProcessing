# Image Derivatives & Edge Detection

This module explores spatial-domain derivative filters used for gradient estimation, edge detection, and sharpening.

It covers both first-order and second-order derivative operators, as well as their use in enhancement and feature extraction.



## Topics Covered

### 1. First-Order Derivatives (Gradients)

- Sobel operator
- Prewitt operator
- Complex derivative kernels
- Gradient magnitude
- Gradient direction (angle)

Demonstrates how real and imaginary components of a complex kernel encode horizontal and vertical derivatives simultaneously.



### 2. Second-Order Derivatives

- Laplacian operator
- Laplacian-based sharpening
- Mexican Hat (Laplacian of Gaussian approximation)

Explores edge enhancement using second derivatives and smoothing-derivative combinations.



### 3. Emboss Filtering

- Directional derivative-based shading effect
- Perceived depth via asymmetric kernels



### 4. Sharpening Techniques

- Unsharp masking using Laplacian
- High-frequency emphasis
- Gaussian pre-smoothing before derivative filtering



## Files

- `linear-derivatives.ipynb`  
  Implementation of Sobel, Prewitt, Laplacian, Mexican Hat kernels, gradient magnitude/angle computation, embossing, and derivative-based sharpening.

- `images/`  
  Image assets used in demonstrations.



## Key Concepts

- Convolution with derivative kernels
- Gradient estimation
- Magnitude vs direction interpretation
- Second-order edge detection
- Relationship between smoothing and differentiation
- Laplacian-based sharpening



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

Open the notebook and run cells sequentially.



## Notes

- Images are converted to float format (`0.0–1.0`) before processing.
- Boundary handling (`reflect`, `nearest`, etc.) affects derivative output.
- Gradient angle is returned in radians (`-π to π`).
- Laplacian and Mexican Hat filters may produce negative values before rescaling.



This module builds directly into segmentation, feature detection, and frequency-domain filtering.
