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
*  [Data from 2020 to Sep 2025](imdb_movies_by_genre_1950_2024.csv) in csv form (ready to be used in a spreadsheet of with an LLM). Date accessed: 24 September 2025.
*  [Python script](exportScript.py) to export the data, and [link to the IMDB dataset](https://developer.imdb.com/non-commercial-datasets/) (the script needs file `title.basics.tsv.gz`).
*  [Jupyter notebook for 1980-2015 strech](MovieGenresExponentials1980-2015.ipynb) for everal genres that give a good fit.
    -  includes also graphs of each genre together with "Romance", which has the slowest growth rate of them all.
    -  also online [here](https://colab.research.google.com/drive/1QhEjEtdhUYwErJ7hDjYXdgk4W8iIdHqU#scrollTo=XwaoQvuzP3mO)



