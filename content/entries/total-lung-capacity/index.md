---
title: "Total Lung Capacity form CT scan"
date: 2026-05-14
type: "entry"
banner: "High-resolution_computed_tomograph_of_a_normal_thorax,_axial_plane_(53).jpg" 
banner_ref: "Image from Mikael Häggström, CC0, via [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:High-resolution_computed_tomograph_of_a_normal_thorax,_axial_plane_(53).jpg)" 

# functions: ["Numerical Integration"]
topics: ["Medical imaging"]
math_topics: ["Numerical Integration", "Riemann Sums", "Volume through Integration"]
tags: ["Lung", "CT scan"]
---

The total lung capacity is estimated by computing the areas of the lungs in different slices and adding them up as a Riemann Sum. 

<!--more-->

See a scrollable of all 100 images in the [wikimedia site](https://commons.wikimedia.org/wiki/Scrollable_high-resolution_computed_tomography_images_of_a_normal_thorax)


## Data

All the data below is adapted and constructed from CT-scan images available at [wikimedia](https://commons.wikimedia.org/wiki/Scrollable_high-resolution_computed_tomography_images_of_a_normal_thorax). Images by *Mikael Häggström, MD.*, CC0 1.0 Universal Public Domain Dedication. Date accessed: 14 May 2026.

**Note on scale for the images:** The original images have no exact scale data, but you can use an approximate scale of 0.287 mm/pixel,[^scale] so each pixel ≈ 0.287² = 0.0824 mm².

**Slice thickness:** The slice thickness of the images is 3 mm.

* [zip file](11LungCTSlices.zip) with 11 axial slices (every 10th slice of the series) for integration problems. Images are named by position (`thorax_axial_003.jpg` = slice 3).
* [lung_areas.csv](lung_areas.csv): lung cross-sectional area for all 106 slices.
Columns:

  - `position`: slice number, 1–106, head→foot
  - `lung_pixels`: number of pixels making up the lung cross-section
  - `lung_area_cm2`: total area in cm² (both lungs combined)
  - `n_lung_regions`: number of regions on the slice that make up the lung cross-section.



[^scale]: The JPEGs carry no pixel-spacing metadata, but each has a burned-in `FoV: 374 mm` annotation, and the reconstructed image spans 1303 pixels in the frame: 374 mm ÷ 1303 px ≈ 0.287 mm/pixel (an estimate, not exact).
