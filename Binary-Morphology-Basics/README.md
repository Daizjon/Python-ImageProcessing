# Binary Morphology Basics

This folder covers **binary morphological image processing**: dilation/erosion, opening/closing, boundaries, thinning/skeletons, area filtering, and convex hull operations.

It also includes a reference PDF with morphology illustrations.



## Contents

### `morphology-binary.ipynb`
**Topic:** Morphology (Binary Methods)

What it demonstrates:
- Load an image and convert to binary using multiple thresholds
- Structuring elements (SE):
  - `disk(N)`
  - `square(N)`
- Binary operations (SciPy):
  - `binary_dilation`
  - `binary_erosion`
  - `binary_opening`
  - `binary_closing`
- Boundary extraction using erosion + set operations
- Skeleton-style representations:
  - `thin`
  - `medial_axis` (and distance transform output)
- Removing small objects:
  - `area_opening`
- Convex hull:
  - `convex_hull_image`
  - `convex_hull_object`

Key concepts:
- How the **structuring element** shape/size controls morphological behavior
- Connectivity differences (4-connectivity vs 8-connectivity effects)
- Skeletonization vs medial axis (and when each is useful)
- Convex hull for binary objects and masks



### `morphology-illustrations.pdf`
A visual reference packet containing morphology diagrams and step-by-step illustrations.

**Attribution:** Illustrations derived from R. Gonzalez & R. Woods, *Digital Image Processing* (Prentice Hall, 2008).



## Data / Images

This folder includes image assets such as:
- `blobs.png` (used for thresholding and morphology demos)

Depending on repo layout, notebook image paths may reference:
- `../../images/...`

Make sure the `images` path matches where you run the notebook from.



## How to Run

1. Create/activate an environment
2. Install dependencies:
   - `numpy`
   - `matplotlib`
   - `scikit-image`
   - `scipy`

3. Launch:
   - `jupyter notebook` or `jupyter lab`
4. Open `morphology-binary.ipynb` and run top-to-bottom.


## Notes / Tips

- If the thresholded result looks “broken,” tweak the threshold.
- Try different structuring elements:
  - larger `disk()` for stronger smoothing of shapes
  - `square()` to emphasize axis-aligned expansion/contraction
- For skeleton/medial axis, results depend heavily on noise and small spurs—area opening can help first.
