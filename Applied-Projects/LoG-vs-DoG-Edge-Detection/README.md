# LoG vs DoG Edge Detection (Scale-Space Filtering)

This project compares **Laplacian of Gaussian (LoG)** filtering with its efficient approximation, **Difference of Gaussians (DoG)**.

The goal is to demonstrate how DoG can approximate LoG by selecting appropriate Gaussian scale parameters.



## 📂 Project Structure

```
LoG-vs-DoG-Edge-Detection/
│
├── log_vs_dog_comparison.ipynb
├── images/
│   └── F35.gif
└── README.md
```



## 🧠 Concepts Demonstrated

- Gaussian smoothing
- Laplacian filtering
- Difference of Gaussians (DoG)
- Scale-space representation
- Edge and feature enhancement
- Kernel approximation techniques



## 🔬 Implementation Overview

The notebook:

1. Loads a grayscale image (`F35.gif`)
2. Computes **LoG** by:
   - Applying Gaussian smoothing
   - Applying the Laplacian operator
3. Computes **DoG** using:
   - `skimage.filters.difference_of_gaussians()`
4. Compares outputs visually using consistent display ranges
5. Explores parameter relationships between:
   - Base sigma (σ)
   - Scale factor (k)



## 📐 Mathematical Insight

The Laplacian of Gaussian can be approximated (up to scale) by:

```
DoG ≈ LoG
```

Where:

- LoG:  ∇² ( Gσ * I )
- DoG:  (Gσ * I) − (Gkσ * I)

For appropriate values of k > 1.



## 🚀 How to Run

### Option 1 — Jupyter Notebook

Open:

```
log_vs_dog_comparison.ipynb
```

and run all cells.



## 📊 Observations

- DoG produces visually similar edge responses to LoG.
- Proper selection of σ and k controls edge thickness and sensitivity.
- DoG is computationally simpler and widely used in practice (e.g., SIFT feature detection).



## 🎯 Why This Matters

LoG and DoG filtering are foundational in:

- Edge detection
- Blob detection
- Scale-space theory
- Feature extraction
- Computer vision pipelines

This project demonstrates practical filter comparison and parameter tuning in a clean experimental workflow.
