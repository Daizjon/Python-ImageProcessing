# Morphology: Shape Filtering

This project applies **binary morphological operations** to filter and restructure shapes in two test images:

- `morpho1.gif` — remove small artifacts while preserving larger circular objects  
- `morpho2.gif` — cluster many small objects into fewer, larger 4-connected groups  

Foreground is treated as **black (0)** and background as **white (1)** after boolean conversion.



## Project Structure

```
Applied-Projects/
└── Morphology-Shape-Filtering/
    ├── morphology_shape_filtering.ipynb
    └── images/
        ├── morpho1.gif
        └── morpho2.gif
```



## Morpho1 — Selective Shape Cleanup

### Objective
- Preserve larger circular objects
- Remove small lines and small circular noise
- Display:
  - Before image
  - After image
  - Difference image (removed structures highlighted)

### Approach
- Convert grayscale image to boolean
- Apply morphological **closing** using a disk structuring element
- Use XOR difference and inversion to visualize removed components



## Morpho2 — Object Clustering (4-Connected)

### Objective
- Merge many small objects into fewer large clusters
- Ensure clusters are **4-connected** (touch via sides, not diagonals)
- Display:
  - Before image
  - After image
  - Overlay of result on input image

### Approach
- Convert to boolean mask
- Apply dilation / closing operations to merge nearby components
- Optionally apply cleanup operations
- Overlay result for visualization



## Dependencies

Install required packages:

```bash
pip install numpy matplotlib scikit-image scipy
```



## How To Run

1. Launch Jupyter:

```bash
jupyter notebook
```

2. Open:

```
morphology_shape_filtering.ipynb
```

3. Run all cells.

Images are loaded from:

```
images/morpho1.gif
images/morpho2.gif
```



## Implementation Notes

- Morphological operations use `skimage.morphology` and `scipy.ndimage`.
- Boolean conversion ensures morphology operates on binary masks.
- Structuring elements such as `disk()` are used to control scale of filtering.
- Difference visualization highlights removed objects clearly.



## Outcome

- Morpho1: small noise removed while larger circular objects remain intact.
- Morpho2: small disconnected objects grouped into larger 4-connected clusters.
