# Adaptive Median vs Standard Median Filtering (Salt-and-Pepper Noise Removal)

This project compares **standard median filtering** with a simplified **adaptive median filtering approach** for removing salt-and-pepper noise from grayscale images.

The experiment demonstrates how adaptive logic can preserve image detail while eliminating impulse noise.



## 📂 Project Structure

```
Adaptive-Median-Denoising/
│
├── adaptive_median_vs_standard.ipynb
├── images/
│   └── sunsphere.gif
└── README.md
```



## 🧠 Concepts Demonstrated

- Salt-and-pepper noise modeling
- Median filtering
- Adaptive filtering logic
- Morphological footprints (kernel masks)
- Detail preservation vs blur trade-offs



## 🔬 Implementation Overview

The notebook:

1. Loads a grayscale image (`sunsphere.gif`)
2. Converts to `uint8` format for rank filtering
3. Adds 5% salt-and-pepper noise
4. Applies:
   - Standard median filter (small kernel)
   - Standard median filter (larger kernel)
   - Simplified adaptive median filter
5. Compares visual results



## 🧩 Adaptive Median Strategy

The simplified adaptive approach:

1. Computes the standard median-filtered image.
2. Uses a logical mask to selectively replace only extreme noise values.
3. Leaves non-extreme pixels unchanged.

This prevents unnecessary smoothing of clean regions.



## 🚀 How to Run

Open:

```
adaptive_median_vs_standard.ipynb
```

and run all cells.



## 📊 Observations

- The adaptive median filter removes salt-and-pepper noise effectively.
- The small standard median filter also removes noise but slightly smooths details.
- The larger standard median filter eliminates noise more aggressively but introduces noticeable blur.
- Adaptive filtering preserves structure while targeting corrupted pixels.



## 🎯 Why This Matters

Median-based denoising is widely used in:

- Medical imaging
- Remote sensing
- Industrial inspection
- Preprocessing pipelines for computer vision

Understanding the difference between standard and adaptive filtering is critical when balancing noise removal against detail preservation.

This project demonstrates both approaches in a controlled experimental workflow.
