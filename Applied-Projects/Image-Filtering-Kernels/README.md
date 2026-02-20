# Image Filtering: Box vs Disk Kernels

This project explores spatial-domain image smoothing by comparing two convolution kernels:

- **Box (Mean) Kernel**
- **Disk (Radially Weighted) Kernel**

The goal is to analyze how kernel shape and weighting affect blur characteristics and the resulting image differences.



## 📂 Project Structure

```
Image-Filtering-Kernels/
│
├── image_filtering_box_vs_disk.py
├── images/
│   └── cars.jpg
└── README.md
```



## 🧠 Concepts Demonstrated

- Spatial-domain convolution
- Kernel design and normalization
- Uniform averaging vs radially weighted filtering
- Difference image analysis (`I_blur - I`)
- Histogram inspection of filtered results



## 🔬 Implementation Overview

The script:

1. Loads `cars.jpg` as a grayscale image.
2. Converts the image to floating-point format.
3. Defines two kernels:
   - `box_kernel(N)`  
     - NxN uniform averaging kernel.
   - `disk_kernel(N)`  
     - Circular support region.
     - Weights proportional to inverse distance from the center.
     - Properly normalized to preserve brightness.
4. Applies both filters using `scipy.ndimage.convolve`.
5. Displays:
   - Filtered images
   - Histograms
   - Difference images to visualize removed frequency content.



## 🚀 How to Run

From inside the folder:

```bash
python image_filtering_box_vs_disk.py
```

Required dependencies:

```bash
pip install numpy matplotlib scipy scikit-image
```



## 📊 Observations

- The **box kernel** produces stronger uniform blur due to equal weighting across the window.
- The **disk kernel** produces smoother radial blur with less harsh averaging at edges.
- Difference images (`I_blur - I`) help reveal how much high-frequency detail each kernel removes.



## 🎯 Why This Matters

Understanding kernel design is foundational for:

- Image denoising
- Preprocessing for computer vision pipelines
- Edge-preserving filter design
- Frequency-domain interpretation of spatial filters

This project demonstrates practical filter implementation and analysis in a clean, reproducible workflow.
