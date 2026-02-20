# Harris Corners and Hough Lines

This module explores classical **feature detection techniques** in computer vision, focusing on:

- Corner detection (Harris)
- Line detection (Hough Transform)

An `images/` folder is included for demonstration examples.


## Contents

### harris-corners.ipynb
Feature Extraction: Corners

Implements and demonstrates:
- corner_harris response map
- corner_peaks for selecting strong keypoints
- corner_subpix for subpixel refinement
- Optional preprocessing with Canny edge detection
- Test image toggle (chess.png) or real-image crop (bikes.jpg)


### hough-lines.ipynb
Feature Extraction: Lines

Implements and demonstrates:
- Standard Hough transform (hough_line)
- Peak detection in accumulator space (hough_line_peaks)
- Probabilistic Hough transform (probabilistic_hough_line)
- Visualization of accumulator space
- Synthetic test pattern option
- Real-image Canny preprocessing


### images/
Example images used in demonstrations:
- bikes.jpg
- chess.png


## Key Concepts Covered

- Harris corner response
- Structure tensor
- Corner strength thresholding
- Subpixel corner refinement
- Canny edge preprocessing
- Hough accumulator space
- Line parameterization (ρ, θ)
- Probabilistic line estimation


## Requirements

pip install numpy matplotlib scikit-image


## Running

jupyter notebook

Run notebooks top-to-bottom.


## Notes

- Harris detection is sensitive to noise and threshold selection.
- Hough results depend heavily on accumulator threshold and line length parameters.
- Toggle the use_test flag in notebooks to switch between synthetic and real images.
