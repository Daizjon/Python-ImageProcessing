# Circle Detection with Hough Transform

This project detects circular objects (coins) in an image using:

- Canny edge detection
- Hough Circle Transform
- Peak extraction from the accumulator space
- Red circle overlays for visualization

Implemented in a Jupyter Notebook.



## Files

- hough_circle_detection.ipynb — Main notebook
- images/coins.png — Input image used for detection



## Overview

### Step 1 — Edge Detection (Canny)

The notebook:
- Converts the image to grayscale
- Applies `skimage.feature.canny()` to generate an edge map
- Tunes:
  - `sigma`
  - `low_threshold`
  - `high_threshold`

These parameters determine edge sensitivity and directly affect circle detection performance.



### Step 2 — Hough Circle Transform

- Defines a radius search range (example: `range(60, 90)`)
- Applies `skimage.transform.hough_circle()`
- Extracts circle candidates using:
  - `hough_circle_peaks()`
  - `total_num_peaks`
  - `min_xdistance`
  - `min_ydistance`

The notebook prints detected circles in the format:

    Coin center: (x, y), radius: r



### Step 3 — Visualization

- Displays the original image
- Overlays detected circles in red
- Uses Matplotlib patches for clean visualization



## How to Run

1. Open Jupyter:

   jupyter notebook

2. Open:

   hough_circle_detection.ipynb

3. Run all cells.

Make sure the image path is correct:

```python
io.imread("images/coins.png", as_gray=True)
```



## Parameters Used (Example)

Canny:
- sigma = 0.7
- low_threshold = 1
- high_threshold = 1

Hough:
- radii range = 60 to 90
- total_num_peaks = 4
- min_xdistance = 40
- min_ydistance = 40



## Notes

- Radius range must match object scale in the image.
- Poor edge maps lead to poor Hough results.
- Minimum distance constraints prevent duplicate detections.
- Results may vary slightly depending on parameter tuning.



## Outcome

Successfully detects all four coins in the image and overlays accurate circle boundaries on the original grayscale input.
