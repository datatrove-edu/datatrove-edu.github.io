---
title: "Exponential growth of yearly movies"
date: 2026-06-14
type: "entry"
banner: "romance_horror_comedy_1950_2014_linear.png"
banner_ref: ""

functions: ["Exponential"]
math_topics: ["Curve fitting", "Modeling"]
# topics: ["data", "data fitting", "Modeling"]
tags: ["Movies"]
---

The number of films by genre grows roughly exponentially per year for many genres, with different rates per genre. 

<!--more-->

{{< figure src="romance_horror_comedy_1950_2014_linear.png" width="800px" caption="Yearly film count by genre for selected genres, 1950–2014, each with a fitted exponential. Source: Wikidata (CC0)." >}}

Corresponding log plots:

{{< figure src="romance_horror_comedy_1950_2014_log.png" width="800px" caption="Same data on a log scale — a true exponential plots as a straight line. Source: Wikidata (CC0)." >}}

The exponential fit is not equally good for every genre. There is a particular stretch from 1980 to 2014 in which several genres fit an exponential very well (examples include *Romance*, *Thriller* and *Documentary*) while others are nearly flat or too noisy to call exponential. 

## The data

All files below are derived from [Wikidata](https://www.wikidata.org), dedicated to the public domain under [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/),  so you may download, host, modify, and redistribute them freely. Films whose Wikidata genres include adult or exploitation categories are excluded from these counts. The data was accessed on June 2026. More information on how the data was obtained, filtered, and processed [here](data/README.txt).

The data groups movie counts into eighteen broad genres: drama, comedy, documentary, action, thriller, horror, crime, romance, adventure, science_fiction, biography, fantasy, musical, war, mystery, history, western, family.

* **Combined, wide** ([`all_genres_wide.csv`](data/all_genres_wide.csv)). One column per genre. 
* **Combined, long** ([`all_genres_long.csv`](data/all_genres_long.csv)). Three columns, `genre,year,count`.
* **Per-genre files** ([zip file](movie_genres_1950_2025.zip)) — one file per genre with two columns, `year,count`, covering every year 1950–2025. 



Our sincere thanks to the volunteers **Wikidata** editors and to the **Wikimedia Foundation** for maintaining a film catalogue in the public domain. CC0 asks for nothing in return — not even attribution — which is exactly what lets us post the data and the ready-to-use CSVs here. 

Note: IMDb's dataset would have been a natural source, but its [non-commercial license](https://developer.imdb.com/non-commercial-datasets/) forbids republishing the data "to create any kind of online/offline database of movie information." That means we cannot share IMDb-derived numbers at all. 



