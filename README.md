# 🖼️ CompVis

> A comprehensive implementation of classical computer vision algorithms in Python

[![Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Installation](#-installation)
- [Usage](#-usage)
  - [Spatial Filters](#spatial-filters)
  - [Noise Generation](#noise-generation)
- [Command-Line Arguments](#-command-line-arguments)
- [Examples & Results](#-examples--results)
- [Project Structure](#-project-structure)
- [Roadmap](#-roadmap)
- [Credits](#-credits)
- [Notes](#-notes)

---

## 🎯 Overview

CompVis is a collection of computer vision algorithms implemented from scratch using NumPy and other basic Python libraries. This project demonstrates fundamental image processing techniques including spatial filtering, noise generation, and more.

**Perfect for:**
- 📚 Learning computer vision fundamentals
- 🔬 Academic research and assignments
- 🛠️ Quick image processing experiments
- 📊 Understanding algorithm implementations

---

## ✨ Features

### Currently Implemented

- ✅ **Spatial Filters**
  - Mean Filter (Average/Box Blur)
  - Median Filter (Salt & Pepper noise removal)
  - Gaussian Filter (Smooth blur)

- ✅ **Noise Generation**
  - Salt & Pepper noise
  - Gaussian noise

### Coming Soon

- 🔄 Frequency domain filters
- 🎨 Pixel-wise operations
- 🔍 Edge detection algorithms
- 📍 Local feature descriptors

---

## 🚀 Installation

### Prerequisites

- Python 3.6 or higher
- Tkinter (for GUI display)

### Install Tkinter (Linux)

```bash
sudo apt install python3-tk
```

### Install Python Dependencies

```bash
pip install -r requirements.txt
```

**Required packages:**
- `matplotlib` - for image visualization
- `numpy` - for numerical operations
- `pillow` - for image I/O operations

---

## 📖 Usage

### Spatial Filters

All filters follow a similar command-line interface pattern:

```bash
python3 -m spatial_filters.<filter_name> --input <path> [options]
```

#### 🔲 Mean Filter

Applies an averaging filter to smooth the image and reduce noise.

**Basic usage:**
```bash
python3 -m spatial_filters.mean --input ./images/cat_512.jpg --kernel_size 5
```

**Save and compare results:**
```bash
python3 -m spatial_filters.mean --input ./images/cat_512.jpg --kernel_size 5 --save --compare
```

**Options:**
- `--input <path>` - Path to input image (required)
- `--kernel_size <int>` - Size of the filter kernel (default: 3)
- `--save` - Save the output image
- `--compare` - Show side-by-side comparison with original

---

#### 🎯 Median Filter

Excellent for removing salt & pepper noise while preserving edges.

**Basic usage:**
```bash
python3 -m spatial_filters.median --input ./images/cat_saltpepper.jpg --kernel_size 3
```

**Save and compare results:**
```bash
python3 -m spatial_filters.median --input ./images/cat_saltpepper.jpg --kernel_size 3 --save --compare
```

**Options:**
- `--input <path>` - Path to input image (required)
- `--kernel_size <int>` - Size of the filter kernel (default: 3, use odd numbers)
- `--save` - Save the output image
- `--compare` - Show side-by-side comparison with original

**💡 Tip:** Use kernel size 3 or 5 for best results with salt & pepper noise.

---

#### 🌫️ Gaussian Filter

Applies Gaussian blur for smooth, natural-looking image smoothing.

**Basic usage:**
```bash
python3 -m spatial_filters.gaussian --input ./images/cat_512.jpg --kernel_size 5
```

**Save and compare results:**
```bash
python3 -m spatial_filters.gaussian --input ./images/cat_512.jpg --kernel_size 5 --save --compare
```

**Options:**
- `--input <path>` - Path to input image (required)
- `--kernel_size <int>` - Size of the Gaussian kernel (default: 3)
- `--save` - Save the output image
- `--compare` - Show side-by-side comparison with original

---

### Noise Generation

#### 🧂 Salt & Pepper Noise

Adds random black and white pixels to simulate sensor noise.

**Basic usage:**
```bash
python3 -m noise.saltpepper --input ./images/cat_512.jpg --output ./images/cat_noisy.jpg --percent 30 --save
```

**Preview noise:**
```bash
python3 -m noise.saltpepper --input ./images/cat_512.jpg --percent 50 --show
```

**Options:**
- `--input <path>` - Path to input image (required)
- `--output <path>` - Path to save noisy image
- `--percent <int>` - Percentage of pixels to corrupt (0-100, default: 50)
- `--save` - Save the noisy image
- `--show` - Display the noisy image

**💡 Example workflow:**
```bash
# 1. Add salt & pepper noise
python3 -m noise.saltpepper --input ./images/cat_512.jpg --output ./images/cat_noisy.jpg --percent 30 --save

# 2. Remove noise with median filter
python3 -m spatial_filters.median --input ./images/cat_noisy.jpg --kernel_size 3 --save --compare
```

---

#### 🌊 Gaussian Noise

Adds random Gaussian-distributed noise to images.

**Basic usage:**
```bash
python3 -m noise.gaussian --input ./images/cat_512.jpg --show
```

---

## 🎛️ Command-Line Arguments

### Common Arguments

| Argument | Type | Default | Description |
|----------|------|---------|-------------|
| `--input` | string | *required* | Path to input image |
| `--kernel_size` | integer | 3 | Size of filter kernel (odd numbers recommended) |
| `--save` | flag | false | Save output image to results folder |
| `--compare` | flag | false | Show side-by-side comparison with original |

### Noise-Specific Arguments

| Argument | Type | Default | Description |
|----------|------|---------|-------------|
| `--output` | string | - | Path to save noisy image |
| `--percent` | integer | 50 | Noise percentage (0-100) |
| `--show` | flag | false | Display the result |

---

## 🎨 Examples & Results

### 🔲 Mean Filter

Apply averaging filter for smoothing and noise reduction.

**Command:**
```bash
python3 -m spatial_filters.mean --input ./images/cat_512.jpg --kernel_size 5 --save --compare
```

**Input Image:**

<img src="./images/cat_512.jpg" width="400" alt="Original Image">

**Output Result:**

<img src="./results/mean_result.jpg" width="400" alt="Mean Filter Result">

**Side-by-Side Comparison:**

<img src="./results/mean/Figure_1.png" width="800" alt="Mean Filter Comparison">

*Smoothing effect with kernel size 5 - notice the reduced noise and softer details*

---

### 🎯 Median Filter

Excellent for removing salt & pepper noise while preserving edges.

**Command:**
```bash
python3 -m spatial_filters.median --input ./images/cat_saltpepper.jpg --kernel_size 3 --save --compare
```

**Input Image (with Salt & Pepper Noise):**

<img src="./images/cat_saltpepper.jpg" width="400" alt="Noisy Image">

**Output Result:**

<img src="./results/med_result.jpg" width="400" alt="Median Filter Result">

*Effective salt & pepper noise removal while preserving edges - notice the clean result with sharp edges maintained*

---

### 🌫️ Gaussian Filter

Natural smooth blur using Gaussian kernel.

**Command:**
```bash
python3 -m spatial_filters.gaussian --input ./images/cat_512.jpg --kernel_size 5 --save --compare
```

**Input Image:**

<img src="./images/cat_512.jpg" width="400" alt="Original Image">

**Output Result:**

<img src="./results/gaus_result.jpg" width="400" alt="Gaussian Filter Result">

*Natural smooth blur - notice the gradual, aesthetically pleasing blur effect*

---

### 🧂 Noise Generation Example

**Adding Salt & Pepper Noise:**

```bash
python3 -m noise.saltpepper --input ./images/cat_512.jpg --output ./results/cat_noisy.jpg --percent 30 --save
```

**Before (Original):**

<img src="./images/cat_512.jpg" width="350" alt="Original">

**After (30% Salt & Pepper Noise):**

<img src="./results/cat_noisy.jpg" width="350" alt="With Noise">

---

## 📁 Project Structure

```
CompVis/
├── images/                 # Sample input images
│   ├── cat_512.jpg
│   ├── cat_saltpepper.jpg
│   ├── lush_512.jpg
│   └── fog_512.jpg
├── spatial_filters/        # Spatial domain filters
│   ├── mean.py            # Mean/Average filter
│   ├── median.py          # Median filter
│   └── gaussian.py        # Gaussian filter
├── noise/                  # Noise generation modules
│   ├── saltpepper.py      # Salt & pepper noise
│   └── gaussian.py        # Gaussian noise
├── utils/                  # Utility functions
│   └── utils.py           # Image I/O, convolution, display
├── results/                # Output images and comparisons
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

---

## 🗺️ Roadmap

### ✅ Completed
- [x] Spatial filters (mean, median, gaussian)
- [x] Noise generation (salt & pepper, gaussian)
- [x] Side-by-side comparison visualization

### 🔄 In Progress
- [ ] Frequency domain filters (High pass, Low pass)
- [ ] Filter variations (Ideal, Gaussian, Butterworth)

### 📅 Planned
- [ ] Pixel-wise operations (contrast, brightness, grayscale)
- [ ] White balancing algorithms
- [ ] Retinex algorithm
- [ ] Edge detection (LoG, Canny)
- [ ] Local descriptors (Corner detection, SIFT, Gabor Filter, LBP)
- [ ] Morphological operations
- [ ] Histogram equalization
- [ ] Image segmentation algorithms

---

## 📷 Credits

**Sample Images:** Photographed at IIT Kharagpur

**License:** MIT License (see [LICENSE](LICENSE))

---

## 📝 Notes

- All filters are implemented from scratch using NumPy
- Images are processed in RGB color space (each channel independently)
- Results are saved in the `results/` directory when using `--save`
- Use `--compare` flag to see before/after side-by-side visualization

---

**Happy Image Processing! 🎉**
