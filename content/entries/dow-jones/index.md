---
title: "Dow Jones Industrial Average"
date: 2026-05-25
type: "entry"
# banner: "TucsonHeat.jpg" 
# banner_ref: "Picture from [Wikipedia](https://commons.wikimedia.org/wiki/File:Saguaro_Sunset.jpg), CC-BY 3.0" 
functions: ["Exponential"]
topics: ["Finance"]
tags: ["Stocks", "Investment"]
---

The Dow Jones Industrial Average has grown approximately exponential for many decades.
<!--more-->
An approximate fit for the period Jan 2018 to Dec 2025 is given by:
$$
\text{DJIA} = 23225e^{0.000331t} \quad\text{with $t$ in days since January 2018}
$$

{{< figure src="DJIAexponentialFit.png" width="700px" caption="Exponential fit to DJIA" >}}

This gives a doubling time of approximately 8 years.

There are also interesting discussions to be had about noticeable drops (Covid) and periods with high average rates of change (bear markets and crashes).


## Sources for the data
*  DJIA data is copyrighted *S&P Dow Jones Indices LLC* and cannot be redistributed without permission. It can be easily downloaded at the FRED (Federal Reserve Bank of St. Louis) website at [https://fred.stlouisfed.org/series/DJIA](https://fred.stlouisfed.org/series/DJIA)
<!-- *  [csv file](DJIA.csv) with historical data for Jan 2018 to Dec 2025. Data copyrighted *S&P Dow Jones Indices LLC, Dow Jones Industrial Average [DJIA], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/DJIA, May 28, 2026*. -->
