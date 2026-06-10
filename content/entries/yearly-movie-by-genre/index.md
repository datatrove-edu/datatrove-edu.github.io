---
title: "Yearly movies grows different for each genre"
date: 2025-09-19
type: "entry"
banner: "" 
banner_ref: "" 

functions: ["exponential"]
math_topics: ["data", "curve fitting", "modeling"]
# topics: ["data", "data fitting", "modeling"]
tags: ["movies"]
---

Number of yearly movies by genre growing exponentially for many genres, and rate is different for each genre.

<!--more-->

{{< figure src="plot.png" width="700px" caption="Made with Python from data extracted from the IMDB website" >}}


{{< figure src="logPlot.png" width="700px" caption="Log plot. Made with Python from data extracted from the IMDB website" >}}

Data from a very big IMDB database (1GB) that needs to be processed.

Note, exponential fit is not fantastic throughout for all genres, but there is a particular stretch from 1980 to 2015 in which several genres have very good exponential fits. This is explored in detail in the AI Precalculus LAB `lab-exponential.tex`. In that lab, we give a possible reason for this: 
>Beginning in the 1980s, worldwide movie production increased approximately exponentially, likely driven by exponential population growth and the home video revolution (VHS, DVDs, rental stores). This exponential trend continued into the early 2010s, after which it slowed, probably because of streaming platforms and the growing popularity of TV series and serialized content. Different genres displayed different exponential growth rates. 

## Used in
*  AI Precalc labs for exponential functions. This uses the 1980 to 2015 stretch.


## Resources
*  [Colab notebook for the 1980-2015 stretch](https://colab.research.google.com/drive/1QhEjEtdhUYwErJ7hDjYXdgk4W8iIdHqU#scrollTo=XwaoQvuzP3mO) — the recommended way to get the data and plots. The first cell downloads IMDb's dataset directly from [datasets.imdbws.com](https://datasets.imdbws.com/) and computes the genre counts itself, so just open it and "Run all" (no local Python install needed).
    -  includes graphs of each genre together with "Romance", which has the slowest growth rate of them all.
    -  also available as a [downloadable notebook](MovieGenresExponentials1980-2015.ipynb).
*  For local/offline use: [Python script](exportScript.py) that processes IMDb's `title.basics.tsv.gz` (download it yourself from [datasets.imdbws.com](https://developer.imdb.com/non-commercial-datasets/), per IMDb's non-commercial terms) into a yearly genre-count csv.



