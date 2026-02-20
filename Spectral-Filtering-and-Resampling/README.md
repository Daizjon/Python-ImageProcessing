# Spectral Filtering and Resampling

This module explores frequency-domain filtering and image resampling using Butterworth filters and FFT-based processing.

It extends Fourier theory into practical spectral manipulation of signals and images.



## Contents

### 1D Spectral Filtering

Implements Butterworth filters for 1D signals:

- Low-pass filter
- High-pass filter
- Band-pass filter
- Band-stop filter

Concepts demonstrated:

- Frequency separation of signals
- Noise suppression
- Filter order and roll-off control
- Convolution kernels derived from spectral filters

Key ideas:
- Butterworth filters provide maximally flat passbands
- Higher order → sharper roll-off
- Filtering in frequency domain equals convolution in spatial domain



### 2D Spectral Filtering (Images)

Extends Butterworth filtering to 2D images using radial distance in frequency space.

Demonstrates:

- Image low-pass filtering (blurring)
- High-pass filtering (edge emphasis)
- Band-pass and band-stop filtering
- Frequency-domain noise removal
- Targeted removal of sinusoidal interference

Includes visualizations of:
- Magnitude spectra
- Log-scaled FFT representations
- Spatial vs frequency domain comparisons



### Spectral Image Resampling

Implements image resizing using Fourier-domain techniques.

Covers:

- Downsampling with anti-aliasing
- Upsampling via FFT zero-padding
- Amplitude scaling compensation
- Arbitrary scaling using upsample → filter → downsample pipeline
- Interpolation using frequency-domain principles

Demonstrates:

- Why anti-aliasing is required before decimation
- How zero-padding increases spatial resolution
- Relationship between spectral bandwidth and spatial smoothness



## Learning Objectives

After completing this module, you should understand:

- How Butterworth filters behave in frequency space
- How filter order affects response sharpness
- How 2D radial filters are constructed
- How to suppress structured noise in images
- Why zero-padding increases spatial resolution
- How aliasing occurs and how to prevent it
- Practical FFT-based image resizing



## Requirements

pip install numpy matplotlib scipy scikit-image



## Images Used

Located in the images/ folder:

- zebras.jpg
- cars.jpg

These are used for:
- Spectral filtering demonstrations
- Noise experiments
- Resampling examples



## Notes

This module builds directly on:

- Fourier Analysis and Frequency Domain Processing
- Spatial Filtering

It bridges theory and advanced frequency-domain image manipulation.

