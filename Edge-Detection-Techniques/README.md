# Edge Detection Techniques (Canny • Sobel • Marr–Hildreth)

This module explores classical and advanced **edge detection algorithms** in the spatial domain.

It includes both:
- From-scratch implementations (with Cython acceleration)
- Library-based comparisons using `scikit-image`



## What’s Inside

### `canny-details.ipynb`
Full Canny edge detector implemented step-by-step:
- Gaussian smoothing
- Sobel gradient computation (complex-valued kernel)
- Gradient magnitude + angle calculation
- Angle quantization
- Non-maximum suppression (edge thinning)
- Hysteresis thresholding (edge tracing)

Includes custom Cython implementations for:
- Angle quantization
- Non-max suppression
- Recursive edge tracing



### `edge-detection.ipynb`
Library-based edge detection comparisons:
- Sobel operator
- Built-in `skimage.feature.canny`
- Histogram analysis of gradient magnitudes
- Threshold tuning comparisons



### `marr-hildreth.ipynb`
Implements Marr–Hildreth edge detection:
- Gaussian smoothing
- Laplacian filtering
- Zero-crossing detection
- Cython implementation of zero-cross logic

Also referred to as:
**Laplacian of Gaussian (LoG) edge detection**



### `images/`
Example images used in demonstrations (blobs, bikes, etc.)



## Key Concepts Covered

- Gradient-based edge detection
- Sobel operators (complex kernels)
- Gradient magnitude and direction
- Non-maximum suppression
- Double thresholding + hysteresis
- Laplacian filtering
- Zero-crossings
- Gaussian smoothing before differentiation
- Tradeoffs between noise suppression and localization



## Requirements

```bash
pip install numpy matplotlib scikit-image scipy jupyter cython
```



## Running

From this folder:

```bash
jupyter notebook
```

Run notebooks top-to-bottom.



## Notes

- Canny implementation is partially accelerated using Cython.
- Angle quantization reduces gradient directions to four principal orientations.
- Hysteresis thresholding ensures edge continuity.
- Marr–Hildreth detects edges via zero-crossings of the Laplacian.
- Threshold and sigma parameters significantly affect output quality.
