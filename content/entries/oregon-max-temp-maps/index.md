---
title: "Oregon max temperatures"
date: 2026-06-23
type: "entry"
banner: "banner_oregon_tmax_contour_10deg_i84.png" 
banner_ref: "Image generated with PRISM and TIGER data." 
math_topics: ["Optimization", "Contour plots"]  # See data/allowed_math_topics.yaml
topics: ["Temperature", "Heat map"]  # See data/allowed_topics.yaml
tags: ["Oregon", "Heat map"]  # See data/allowed_tags.yaml
---

The PRISM Climate Group publishes data on max temperatures throughout the US on every date. One can use it to draw heat maps for any state and date. 

<!--more-->

In particular, one can think about temperature changes as one drives along a highway. An example for Oregon and the I-84 is shown below.

{{< figure src="oregon_tmax_contour_10deg_i84_20250727.png" width="800px" caption="Temperatures in Oregon on July 27, 2025. Own creation with data from PRISM and the US Census Bureau (see source details notes below)." >}}



 
## Data and images.
*  [Max Temperatures throughout the US on July 27, 2025](prism_tmax_us_30s_20250727.tif) (tif file). Data from PRISM Climate Group, Oregon State University, https://prism.oregonstate.edu, created June 19, 2026. Freely reproduced and distributed with attribution to PRISM.
*  Geographical data for the Oregon border and the I-84 interstate from the US Census Bureau TIGER:
   *  [oregon.geojson](oregon.geojson): the Oregon state boundary, extracted from the [State Boundaries file](https://www2.census.gov/geo/tiger/TIGER2025/STATE/tl_2025_us_state.zip) (`tl_2025_us_state`).
   *  [i84.geojson](i84.geojson): the Interstate 84 route, extracted from the [Primary Roads national shapefile](https://www2.census.gov/geo/tiger/TIGER2025/PRIMARYROADS/tl_2025_us_primaryroads.zip) (`tl_2025_us_primaryroads`).


## Sources for the data
*  PRISM Climate Group, Oregon State University, https://prism.oregonstate.edu. 
*  US Census Bureau, Topologically Integrated Geographic Encoding and Referencing system (TIGER) 2025 data, at https://www2.census.gov/geo/tiger/TIGER2025

