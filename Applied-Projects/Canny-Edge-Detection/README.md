# Canny Edge Detection (Applied Project)

This project implements and tunes a **Canny-style edge detection pipeline** on an example building image (`umbc.png`), combining:
- **Gaussian smoothing + Sobel gradients** (via `skimage.filters`)
- **Gradient angle quantization**
- **Non-maximum suppression (edge thinning)**
- **Double-threshold hysteresis (edge tracking)**

It also demonstrates how output changes when **low/high hysteresis thresholds are doubled** while keeping smoothing and contrast scaling fixed.



## What’s Inside

- `canny_edge_detection.ipynb`   
  Notebook implementation (includes a `%%cython` cell for faster edge thinning/hysteresis helpers).

  > If wanting on a `.py` file: remove notebook magics (`%matplotlib inline`, `%%cython`, etc.) and convert the Cython helpers into pure Python or a separate compiled module.

- `images/umbc.png`  
  Test image used for edge detection.



## Approach

### 1) Preprocessing + Gradients (scikit-image)
- Apply Gaussian smoothing with a chosen `sigma`
- Compute **horizontal** and **vertical** Sobel gradients (`sobel_h`, `sobel_v`)
- Combine into a complex-valued gradient field and compute magnitude
- Rescale gradient magnitudes using a **fraction of the max magnitude** (contrast normalization)

### 2) Canny Support Steps (custom)
- **Angle quantization** into 4 directions (0°, 45°, 90°, 135°)
- **Edge thinning** (non-max suppression) based on quantized direction
- **Edge hysteresis** using low/high thresholds with recursive edge tracing

### 3) Parameter Comparison
- **C1:** tuned thresholds that produce a visually satisfying result  
- **C2:** same `sigma` and rescaling, but **thresholds doubled**



## How to Run

### Jupyter Notebook
1. Open `canny_edge_detection.ipynb` in Jupyter / VS Code
2. Run all cells top-to-bottom
3. The notebook outputs side-by-side edge maps:
   - `C1` (baseline thresholds)
   - `C2` (doubled thresholds)

### Dependencies
- `numpy`
- `matplotlib`
- `scikit-image`
- `cython` *(only needed because the notebook uses `%%cython`)*


## Notes / Observations
With `sigma` and contrast rescaling held constant, **doubling both thresholds** generally produces **fewer detected edges** and can miss weaker structure, resulting in a less complete edge map compared to the tuned baseline.
