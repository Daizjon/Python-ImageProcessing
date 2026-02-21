# Spectral Filtering: Butterworth Notch Filter

This project implements a **2D Butterworth notch filter** in the frequency domain to remove structured periodic noise from an image.

A zebra image is intentionally corrupted with a 2D sine wave. The notch filter is then applied in the Fourier domain to suppress the injected frequency components and restore the image.



## Project Structure

```
Applied-Projects/
└── Butterworth-Notch-Filtering/
    ├── butterworth_notch_filter.ipynb
    └── images/
        └── zebras.jpg
```



## What This Project Demonstrates

- 2D FFT and inverse FFT (`fft2`, `ifft2`)
- Frequency shifting
- Synthetic periodic noise generation (2D sinewave)
- Butterworth notch filter construction
- Frequency-domain filtering
- Log-spectrum visualization



## Workflow

### 1. Load Image
- Read `zebras.jpg`
- Convert to float

### 2. Add Periodic Noise
- Generate 2D sinewave pattern
- Add to original image
- Produce corrupted image

### 3. Fourier Transform
- Apply `fft2`
- Use power-of-two padding
- Shift frequency components

### 4. Butterworth Notch Filter

The notch filter suppresses specific frequencies.

It is defined using:

- `d0` — notch cutoff distance
- `(u0, v0)` — notch center location
- `n` — filter order
- `(M, N)` — image size

The transfer function is based on a shifted Butterworth high-pass formulation.

A small epsilon may be required to avoid divide-by-zero.

### 5. Apply Filter
- Multiply FFT by notch filter transfer function
- Apply inverse FFT
- Crop to original dimensions

### 6. Visualization
The notebook displays:

- Original image
- Corrupted image
- Filtered image
- 1D frequency cross-sections
- Log-scaled frequency spectra for clarity



## How To Run

1. Launch Jupyter:

```bash
jupyter notebook
```

2. Open:

```
butterworth_notch_filter.ipynb
```

3. Run all cells.

Make sure the image path is:

```
images/zebras.jpg
```



## Key Parameters

- `ku, kv` — sinewave frequency components
- `d0` — notch cutoff radius
- `u0, v0` — notch center
- `n` — filter order

Different frequency pairs can be tested by modifying the sinewave generator.



## Notes

- Divide-by-zero can occur in notch transfer computation — add a small epsilon if needed.
- High filter orders may cause overflow warnings.
- Log transformation is applied to spectra to make frequency peaks visible.



## Outcome

- Periodic noise introduced via 2D sinewave is successfully suppressed.
- The filtered image restores the dominant spatial structure.
- Frequency-domain behavior is clearly visualized before and after filtering.
