# Image I/O Basics

Foundational image processing exercises demonstrating how to load, inspect, convert, and display images using Python, NumPy, Matplotlib, and scikit-image.

This module focuses on understanding image data structures, data types, and grayscale conversion.



## Files

- `io_matplotlib.ipynb`  
  Demonstrates image loading using `matplotlib.image.imread`, metadata inspection, RGB → grayscale conversion, and visualization.

- `io_skimage.ipynb`  
  Demonstrates image loading using `skimage.io.imread`, conversion between floating-point and 8-bit formats, and grayscale handling.



## Concepts Demonstrated

- Reading images into NumPy arrays
- Inspecting image metadata:
  - Data type (`dtype`)
  - Shape
  - Value range
- RGB to grayscale conversion
- Float (`float32`) vs unsigned 8-bit (`uint8`) image representations
- Displaying images with Matplotlib
- Type-safe image conversion using scikit-image utilities



## Dependencies

- Python 3.x
- NumPy
- Matplotlib
- scikit-image
- Jupyter Notebook

Install dependencies:

```bash
pip install numpy matplotlib scikit-image jupyter
```



## Running the Notebooks

From the repository root:

```bash
jupyter notebook
```

Open:

- `io_matplotlib.ipynb`
- `io_skimage.ipynb`

Note: Image paths inside the notebooks may need to be adjusted depending on your local directory structure.



## Learning Goals

This module establishes core understanding of:

- How images are stored as multidimensional arrays
- The importance of numeric precision in image processing
- Safe type conversion practices
- Visualization of image data

These concepts form the foundation for more advanced topics such as filtering, convolution, morphology, and frequency-domain analysis.
