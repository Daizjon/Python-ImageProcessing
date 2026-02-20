# Fourier Implementations (FFT Basics)

This folder contains practical implementations of Fourier-domain operations using the Fast Fourier Transform (FFT).

These notebooks demonstrate how common signal-processing tasks can be performed efficiently in the frequency domain.



## Contents

### fft-convolution.ipynb
FFT Basics: Convolution

Demonstrates:

- Direct convolution (`signal.convolve`)
- FFT-based convolution (`signal.fftconvolve`)
- Manual FFT pipeline:
  - FFT of signal
  - FFT of kernel
  - Multiplication in frequency domain
  - Inverse FFT
- Error comparison between spatial and frequency approaches
- Visualization of real and imaginary components

Key Concept:

Convolution in spatial domain = multiplication in frequency domain.



### fft-derivative.ipynb
FFT Basics: Derivative

Demonstrates:

- Computing derivatives using the Fourier property:

  dⁿf/dxⁿ  ↔  (jω)ⁿ F(ω)

- First and second derivatives via FFT
- Verification against analytic derivatives
- Handling periodic grids
- Use of `fftshift` and frequency indexing

Key Concept:

Differentiation becomes multiplication in the frequency domain.



### fft-gaussian.ipynb
FFT Basics: Gaussian

Demonstrates:

- Constructing a Gaussian in spatial domain
- Computing its Fourier Transform
- Inspecting magnitude and phase spectra
- Observing Gaussian self-similarity in frequency domain

Key Concept:

A Gaussian transforms to a Gaussian in the frequency domain.



### fft-upsampling.ipynb
FFT Basics: Upsampling

Demonstrates:

- Zero-padding in the frequency domain
- Spectrum shifting with `fftshift`
- Inverse FFT to obtain interpolated signal
- Visualization of upsampled signal vs original

Key Concept:

Zero-padding the Fourier spectrum increases spatial resolution (interpolation).



## Requirements

Install dependencies:

pip install numpy matplotlib scipy



## How to Run

jupyter notebook

Open each notebook and run top-to-bottom.



## Notes

- Signals are treated as periodic due to FFT assumptions.
- Small imaginary components after inverse FFT are normal numerical artifacts.
- Zero-padding length and alignment matter for accurate reconstruction.
- These notebooks pair directly with the Fourier theory PDFs in the parent folder.


