# Histogram Equalization (Grayscale Image Processing)

This mini-project demonstrates **histogram equalization** for contrast enhancement on a grayscale image.

The script loads an image, performs histogram equalization, and displays:

- Original image
- Original intensity histogram
- Equalized image
- Equalized intensity histogram

This illustrates how redistributing pixel intensities improves global contrast.



## 📂 Project Structure

```
Histogram-Equalization/
│
├── histogram_equalization.py
├── images/
│   └── cheetah.png
└── README.md
```



## 🧠 Concepts Demonstrated

- Grayscale image processing
- Histogram computation
- Cumulative distribution function (CDF)
- Contrast enhancement
- Visualization of intensity distributions



## ⚙️ Implementation Details

The script:

1. Loads a grayscale image using `skimage.io`
2. Converts it to floating-point format
3. Applies histogram equalization using:
   - `skimage.exposure.equalize_hist()`
4. Displays before/after images and histograms in a 2×2 grid



## 🚀 How to Run

From inside the project folder:

```bash
python3 histogram_equalization.py
```

Make sure you have the required packages installed:

```bash
pip install numpy matplotlib scikit-image
```



## 📊 What to Look For

After running the script, you should observe:

- A wider intensity spread in the equalized histogram
- Improved visual contrast in the processed image
- Redistribution of pixel intensities toward a more uniform distribution



## 🎯 Why This Matters

Histogram equalization is a foundational image enhancement technique used in:

- Medical imaging
- Remote sensing
- Low-light image correction
- Preprocessing for computer vision pipelines

This project demonstrates both the theory and practical application of intensity redistribution in digital images.
