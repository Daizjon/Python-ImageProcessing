# Point Operations & Histogram Methods

This module demonstrates foundational **image enhancement techniques** using point-wise intensity transformations and histogram-based processing.

The notebooks explore how pixel intensity values can be manipulated to improve contrast, enhance visibility, perform masking, and detect motion.



## Topics Covered

### 1. Point Operations
Operations applied independently to each pixel:

- Thresholding
- Contrast & brightness adjustment
- Contrast stretching
- Gamma correction
- Log and inverse-log correction
- Sigmoid correction
- Logical masking
- Alpha blending (image compositing)
- Motion detection via subtraction



### 2. Histogram-Based Methods

Techniques that operate on the intensity distribution:

- Histogram visualization
- Histogram equalization
- CLAHE (Contrast Limited Adaptive Histogram Equalization)
- Histogram matching



## Files

- `point_operations.ipynb`  
  Practical implementations of intensity transforms, masking, blending, and motion detection.

- `point_functions.ipynb`  
  Mathematical visualization of gamma, log, and sigmoid transformation curves.

- `histogram_methods.ipynb`  
  Histogram equalization, adaptive histogram equalization, and histogram matching using `scikit-image`.

- `images/`  
  Local images used for demonstration (kept as-is).



## Requirements

Install required libraries:

```bash
pip install numpy matplotlib scikit-image jupyter
```



## Running the Notebooks

From this folder:

```bash
jupyter notebook
```

Open any notebook and execute the cells sequentially.



## Key Concepts

- Pixel intensity scaling (float vs uint8 ranges)
- Distribution reshaping via histogram equalization
- Local contrast enhancement (CLAHE)
- Intensity transfer between images (histogram matching)
- Mathematical form of common intensity transformations
- Basic compositing and change detection techniques



## Notes

- Some notebooks reference images using relative paths (e.g., `../../images/...`).
  Adjust paths if you reorganize the repository structure.
- Float images typically use the range `[0.0, 1.0]`.
- uint8 images use `[0, 255]`.



This module forms the foundation for later topics such as filtering, convolution, morphology, and segmentation.
