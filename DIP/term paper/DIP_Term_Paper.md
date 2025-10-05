---
title: "Digital Image Processing (DIP) — Term Paper"
author: ""
date: 2025-09-15
course: "Digital Image Processing"
---



# Digital Image Processing (DIP)



## Abstract

This term paper summarizes key concepts of Digital Image Processing (DIP) including image representation, acquisition, spatial domain enhancement, histogram techniques, derivatives and filters, morphological operations, region-based segmentation, and thresholding. Each section includes concise definitions, essential equations, and brief examples or notes where helpful.



## Table of Contents

- Introduction
- Image, Digital Image, BPP
- Image Acquisition and Digitization
- Representing Digital Images
- Image Interpolation
- Neighbours and Adjacency
- Enhancement in Spatial Domain and Spatial Filtering
- Image Histogram; Local and Global Histogram Processing

- Spatial Correlation (1D, 2D) & Convolution
- Histogram Processing Techniques
- Smoothing and Sharpening; Sharpening Filters
- First-order and Second-order Derivatives and Properties
- Morphological Operations and Structuring Element
  - Erosion
  - Dilation
  - Opening
  - Closing (optional: top-hat and bottom-hat)
- Region Growing; Region Splitting and Merging
- Segmentation and Basics
- Image Binarization and Thresholding
- Laplacian and Enhanced Laplacian Filters
- Smoothing Spatial Filters
- Conclusion
- References and Local Notes

---



## Image, Digital Image, BPP

- Image: A function f(x, y) that maps coordinates (continuous) to intensity or color values.
- Digital image: A discrete approximation g[i, j] obtained by sampling and quantizing f(x, y).
- Bits per pixel (BPP): Number of bits used to represent each pixel. For a grayscale image with L gray levels, BPP = log2(L). Example: 8 BPP → 256 gray levels.



### Short example

Consider a continuous image f(x, y). Sampling at intervals Δx and Δy yields g[i, j] = f(iΔx, jΔy). Quantizing to 8 bits maps continuous intensities to integers 0..255.



## Image Acquisition and Digitization

- Acquisition: Capturing images via sensors (CCD/CMOS) or scanners.
- Digitization: Two-step process — sampling (spatially discretize coordinates) and quantization (discretize amplitude values). Sampling rate controls spatial resolution; quantization levels control gray-scale resolution.



### Notes on aliasing

If sampling frequency is inadequate (below Nyquist), high-frequency image content causes aliasing. Anti-aliasing low-pass filters (optical or pre-sampling) reduce this effect.



## Representing Digital Images

- Common representations: 2D arrays for grayscale, 3D arrays for color (channels).
- File formats: BMP, PNG, JPEG, TIFF — trade-offs include compression (lossy/lossless) and metadata support.



### Color spaces

- RGB: direct channel representation.
- HSV / HSL: useful for color-based segmentation.
- YCbCr / YUV: used in compression; separates luminance from chrominance.



## Image Interpolation

- Purpose: Estimate image values at non-grid positions (resizing, warping).
- Methods:
  - Nearest-neighbor: Fast, blocky artifacts.
  - Bilinear: Linear interpolation in two dimensions; smoother.
  - Bicubic: Uses cubic polynomials; smoother and preserves more detail.



### Formulas (1D view)

- Linear interpolation between x0 and x1: f(x) ≈ f(x0) (1 − t) + f(x1) t, where t = (x − x0)/(x1 − x0).
- Cubic interpolation uses four points and cubic polynomials; more complex but smoother.



## Neighbours and Adjacency

- Pixel neighbourhood: For pixel (i, j), typical neighbourhoods are 4-neighbour (N4), 8-neighbour (N8), and m×n windows.
- Adjacency types:
  - 4-adjacency: pixels that share an edge.
  - 8-adjacency: pixels that share an edge or a corner.
  - m-adjacency (mixed): to avoid connectivity paradoxes—use 4-adjacency for foreground, 8 for background or vice versa.



### Example

For pixel p at (i, j): 4-neighbours: (i−1,j), (i+1,j), (i,j−1), (i,j+1). 8-neighbours add diagonals: (i±1, j±1).



## Enhancement in Spatial Domain and Spatial Filtering

- Spatial domain methods operate directly on pixels. A spatial filter replaces a pixel by a function of its neighbourhood.
- Linear filters: convolution with a kernel (e.g., smoothing, derivative kernels).
- Non-linear filters: median, morphological filters.



### Practical tip

Always consider boundary handling (zero-padding, replication, reflection) when applying spatial filters.



## Image Histogram; Local and Global Histogram Processing

- Image histogram: h(rk) counts frequency of intensity rk.
- Global histogram processing: e.g., histogram equalization using cumulative distribution function (CDF) to remap intensities for global contrast enhancement.
- Local (adaptive) histogram processing: apply histogram-based transforms to subregions to enhance local contrast (e.g., CLAHE).



### Pseudocode: basic histogram equalization

1. Compute histogram h(r) for r in [0, L−1].
2. Compute normalized CDF: cdf(r) = Σ_{s=0..r} h(s) / (M×N).
3. Map intensity r to s = floor((L−1) × cdf(r)).



## Spatial Correlation (1D, 2D) & Convolution

- 1D correlation: (f ⋆ h)[n] = Σ_k f[k] h[n + k]
- 2D correlation: (f ⋆ h)[i, j] = Σ_m Σ_n f[m, n] h[i + m, j + n]
- Convolution: (f * h)[i, j] = Σ_m Σ_n f[m, n] h[i - m, j - n]
- For symmetric kernels, correlation and convolution are equivalent. Convolution used in linear shift-invariant filtering; implement via kernel flipping.



### Relationship to frequency domain

Convolution in spatial domain ↔ Multiplication in frequency domain: F {f * h} = F{f} · F{h}, enabling FFT-based fast convolution for large kernels.



## Histogram Processing Techniques

- Histogram equalization: transform s = T(r) where T is proportional to the CDF of the histogram.
- Histogram matching (specification): remap image histogram to match a specified histogram.



## Concept of Smoothing and Sharpening; Sharpening Filters

- Smoothing reduces noise and detail — commonly via averaging (box filter) or Gaussian smoothing.
- Sharpening enhances edges and fine detail — often via derivatives or high-pass filters.
- Unsharp masking: sharpened = original + α (original − blurred).



### Example kernel: high-boost filtering

High-boost filter adds a scaled version of the input to its high-pass version: g = A f − f * h_lowpass (or g = f + λ (f − f_blur)).



## First-order Derivative & Its Properties

- First-order derivative highlights gradient (edge strength and direction): in 2D, gradient ∇f = [∂f/∂x, ∂f/∂y].
- Magnitude: |∇f| = sqrt((∂f/∂x)^2 + (∂f/∂y)^2). Common discrete approximations: Roberts, Prewitt, Sobel operators.
- Properties: detects edges, sensitive to noise, orientation-specific.



### Discrete Sobel masks

- Gx = [[-1 0 1], [-2 0 2], [-1 0 1]]
- Gy = [[-1 -2 -1], [0 0 0], [1 2 1]]



## Second-order Derivative & Its Properties

- Second derivative measures curvature; zero-crossings often indicate edges.
- Laplacian ∇^2 f = ∂^2 f/∂x^2 + ∂^2 f/∂y^2 — isotropic second derivative used for edge detection.
- Discrete Laplacian kernels: e.g., 3×3 with center 4 and -1 for orthogonal neighbours, or center 8 and -1 for all eight neighbours.



### Zero-crossings

Edges from second-derivative methods are often found at zero-crossings of the Laplacian; apply zero-crossing detection after filtering.



## Morphological Operations and Structuring Element

- Morphology works on binary or grayscale images using a structuring element (SE) B that probes image shapes.
- Basic SE shapes: disk, square, line — defined by a set of coordinates relative to the origin.



### Erosion

- Erosion (A ⊖ B): shrinks objects. For binary images, output pixel is 1 only if B translated to that position fits entirely within A.



### Example (binary)

If B is a 3×3 all-ones SE, erosion removes any foreground pixel that has a background pixel in its 3×3 neighbourhood.



### Dilation

- Dilation (A ⊕ B): grows objects. Output pixel is 1 if B reflected and translated overlaps A.



### Morphological Opening

- Opening (A ◦ B) = (A ⊖ B) ⊕ B. Removes small objects and smooths boundaries.



### Morphological Closing

- Closing (A • B) = (A ⊕ B) ⊖ B. Fills small holes and connects nearby objects.
- Optional: Top-hat (A − (A ◦ B)) and Bottom-hat ((A • B) − A) highlight small bright/dark features respectively.



## Region Growing

- Region growing: start from seeds and add neighbouring pixels that satisfy a homogeneity criterion (e.g., intensity difference below threshold). Iterative process until no more pixels qualify.



## Region Splitting and Merging

- Splitting: divide image recursively (e.g., quadtree) until regions satisfy a homogeneity test.
- Merging: combine adjacent regions if their union meets the homogeneity criterion. Combined splitting and merging yields balanced segmentation.



### Example: quadtree

Start with entire image; if not homogeneous, split into four quadrants; repeat for each quadrant until homogeneity or minimum block size.



## Segmentation and Basics

- Segmentation: partition image into meaningful regions. Methods include thresholding, edge-based, region-based, clustering (k-means), and model-based.



## Image Binarization and Thresholding

- Global thresholding: choose T, produce binary image B(i,j) = 1 if I(i,j) ≥ T else 0.
- Otsu's method: automatic selection of threshold that minimizes within-class variance (maximizes between-class variance).



### Otsu summary

Compute class probabilities and means for all possible thresholds; choose threshold maximizing between-class variance σ_b^2 = ω_0 ω_1 (μ_0 − μ_1)^2.



## Laplacian Filter and Enhanced Laplacian Filter

- Laplacian filter is a second-derivative operator for edge detection. Example kernel:

-   [ 0  -1   0]
-   [-1  4  -1]
-   [ 0  -1   0]

- Enhanced Laplacian: combine with original (Laplacian of Gaussian or add scaled Laplacian to original) to sharpen: g = f − λ (∇^2 f).



### LoG (Laplacian of Gaussian)

Apply Gaussian smoothing first, then Laplacian to reduce noise sensitivity: LoG(x,y) = ∇^2(Gσ * f). Often implemented by convolving with a discrete LoG kernel.



## Smoothing Spatial Filters

- Box (mean) filter: average over neighbourhood; kernel values 1/(mn).
- Gaussian filter: weights decrease with distance; separable (apply 1D Gaussian along rows and columns for efficiency).
- Median filter: non-linear filter useful for salt-and-pepper noise.



## Additional content from DIP_Lectures.pdf

 To demonstrate that image processing is based
on strong mathematical principles, applied to
digital images via numerical schemes

A digital image is a representation of a two-
image as a finite set of digital
dimensional
values, called picture elements or pixels.

Alpha is for transparency (0.0 fully transparent
and 1.0 full opaque (not Transparent)).

Depending on context, synonyms of pixel as
follows:
 pel,
 sample,
 byte,
 bit,
 dot, and
 spot.
Pixels can be used as a unit of measure such as:
2400 pixels per inch, 640 pixels per line, or
spaced 10 pixels apart.

For printer devices, dpi is a measure of the
ink droplet)
printer's density of dot
placement.

A high-quality photographic image may be
printed with 600 ppi on a 1200 dpi inkjet
printer.

The number of distinct colors that can be
represented by a pixel depends on the number
of bits per pixel (bpp).

A 1 bpp image uses 1-bit for each pixel, so
each pixel can be either on or off. Each
additional bit doubles the number of colors
available, so a 2 bpp image can have 4 colors,
and a 3 bpp image can have 8 colors.

8 bpp, 28 = 256 colors
16 bpp, 216 = 65,536 colors ("Highcolor" )
24 bpp, 224 = 16,777,216 colors ("Truecolor")

the bits
Depth is normally the sum of
allocated to each of the red, green, and blue
components.

215
-> Means 5 red, 5 green and 5 blue
(divide by 3 channels and always red and
blue are equal).

As the human eye is more sensitive to
two
errors in green than in the other
primary colors.

For applications involving transparency, the 16
bits may be divided into five bits each of red,
for
and blue, with one bit
green,
transparency.

On some systems, 32-bit depth is available: this
means that each 24-bit pixel has an extra 8 bits
to describe its opacity (for purposes of
combining with another image).

In most digital cameras, the sensor array is
covered with a patterned color
filter
having

The term gray level is often used to refer to the
intensity of monochrome images.

A monochromatic object or image reflects colors in
shades of limited colors or hues. Images using only
shades of grey (with or without black or white) are
called grayscale or black-and-white.

Hue is one of the main properties (called color
appearance parameters) of a color.

Digital image processing refers to processing digital
images by means of a digital computer.

 A digital image is composed of a finite number of
elements, each of which has a particular location
and value.

Monochromatic Light
 Light that is void of color is called monochromatic
light. (A photograph or picture developed or executed in black and white or in
varying tones of only one color.)

The sensor array produces outputs proportional
integral of the light received at each sensor.

Digital and analog circuitry sweep these outputs and convert
them to an analog signal which is then digitized by another
section of the imaging system

This is a plot of amplitude
values of the continuous image
along the line segment AB.
Random variations are due to
image noise.

grid with the same pixel
Create an imaginary 12 X 12
spacing as the original and then shrink it so that it fits exactly
over the original image.

grid with the same pixel
Create an imaginary 12 X 12
spacing as the original and then shrink it so that it fits exactly
over the original image.

 For any specific location (x, y), the value of the output
image g at those coordinates is equal to the result of
applying T to the neighborhood with origin at (x, y).

 For any specific location (x, y), the value of the output
image g at those coordinates is equal to the result of
applying T to the neighborhood with origin at (x, y).

 For any specific location (x, y), the value of the output
image g at those coordinates is equal to the result of
applying T to the neighborhood with origin at (x, y).

 For any specific location (x, y), the value of the output
image g at those coordinates is equal to the result of
applying T to the neighborhood with origin at (x, y).

 For any specific location (x, y), the value of the output
image g at those coordinates is equal to the result of
applying T to the neighborhood with origin at (x, y).

 For any specific location (x, y), the value of the output
image g at those coordinates is equal to the result of
applying T to the neighborhood with origin at (x, y).

 For any specific location (x, y), the value of the output
image g at those coordinates is equal to the result of
applying T to the neighborhood with origin at (x, y).

 Input gray level R
 Produce an image of higher 
contrast than the original.
 Below a threshold (m), image 
is compressed towards black
 Values of r lower than m are

that
Condition
output intensity values will never
be less than corresponding input
values thus preventing artifacts
created by reversals of intensity.

Condition 2 guarantees that the
range of output intensities is the
same as the input.

– pr(r): the equalized histogram of the given image
– ps(s): the equalized histogram of the output image

 For any specific location (x, y), the value of the output
image g at those coordinates is equal to the result of
applying T to the neighborhood with origin at (x, y).

A spatial averaging filter in
which all coefficients are
equal is called a box filter.

This mask yields a weighted
average.
gives more
importance to the center
pixels and the 4-neighbors.

h = fspecial('average',5); % h = fspecial('average',hsize)
localMean = imfilter(I,h,'replicate');
imshowpair(I,localMean,'montage')

To highlight fine detail in an image or to enhance detail that 
has been blurred, either in error or as a natural effect of a 
particular method of image acquisition.

Blurring vs Sharpening 
•Blurring/smooth is done in spatial domain by pixel averaging 
in a neighbors, it is a process of integration.

• Sharpening is an inverse process, to find the difference by 
the neighborhood, done by spatial differentiation. spatial 
differentiation.

•The strength of the response of a derivative operator is 
proportional to the degree of operator is proportional to 
the degree of discontinuity of the image at the point at 
which the operator is applied.

–enhances edges and other discontinuities (noise) 
–deemphasizes area with slowly varying gray-level 
values.

 Gray-ramp (smooth transition betn white and black)
 Isolated noise point
 Line
 Edge

 Morphological image processing pursues the
removing these imperfections by
goals of
accounting for the form and structure of the
image.

numerous
imperfections. In particular, the binary regions
produced by simple thresholding are distorted by
noise and texture.

Morphological image processing is a collection
of non-linear (non-sequential) operations related to
the shape or morphology of features in an image.

Morphological operations rely only on the relative
ordering of pixel values and therefore are especially
suited to the processing of binary images.

Morphological techniques probe an image with a
small
template called a structuring
element.

The structuring element is positioned at all possible
locations in the image and it is compared with the
corresponding neighborhood of pixels.

The most basic morphological operations are
dilation and erosion.
In a morphological operation, the value of each
pixel in the output image is based on a comparison of
the corresponding pixel in the input image with its
neighbors.
By
the
size
neighborhood, you can construct a morphological
operation that is sensitive to specific shapes in the
input image

Structuring elements can be seen in 3 different
ways in the test input image which are as follows:

1) Structuring element fits the image region
2) Structuring element hits (intersects) the image

Morphological techniques probe an image with a
small
template called a structuring
element.

The structuring element is a small binary image,
i.e. a small matrix of pixels, each with a value of zero
or one:

An essential part of the dilation and erosion
operations is the structuring element used to probe
the input image.

A structuring element is a matrix consisting of
only 0's and 1's that can have any arbitrary shape
and size.

There are two main characteristics that are directly
related to structuring elements:

For example, the structuring element can be a
circle, square, diamond etc.
By choosing a particular structuring element, one
sets a way of differentiating some objects (or parts
of objects) from others, according to their shape or
spatial orientation.

For example, one structuring element can be a 3 x 3
square or a 21 x 21 square.
Setting the size of the structuring element is similar
to setting the observation scale, and setting the
criterion to differentiate image objects or features
according to size.

Dilation adds pixels to the boundaries of objects in
an image, while
Erosion removes pixels on object boundaries.

The number of pixels added or removed from the
objects in an image depends on the size and shape of
the structuring element used to process the image.

Erosion generally decreases the sizes of objects and
removes small anomalies by subtracting objects with
a radius smaller than the structuring element.

With grayscale
the
brightness (and therefore the size) of bright objects
on a dark background by taking the neighborhood
minimum when passing the structuring element over
the image.

With binary images, erosion completely removes
objects smaller than the structuring element and
removes perimeter pixels from larger image objects
(the continuous line forming the boundary of a closed
geometrical figure.)

Dilation generally increases the sizes of objects,
filling in holes and broken areas, and connecting
areas that are separated by spaces smaller than the
size of the structuring element.

With grayscale images, dilation increases
the
brightness of objects by taking the neighborhood
maximum when passing the structuring element over
the image.

With binary images, dilation connects areas that are
separated by spaces smaller than the structuring
element and adds pixels to the perimeter of each
image object.

The erosion of a binary image f by a structuring
element s (denoted f Ɵ s) produces a new binary
image g = f Ɵ s with ones in all locations (x,y) of a
structuring element's origin at which that structuring
element s fits the input image f,

Erosion with small
square
structuring elements shrinks an image by stripping
away a layer of pixels from both the inner and outer
boundaries of regions.

The holes and gaps between different
become larger, and small details are eliminated.

The value of the output pixel is the minimum value 
of all the pixels in the input pixel's neighborhood.

In a binary image, if any of the pixels is set to 0,
the output pixel is set to 0.

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 1 1 1 0 0 0 0 0 0 0 0 0 0
0 0 1 1 1 1 1 0 0 0 0 0 0 0 0 0
0 0 1 1 1 1 1 0 0 0 0 1 1 1 0 0
0 0 1 1 1 1 0 0 0 0 1 1 1 1 0 0
0 0 0 1 1 0 0 0 0 1 1 1 1 1 0 0
0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0
0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 0
0 0 0 0 1 1 1 1 1 0 0 0 0 0 0 0
0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 1 1 1 0 0 0 0 0 0 0 0 0 0
0 0 1 1 1 1 1 0 0 0 0 0 0 0 0 0
0 0 1 1 1 1 1 0 0 0 0 1 1 1 0 0
0 0 1 1 1 1 0 0 0 0 1 1 1 1 0 0
0 0 0 1 1 0 0 0 0 1 1 1 1 1 0 0
0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0
0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 0
0 0 0 0 1 1 1 1 1 0 0 0 0 0 0 0
0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 1 1 0 0 0 0 0 0 0 0 0 0
0 0 0 1 1 1 1 1 0 0 0 0 0 0 0 0 0
0 0 0 1 1 1 1 1 0 0 0 0 1 1 1 0 0
0 0 0 1 1 1 1 0 0 0 0 1 1 1 1 0 0
0 0 0 0 1 1 0 0 0 0 1 1 1 1 1 0 0
0 0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0
0 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 0
0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 0 0
0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 1 1 1 0 0 0 0 0 0 0 0 0 0
0 0 1 1 1 1 1 0 0 0 0 0 0 0 0 0
0 0 1 1 1 1 1 0 0 0 0 1 1 1 0 0
0 0 1 1 1 1 0 0 0 0 1 1 1 1 0 0
0 0 0 1 1 0 0 0 0 1 1 1 1 1 0 0
0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0
0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 0
0 0 0 0 1 1 1 1 1 0 0 0 0 0 0 0
0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 1 1 0 0 0 0 0 0 0 0 0 0
0 0 0 1 1 1 1 1 0 0 0 0 0 0 0 0 0
0 0 0 1 1 1 1 1 0 0 0 0 1 1 1 0 0
0 0 0 1 1 1 1 0 0 0 0 1 1 1 1 0 0
0 0 0 0 1 1 0 0 0 0 1 1 1 1 1 0 0
0 0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0
0 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 0
0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 0 0
0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 1 1 1 0 0 0 0 0 0 0 0 0 0
0 0 1 1 1 1 1 0 0 0 0 0 0 0 0 0
0 0 1 1 1 1 1 0 0 0 0 1 1 1 0 0
0 0 1 1 1 1 0 0 0 0 1 1 1 1 0 0
0 0 0 1 1 0 0 0 0 1 1 1 1 1 0 0
0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0
0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 0
0 0 0 0 1 1 1 1 1 0 0 0 0 0 0 0
0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 1 1 0 0 0 0 0 0 0 0 0 0
0 0 0 1 1 1 1 1 0 0 0 0 0 0 0 0 0
0 0 0 1 1 1 1 1 0 0 0 0 1 1 1 0 0
0 0 0 1 1 1 1 0 0 0 0 1 1 1 1 0 0
0 0 0 0 1 1 0 0 0 0 1 1 1 1 1 0 0
0 0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0
0 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 0
0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 0 0
0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 1 1 1 1 1 0 0 0 0 0 0 0 0 0
0 0 1 1 1 1 1 0 0 0 0 1 1 1 0 0
0 0 1 1 1 1 0 0 0 0 1 1 1 1 0 0
0 0 0 1 1 0 0 0 0 1 1 1 1 1 0 0
0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0
0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 0
0 0 0 0 1 1 1 1 1 0 0 0 0 0 0 0
0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 1 1 0 0 0 0 0 0 0 0 0 0
0 0 0 1 1 1 1 1 0 0 0 0 0 0 0 0 0
0 0 0 1 1 1 1 1 0 0 0 0 1 1 1 0 0
0 0 0 1 1 1 1 0 0 0 0 1 1 1 1 0 0
0 0 0 0 1 1 0 0 0 0 1 1 1 1 1 0 0
0 0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0
0 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 0
0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 0 0
0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 1 1 1 1 1 0 0 0 0 0 0 0 0 0
0 0 1 1 1 1 1 0 0 0 0 1 1 1 0 0
0 0 1 1 1 1 0 0 0 0 1 1 1 1 0 0
0 0 0 1 1 0 0 0 0 1 1 1 1 1 0 0
0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0
0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 0
0 0 0 0 1 1 1 1 1 0 0 0 0 0 0 0
0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 1 1 0 0 0 0 0 0 0 0 0 0
0 0 0 1 1 1 1 1 0 0 0 0 0 0 0 0 0
0 0 0 1 1 1 1 1 0 0 0 0 1 1 1 0 0
0 0 0 1 1 1 1 0 0 0 0 1 1 1 1 0 0
0 0 0 0 1 1 0 0 0 0 1 1 1 1 1 0 0
0 0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0
0 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 0
0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 0 0
0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0
0 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0
0 0 1 1 1 1 0 0 0 0 1 1 1 1 0 0
0 0 0 1 1 0 0 0 0 1 1 1 1 1 0 0
0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0
0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 0
0 0 0 0 1 1 1 1 1 0 0 0 0 0 0 0
0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 1 1 0 0 0 0 0 0 0 0 0 0
0 0 0 1 1 1 1 1 0 0 0 0 0 0 0 0 0
0 0 0 1 1 1 1 1 0 0 0 0 1 1 1 0 0
0 0 0 1 1 1 1 0 0 0 0 1 1 1 1 0 0
0 0 0 0 1 1 0 0 0 0 1 1 1 1 1 0 0
0 0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0
0 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 0
0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 0 0
0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0
0 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0
0 0 0 1 1 0 0 0 0 1 1 1 1 1 0 0
0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0
0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 0
0 0 0 0 1 1 1 1 1 0 0 0 0 0 0 0
0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 1 1 0 0 0 0 0 0 0 0 0 0
0 0 0 1 1 1 1 1 0 0 0 0 0 0 0 0 0
0 0 0 1 1 1 1 1 0 0 0 0 1 1 1 0 0
0 0 0 1 1 1 1 0 0 0 0 1 1 1 1 0 0
0 0 0 0 1 1 0 0 0 0 1 1 1 1 1 0 0
0 0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0
0 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 0
0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 0 0
0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0
0 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0
0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0
0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 0
0 0 0 0 1 1 1 1 1 0 0 0 0 0 0 0
0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 1 1 0 0 0 0 0 0 0 0 0 0
0 0 0 1 1 1 1 1 0 0 0 0 0 0 0 0 0
0 0 0 1 1 1 1 1 0 0 0 0 1 1 1 0 0
0 0 0 1 1 1 1 0 0 0 0 1 1 1 1 0 0
0 0 0 0 1 1 0 0 0 0 1 1 1 1 1 0 0
0 0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0
0 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 0
0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 0 0
0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0
0 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0
0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0
0 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0
0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 0
0 0 0 0 1 1 1 1 1 0 0 0 0 0 0 0
0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 1 1 0 0 0 0 0 0 0 0 0 0
0 0 0 1 1 1 1 1 0 0 0 0 0 0 0 0 0
0 0 0 1 1 1 1 1 0 0 0 0 1 1 1 0 0
0 0 0 1 1 1 1 0 0 0 0 1 1 1 1 0 0
0 0 0 0 1 1 0 0 0 0 1 1 1 1 1 0 0
0 0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0
0 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 0
0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 0 0
0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0
0 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0
0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0
0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 0
0 0 0 0 1 1 1 1 1 0 0 0 0 0 0 0
0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 1 1 0 0 0 0 0 0 0 0 0 0
0 0 0 1 1 1 1 1 0 0 0 0 0 0 0 0 0
0 0 0 1 1 1 1 1 0 0 0 0 1 1 1 0 0
0 0 0 1 1 1 1 0 0 0 0 1 1 1 1 0 0
0 0 0 0 1 1 0 0 0 0 1 1 1 1 1 0 0
0 0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0
0 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 0
0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 0 0
0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0
0 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0
0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0
0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0
0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 0
0 0 0 0 1 1 1 1 1 0 0 0 0 0 0 0
0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 1 1 0 0 0 0 0 0 0 0 0 0
0 0 0 1 1 1 1 1 0 0 0 0 0 0 0 0 0
0 0 0 1 1 1 1 1 0 0 0 0 1 1 1 0 0
0 0 0 1 1 1 1 0 0 0 0 1 1 1 1 0 0
0 0 0 0 1 1 0 0 0 0 1 1 1 1 1 0 0
0 0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0
0 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 0
0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 0 0
0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0
0 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0
0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0
0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0
0 0 0 0 1 1 1 1 1 0 0 0 0 0 0 0
0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 1 1 0 0 0 0 0 0 0 0 0 0
0 0 0 1 1 1 1 1 0 0 0 0 0 0 0 0 0
0 0 0 1 1 1 1 1 0 0 0 0 1 1 1 0 0
0 0 0 1 1 1 1 0 0 0 0 1 1 1 1 0 0
0 0 0 0 1 1 0 0 0 0 1 1 1 1 1 0 0
0 0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0
0 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 0
0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 0 0
0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0
0 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0
0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0
0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 1 0 0 0 0 0 0 0 0
0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 1 1 0 0 0 0 0 0 0 0 0 0
0 0 0 1 1 1 1 1 0 0 0 0 0 0 0 0 0
0 0 0 1 1 1 1 1 0 0 0 0 1 1 1 0 0
0 0 0 1 1 1 1 0 0 0 0 1 1 1 1 0 0
0 0 0 0 1 1 0 0 0 0 1 1 1 1 1 0 0
0 0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0
0 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 0
0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 0 0
0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0
0 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0
0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0
0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 1 0 0 0 0 0 0 0 0
0 0 0 0 0 1 1 1 0 0 0 0 0 0 0 0
0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 1 1 0 0 0 0 0 0 0 0 0 0
0 0 0 1 1 1 1 1 0 0 0 0 0 0 0 0 0
0 0 0 1 1 1 1 1 0 0 0 0 1 1 1 0 0
0 0 0 1 1 1 1 0 0 0 0 1 1 1 1 0 0
0 0 0 0 1 1 0 0 0 0 1 1 1 1 1 0 0
0 0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0
0 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 0
0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 0 0
0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0
0 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0
0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0
0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 1 0 0 0 0 0 0 0 0
0 0 0 0 0 1 1 1 0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 1 1 1 0 0 0 0 0 0
0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 1 1 0 0 0 0 0 0 0 0 0 0
0 0 0 1 1 1 1 1 0 0 0 0 0 0 0 0 0
0 0 0 1 1 1 1 1 0 0 0 0 1 1 1 0 0
0 0 0 1 1 1 1 0 0 0 0 1 1 1 1 0 0
0 0 0 0 1 1 0 0 0 0 1 1 1 1 1 0 0
0 0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0
0 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 0
0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 0 0
0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0
0 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0
0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0
0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 1 0 0 0 0 0 0 0 0
0 0 0 0 0 1 1 1 0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 1 1 1 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 1 1 0 0 0 0 0 0 0 0 0 0
0 0 0 1 1 1 1 1 0 0 0 0 0 0 0 0 0
0 0 0 1 1 1 1 1 0 0 0 0 1 1 1 0 0
0 0 0 1 1 1 1 0 0 0 0 1 1 1 1 0 0
0 0 0 0 1 1 0 0 0 0 1 1 1 1 1 0 0
0 0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0
0 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 0
0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 0 0
0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0
0 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0
0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0
0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 1 0 0 0 0 0 0 0 0
0 0 0 0 0 1 1 1 0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 1 1 1 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 1 1 0 0 0 0 0 0 0 0 0 0
0 0 0 1 1 1 1 1 0 0 0 0 0 0 0 0 0
0 0 0 1 1 1 1 1 0 0 0 0 1 1 1 0 0
0 0 0 1 1 1 1 0 0 0 0 1 1 1 1 0 0
0 0 0 0 1 1 0 0 0 0 1 1 1 1 1 0 0
0 0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0
0 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 0
0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 0 0
0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0
0 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0
0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0
0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 1 0 0 0 0 0 0 0 0
0 0 0 0 0 1 1 1 0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 1 1 1 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

Rules:
1) Use zero ( 0 ) padding for each side.
2) Place the Structuring element and get the result straightway
Using the neighbors and erosion rule.
3) Make sure you only update values for origin only.

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 1 1 1 0 0 0 0 0 0 0 0 0 0
0 0 1 1 1 1 1 0 0 0 0 0 0 0 0 0
0 0 1 1 1 1 1 0 0 0 0 1 1 1 0 0
0 0 1 1 1 1 0 0 0 0 1 1 1 1 0 0
0 0 0 1 1 0 0 0 0 1 1 1 1 1 0 0
0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0
0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 0
0 0 0 0 1 1 1 1 1 0 0 0 0 0 0 0
0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 1 1 0 0 0 0 0 0 0 0 0 0 0
0 0 0 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0
0 0 0 1 1 1 1 1 0 0 0 0 1 1 1 0 0 0
0 0 0 1 1 1 1 0 0 0 0 1 1 1 1 0 0 0
0 0 0 0 1 1 0 0 0 0 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0
0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 0
0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 0 0
0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 0 0 0
0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0
0 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0
0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0
0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 1 0 0 0 0 0 0 0 0
0 0 0 0 0 1 1 1 0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 1 1 1 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 1 1 0 0 0 0 0 0 0 0 0 0 0
0 0 0 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0
0 0 0 1 1 1 1 1 0 0 0 0 1 1 1 0 0 0
0 0 0 1 1 1 1 0 0 0 0 1 1 1 1 0 0 0
0 0 0 0 1 1 0 0 0 0 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0
0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 0
0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 0 0
0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 0 0 0
0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

clc,
close all;
clear all;
I = imread('D:\matlab_folder\week_9.png');
figure, imshow(I);
SE = strel('square',5);
J = imerode(I,SE);
figure, imshow(J);

Just change line number 7 for the previous slide and play with 
different shapes of structuring element

-> SE = strel(‘diamond’,5);
OR -> SE = strel(‘disk’,5);
OR -> SE = strel(‘octagon’,5);
OR -> SE = strel(‘line’,len,deg); %len =lenth , deg = degree
OR -> SE = strel(‘rectangle’,[m n]);
OR -> SE = strel(‘cube’,5);
OR -> SE = strel('square',5);

Larger structuring elements have a more pronounced
effect, the result of erosion with a large structuring
element being similar
to the result obtained by
iterated erosion using a smaller structuring element of
the same shape.

If s1 and s2 are a pair of structuring elements identical
in shape, with s2 twice the size of s1,

clc,
%close all;
clear all;
I = imread('D:\matlab_folder\2.jpg');
figure, imshow(I);
SE = strel('rectangle',[4 8]);
J = imerode(I,SE);
%J = imerode(J,SE);
figure, imshow(J);

clc,
%close all;
clear all;
I = imread('D:\matlab_folder\2.jpg');
figure, imshow(I);
SE = strel('rectangle',[4 4]);
J = imerode(I,SE);
J = imerode(J,SE);
figure, imshow(J);

Erosion removes small-scale details from a binary
image but simultaneously reduces the size of regions
of interest, too.

By subtracting the eroded image from the original
image, boundaries of each region can be found:

where f
is an image of the regions, s is a 3×3
structuring element, and b is an image of the region
boundaries.

clc,
%close all;
clear all;
I = imread('D:\matlab_folder\2.jpg');
figure, imshow(I);
SE = strel('rectangle',[4 4]);
J = imerode(I,SE);
figure, imshow(J);
K = I - J;
figure, imshow(K);

The dilation of an image f by a structuring
s) produces a new binary
element s (denoted f
image g = f
s with ones in all locations (x,y) of a
structuring element's origin at which that structuring
element s hits the input image f,
i.e. g(x,y) = 1 if s hits f
and

Dilation has the opposite effect to erosion as it adds a
layer of pixels to both the inner and outer boundaries
of regions.

The value of the output pixel is the maximum value
of all the pixels in the input pixel's neighborhood. In
a binary image, if any of the pixels is set to the
value 1, the output pixel is set to 1.

The holes enclosed by a single region and gaps
between different regions become smaller, and small
intrusions into boundaries of a region are filled in:

Results of dilation or erosion are influenced both by
the size and shape of a structuring element. Dilation
and erosion are dual operations in that they have
opposite effects. Let f c denote the complement of an
image f, i.e., the image produced by replacing 1 with
0 and vice versa. Formally, the duality is written as

where srot is the structuring element s rotated by 180.
If a structuring element is symmetrical with respect
to rotation, then srot does not differ from s.
If a binary image is considered to be a collection of
connected regions of pixels set to 1 on a background
of pixels set to 0, then erosion is the fitting of a
structuring element to these regions and dilation is
(rotated if
the fitting of a structuring element
necessary)
by
the
inversion of the result.

clc,
%close all;
clear all;
I = imread('D:\matlab_folder\2.jpg');
figure, imshow(I);
SE = strel('square',7);
J = imdilate(I,SE);
figure, imshow(J);

clc,
%close all;
clear all;
I = imread('D:\matlab_folder\2.jpg');
I1 = imcomplement(I);
figure, imshow(I);
SE = strel('square',7);
J = imerode(I1,SE);
J = imcomplement(J);
figure, imshow(J);

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 1 1 1 0 0 0 0 0 0 0 0 0 0
0 0 1 1 1 1 1 0 0 0 0 0 0 0 0 0
0 0 1 1 1 1 1 0 0 0 0 1 1 1 0 0
0 0 1 1 1 1 0 0 0 0 1 1 1 1 0 0
0 0 0 1 1 0 0 0 0 1 1 1 1 1 0 0
0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 1 1 1 0 0 0 0 0 0 0 0 0 0
0 0 1 1 1 1 1 0 0 0 0 0 0 0 0 0
0 0 1 1 1 1 1 0 0 0 0 1 1 1 0 0
0 0 1 1 1 1 0 0 0 0 1 1 1 1 0 0
0 0 0 1 1 0 0 0 0 1 1 1 1 1 0 0
0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 1 1 1 0 0 0 0 0 0 0 0 0 0
0 0 1 1 1 1 1 0 0 0 0 0 0 0 0 0
0 0 1 1 1 1 1 0 0 0 0 1 1 1 0 0
0 0 1 1 1 1 0 0 0 0 1 1 1 1 0 0
0 0 0 1 1 0 0 0 0 1 1 1 1 1 0 0
0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 1 1 1 0 0 0 0 0 0 0 0 0 0
0 0 1 1 1 1 1 0 0 0 0 0 0 0 0 0
0 0 1 1 1 1 1 0 0 0 0 1 1 1 0 0
0 0 1 1 1 1 0 0 0 0 1 1 1 1 0 0
0 0 0 1 1 0 0 0 0 1 1 1 1 1 0 0
0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 1 1 1 1 1 0 0 0 0 0 0 0 0 0
0 0 0 1 1 1 0 0 0 0 0 0 0 0 0 0
0 0 1 1 1 1 1 0 0 0 0 0 0 0 0 0
0 0 1 1 1 1 1 0 0 0 0 1 1 1 0 0
0 0 1 1 1 1 0 0 0 0 1 1 1 1 0 0
0 0 0 1 1 0 0 0 0 1 1 1 1 1 0 0
0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 1 1 1 0 0 0 0 0 0 0 0 0 0
0 0 1 1 1 1 1 0 0 0 0 0 0 0 0 0
0 0 1 1 1 1 1 0 0 0 0 1 1 1 0 0
0 0 1 1 1 1 0 0 0 0 1 1 1 1 0 0
0 0 0 1 1 0 0 0 0 1 1 1 1 1 0 0
0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 1 1 1 1 1 0 0 0 0 0 0 0 0 0
0 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0
0 0 1 1 1 1 1 0 0 0 0 0 0 0 0 0
0 0 1 1 1 1 1 0 0 0 0 1 1 1 0 0
0 0 1 1 1 1 0 0 0 0 1 1 1 1 0 0
0 0 0 1 1 0 0 0 0 1 1 1 1 1 0 0
0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 1 1 1 0 0 0 0 0 0 0 0 0 0
0 0 1 1 1 1 1 0 0 0 0 0 0 0 0 0
0 0 1 1 1 1 1 0 0 0 0 1 1 1 0 0
0 0 1 1 1 1 0 0 0 0 1 1 1 1 0 0
0 0 0 1 1 0 0 0 0 1 1 1 1 1 0 0
0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 1 1 1 1 1 0 0 0 0 0 0 0 0 0
0 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0
0 1 1 1 1 1 1 1 0 0 1 1 1 1 0 0
0 0 1 1 1 1 1 0 0 0 0 1 1 1 0 0
0 0 1 1 1 1 0 0 0 0 1 1 1 1 0 0
0 0 0 1 1 0 0 0 0 1 1 1 1 1 0 0
0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 1 1 1 0 0 0 0 0 0 0 0 0 0
0 0 1 1 1 1 1 0 0 0 0 0 0 0 0 0
0 0 1 1 1 1 1 0 0 0 0 1 1 1 0 0
0 0 1 1 1 1 0 0 0 0 1 1 1 1 0 0
0 0 0 1 1 0 0 0 0 1 1 1 1 1 0 0
0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 1 1 1 1 1 0 0 0 0 0 0 0 0 0
0 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0
0 1 1 1 1 1 1 1 0 0 1 1 1 1 0 0
0 1 1 1 1 1 1 1 0 1 1 1 1 1 1 0
0 0 1 1 1 1 0 0 0 0 1 1 1 1 0 0
0 0 0 1 1 0 0 0 0 1 1 1 1 1 0 0
0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 1 1 1 0 0 0 0 0 0 0 0 0 0
0 0 1 1 1 1 1 0 0 0 0 0 0 0 0 0
0 0 1 1 1 1 1 0 0 0 0 1 1 1 0 0
0 0 1 1 1 1 0 0 0 0 1 1 1 1 0 0
0 0 0 1 1 0 0 0 0 1 1 1 1 1 0 0
0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 1 1 1 1 1 0 0 0 0 0 0 0 0 0
0 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0
0 1 1 1 1 1 1 1 0 0 1 1 1 1 0 0
0 1 1 1 1 1 1 1 0 1 1 1 1 1 1 0
0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0
0 0 0 1 1 0 0 0 0 1 1 1 1 1 0 0
0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 1 1 1 0 0 0 0 0 0 0 0 0 0
0 0 1 1 1 1 1 0 0 0 0 0 0 0 0 0
0 0 1 1 1 1 1 0 0 0 0 1 1 1 0 0
0 0 1 1 1 1 0 0 0 0 1 1 1 1 0 0
0 0 0 1 1 0 0 0 0 1 1 1 1 1 0 0
0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 1 1 1 1 1 0 0 0 0 0 0 0 0 0
0 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0
0 1 1 1 1 1 1 1 0 0 1 1 1 1 0 0
0 1 1 1 1 1 1 1 0 1 1 1 1 1 1 0
0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0
0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0
0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 1 1 1 0 0 0 0 0 0 0 0 0 0
0 0 1 1 1 1 1 0 0 0 0 0 0 0 0 0
0 0 1 1 1 1 1 0 0 0 0 1 1 1 0 0
0 0 1 1 1 1 0 0 0 0 1 1 1 1 0 0
0 0 0 1 1 0 0 0 0 1 1 1 1 1 0 0
0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 1 1 1 1 1 0 0 0 0 0 0 0 0 0
0 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0
0 1 1 1 1 1 1 1 0 0 1 1 1 1 1 0
0 1 1 1 1 1 1 1 0 1 1 1 1 1 1 0
0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0
0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0
0 0 1 1 1 1 0 1 1 1 1 1 1 1 1 0

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 1 1 1 0 0 0 0 0 0 0 0 0 0
0 0 1 1 1 1 1 0 0 0 0 0 0 0 0 0
0 0 1 1 1 1 1 0 0 0 0 1 1 1 0 0
0 0 1 1 1 1 0 0 0 0 1 1 1 1 0 0
0 0 0 1 1 0 0 0 0 1 1 1 1 1 0 0
0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 1 1 1 1 1 0 0 0 0 0 0 0 0 0
0 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0
0 1 1 1 1 1 1 1 0 0 1 1 1 1 1 0
0 1 1 1 1 1 1 1 0 1 1 1 1 1 1 0
0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0
0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0
0 0 1 1 1 1 0 1 1 1 1 1 1 1 1 0

Rules:
1) Use zero ( 0 ) padding for each side.
2) Place the Structuring element and get the result straightway
Using the neighbors and dilation rule.
3) Make sure you only update values for origin only.

0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 1 1 0 0 0
0 0 1 1 1 1 0 0
0 0 0 1 1 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 1 1 1 1 1 0 0 0 0 0 0 0 0 0
0 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0
0 1 1 1 1 1 1 1 0 0 1 1 1 1 1 0
0 1 1 1 1 1 1 1 0 1 1 1 1 1 1 0
0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0
0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0
0 0 1 1 1 1 0 1 1 1 1 1 1 1 1 0

Opening is so called because it can open up a gap between
objects connected by a thin bridge of pixels. Any regions that
have survived the erosion are restored to their original size by
the dilation:

Opening is an idempotent operation: once an image has been
opened, subsequent openings with the same structuring
element have no further effect on that image:

clc,
%close all;
clear all;
I = imread('D:\matlab_folder\2.jpg');
figure, imshow(I);
SE = strel('square',5);
J = imopen(I,SE);
figure, imshow(J);

clc,
%close all;
clear all;
I = imread('D:\matlab_folder\2.jpg');
figure, imshow(I);
SE = strel('square',5);
J = imerode(I,SE);
J = imdilate(J,SE);
figure, imshow(J);

The closing of an image f by a structuring element s (denoted
by f • s) is a dilation followed by an erosion:

clc,
%close all;
clear all;
I = imread('D:\matlab_folder\2.jpg');
figure, imshow(I);
SE = strel('square',5);
J = imclose(I,SE);
figure, imshow(J);

clc,
%close all;
clear all;
I = imread('D:\matlab_folder\2.jpg');
figure, imshow(I);
SE = strel('square',11);
J= imdilate(I,SE);
J = imerode(J,SE);
figure, imshow(J);

Morphological top-hat filtering performs on the grayscale or
binary image and returns a filtered image. Top-hat filtering
computes the morphological opening of the image and then
subtracts the result from the original image.

clc,
close all;
clear all;
I = imread('D:\matlab_folder\Dip1.png');
figure, imshow(I);
SE = strel('square',11);
J = imtophat(I,SE);
figure, imshow(J);

the
morphological
grayscale or binary image and returns a filtered image,
Bottom-hat filtering computes the morphological closing of
the image and then subtracts the original image from the
result.

clc,
close all;
clear all;
I = imread('D:\matlab_folder\Dip1.png');
figure, imshow(I);
SE = strel('square',5);
J = imbothat(I,SE);
figure, imshow(J);

• Image binarization applies often just one global threshold 
T for mapping a scalar image I into a binary image.

• The global threshold can
optimization strategy aiming at creating “large” 
connected regions and at reducing
small-sized regions, called artifacts

Transition intensity: to change (intensity) from an origin state to a destination state at time t.

Applications of image sharpening include electronic printing, medical imaging, industrial 
inspection and autonomous guidance in military systems.

The strength of the response of a derivational operator is proportional to the degree of intensity 
discontinuity of the image at the point at which the operator is applied.

Therefore, image differentiation enhances edges and other discontinuities (such as noise) and 
deemphasizes area which have slowly varying intensities.

Left – original Image
Right – Blurred Image
There will be a mask which will slide the original image and will result the blurred image (average value 
will be placed in the center pixel to obtain the result )

Left – original Image
Right – Blurred Image
There will be a mask which will slide the original image and will result the blurred image (average value 
will be placed in the center pixel to obtain the result )
After 4 iterations of 21 x 21 box filter the result will be right one

It highlights gray-level discontinuities in an image
It deemphasizes regions with slowing varying gray levels

𝜕2𝑓
𝜕𝑥2 = 𝑓 𝑥 + 1, 𝑦 + 𝑓 𝑥 − 1, 𝑦 − 2𝑓(𝑥, 𝑦)
𝜕2𝑓
𝜕𝑦2 = 𝑓 𝑥, 𝑦 + 1 + 𝑓 𝑥, 𝑦 − 1 − 2𝑓(𝑥, 𝑦)

= (8x0) + (5x1) + (4x0) + (0x1) + (6x-4) + (2x1) + (1x0) + (3x1) + (7x0)
= 0 + 5 + 0 + 0 -24 + 2 + 0 + 3 + 0
= - 14

Rule: will increase 1 in the center point (e.g.; if -4 then it will be -5, if +4 then it will be +5 )


## Additional content from DIP_Lectures.txt

 To tell you what you can do with digital

 To show you that doing research in image

 To show you that you can solve typical image

 A visual representation of something captured

 Pixel values typically represent gray levels,

 Digital image is an approximation of a real

 3 samples per point (Red, Green, and Blue)

 4 samples per point (Red, Green, Blue, and

 The smallest individual element in an image

 In digital imaging a pixel, pel, or picture

accurate representations of the original.

 The intensity of each pixel is variable.

typically represented by three or
component intensities such as

For 4 colors:
cyan, magenta, yellow, and black.

 dots per inch (dpi) and
 pixels per inch (ppi)

1 bpp, 21 = 2 colors (monochrome)
2 bpp, 22 = 4 colors
3 bpp, 23 = 8 colors

2x -> Here x means color depths per pixel.

Highcolor: usually meaning 16 bpp,
normally has

a) Five bits for red and blue each, and
b) Six bits for green,

A 24-bit depth allows 8 bits per component.

The term is used not only for the number
of pixels in an image but also

 Improvement of pictorial information for

 Processing of
transmission
autonomous machine perception.

 What is the input for image processing or

 What is the output of image processing or

 Averaging (adding) multiple images can reduce

 Processing of digital images using digital devices

 DIP is not limited to image retrieval (IR)

o Watermarking and registration
Image compression

o Biometric application: face, iris, finger print,

 Automatic scanning and detection: X-ray,

• Environmental monitoring and remote sensing

An image can be defined as
 a two-dimensional function, f(x,y),

a) x and y are spatial (plane) coordinates
f
b)
coordinates (x,y)

is called the intensity of the image at that point.

are
elements, image elements, pels and pixels.

 Pixel is the term most widely used to denote the

The electromagnetic spectrum is the term used

by scientists to describe the entire range of light

From radio waves to gamma rays, most of the

light in the universe is, in fact, invisible to us!

 The only attribute of monochromatic light

intensity. (can be referred to as brightness)

 The intensity of monochromatic light is perceived

to vary from black to grays and finally to white.

 The term gray level is used to commonly denote

 The range of measured values of monochromatic

light from black to white is usually called the gray

 Chromatic light spans the electromagnetic energy

spectrum from approximately 0.43 to 0.79 µm

• A location (x, y): picture element, pixel, pel, etc

• A value f(x, y) at pixel (x, y): gray scale value

f(x, y) represents intensity which is proportional

1. Sampling : Digitizing the coordinates values is

2. Quantization : Digitizing the amplitude values

To sample this function,
we take equally spaced
samples along line AB

The values of the samples
continuous
a
still
range of intensity values

Intensity scale is divided
discrete
into
intervals.

Each element of this matrix
is called pixel or pel

 Number of Rows (M) and Columns (N) can be any integer

o Number of gray levels, L,  is usually power of 2:

 The number of bits required to store a digitized image :

 Suppose, you want to create an image of

size 1024 × 512 having 72 distinct intensity

values.What will be the size of the image?

 Interpolation is the process of using known data

Defined as the pixels at (x+1, y), (x-1, y), (x, y+1),

Defined as the pixels at (x+1, y+1), (x+1, y-1), (x-

Defined as the pixels at (x+1, y), (x-1, y), (x, y+1),

(x, y-1),(x+1, y+1), (x+1, y-1), (x-1, y+1), (x-1, y-1)

Adjacent pixels must be neighbors and have gray
values from the same set, V

Adjacent pixels must be neighbors and have gray

Can not be adjacent
if both values are
not present in V

o q in N4(p), or
o q in ND(p) and N4 (p) ∩ N4 (q) has no pixel

Intensity Transformations 
and Spatial Filtering

 Enhancement is the process of manipulating an

image so that the result is more suitable than the

 Enhancement in spatial domain (Chapter 3)

Spatial domain is a plane where a digital image is

defined by the spatial coordinates of its pixels.

 Enhancement in frequency domain (Chapter 4)

Frequency domain where a digital image is defined

by its decomposition into spatial frequencies

• The section of the real plane spanned by the

coordinates of an image is called the spatial

 The spatial domain processes can be denoted by

 f(x, y) is the input image and g(x, y) is the output

image and T is an operator defined over a

 Neighborhood can be as small as a single pixel

 Neighborhood (sub-image) rolls over the entire image,

 Neighborhood (sub-image) rolls over the entire image,

 Neighborhood (sub-image) rolls over the entire image,

 Neighborhood (sub-image) rolls over the entire image,

 Neighborhood (sub-image) rolls over the entire image,

 Neighborhood (sub-image) rolls over the entire image,

 Neighborhood (sub-image) rolls over the entire image,

 This procedure is called Spatial Filtering.

 The neighborhood along with a predefined

kernel, template or window. Spatial mask is the

 If the neighborhood is of size 1 × 1, g depends

only on the value of f at a single point (x, y) and T

 The four higher order bit, especially the last two, contain

a significant amount of visually significant data.

 The lower-order planes contribute to more subtle

Some of the bit plane sliced 
images have black border.

Look at this gray border. 
Its decimal value is 194

Some of the bit plane sliced 
images have white border.

 Useful for analyzing the relative importance of

 This process aids in determining the adequacy of

the number of bits used to quantize the image.

9  8  9  8
2  7  4  7
6  4  6  1
4  0  7  4
An image

0     1      2      3    4      5     6     7     8     9
2
1

9  8  9  8
2  7  4  7
6  4  6  1
4  0  7  4
An image

0       1       2      3      4       5       6       7      8       9

 Normalized histogram is more like probabilities

 p(rk): how likely a pixel will have gray level rk

9  8  9  8
2  7  4  7
6  4  6  1
4  0  7  4
An image

0       1       2      3      4       5       6       7      8       9

 An image whose pixels tend to occupy the entire

range of possible intensity level, will have an

 histogram(S,'Normalization','probability')

• Let s, r: are all discrete and in [0, L-1]

• Let, 2 conditions hold:
• T(r): single valued and monotonous in

• Let s, r: are all discrete and in [0, L-1]

• Let, 2 conditions hold:
• T(r): single valued and monotonous in

• Objective: to find the transformed image so that ps(s) of

 The previous method was global because pixels

are modified by a transformation function based

on the intensity distribution of an entire image.

 In some cases, it is necessary to enhance details

functions based on the intensity distribution in a

neighborhood of every pixel in the image.

 Define a neighborhood and move its center from

 At each location, the histogram of the points in

 Global histogram equalization increases noise

 Local histogram equalization provides more fine

details than global histogram equalization

 The intensity values of the objects were too close

to the intensity of the large squares and their

 Neighborhood (sub-image) rolls over the entire image,

 This procedure is called Spatial Filtering.

 The neighborhood along with a predefined

kernel, template or window. Spatial mask is the

 Filtering creates a new pixel with coordinates

neighborhood and whose value is the result of

If the operation performed on the image pixels is

linear, then the filter is called a linear spatial

If the operation performed on the image pixels is

non-linear, then the filter is called a non-linear

 A mask or filter or template or kernel or window

Mask Coefficients 
showing coordinate 
arrangement

Mask Coefficients showing 
coordinate arrangement

Mask Coefficients showing 
coordinate arrangement

Mask Coefficients showing 
coordinate arrangement

Now, Convolute 0 0 0 1 0 0 0 0 by 1 2 3 2 8

Apply the mask and calculate the first row

 When the mask moves closer to the border

– Closer to that distance: some rows/columns of the

• finding large objects, ignoring small details

 The output of a smoothing linear spatial filter is

clc;
clear all;
close all;
I = imread('cameraman.tif');
figure, imshow(I);

 Circle: 25 pixels, gray: 0, 20, ..., 100%

 For certain type of random noise, they provide excellent

 Particularly effective in the presence of impulse noise,

– Sort the values of enclosed pixels
– Select the median as output pixel level

– Sorted values: 10, 15, 20, 20, 20, 20, 20,

– Median is 20
– Output pixel value is 20

 Very useful for highlighting fine details

derivative proportional
image discontinuity

 Sharp changes noise point,
edges, lines, grey ramp are
easily detected

 1st and 2nd order derivatives will be used

• At onset and end of discontinuities (ramp

•
• Nonzero at onset of step and ramp
• Nonzero along ramp

•
• Nonzero at onset and end of step and ramp

Some operations test whether the element "fits"
within the neighborhood, while

3) Structuring element neither fits nor hits the image

The matrix dimensions specify the size of the 
structuring element.

The pattern of ones and zeros specifies the shape of 
the structuring element.

How to Calculate the Origin of a Structuring Element

Equation can be written as:
origin = floor((size+1)/2)

Lets say structuring element mask size is 3 x 3

Base on the equation;
Origin = floor((3+1)/2) = 2

The position will be (2,2) if initial
Position is considered as (1,1)

Structuring elements contains different shapes…

erosion
and
Dilation
morphological operations.

repeating for all pixel coordinates (x,y).

1) Fully match  1
2) Some match  0
3) No match  0

Let’s solve this for Erosion using 3 x 3 square Structuring element

1) Fully match  1
2) Some match  1
3) No match  0

Let’s try this with 3 x 3 matrix for Dilation

The opening of an image f
element s (denoted by f
a dilation:

by a structuring
s) is an erosion followed by

There can be two types of morphological filtering
possible which are:

to partition an image into a collection of set of pixels

Definition: Image segmentation partitions an image into

 Segmentation partitions an image into distinct

regions containing each pixels with similar

 To be meaningful and useful for image analysis

relate to depicted objects or features of interest.

 Meaningful segmentation is the first step from

greyscale or color image into one or more other

images to high-level image description in terms of

features, objects, and scenes. The success of

segmentation, but an accurate partitioning of an

image is generally a very challenging problem

Image binarization applies often just
threshold T for
a binary

the
given image I
providing
sense that
two
background
by

histogram
input
and
threshold
“overlap”
of
minimized
balance).

The principal objective of sharpening is to highlight transitions of intensity.

• Blurring – Pixel averaging
• Sharpening – spatial differentiation

1) First-order derivatives of a one-dimensional function

2) Second-order derivative of a one-dimensional function

Previously we had 1 dimensional now we will consider 2 dimensional

= [𝑓 𝑥 + 1, 𝑦 + 𝑓 𝑥 − 1, 𝑦 − 2𝑓(𝑥, 𝑦)] + 
[𝑓 𝑥, 𝑦 + 1 + 𝑓 𝑥, 𝑦 − 1 − 2𝑓(𝑥, 𝑦)]

= 𝑓 𝑥 + 1, 𝑦 + 𝑓 𝑥 − 1, 𝑦 + 𝑓 𝑥, 𝑦 + 1 + 𝑓 𝑥, 𝑦 − 1 - 4𝑓(𝑥, 𝑦)

