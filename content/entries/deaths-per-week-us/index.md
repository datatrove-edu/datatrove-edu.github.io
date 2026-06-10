---
title: "Deaths per week in the US by cause"
date: 2026-02-25
type: "entry"
# banner: "TucsonHeat.jpg" 
# banner_ref: "Picture from [Wikipedia](https://commons.wikimedia.org/wiki/File:Saguaro_Sunset.jpg), CC-BY 3.0" 
functions: ["trigonometric"]
topics: ["public health"]
tags: ["cancer", "heart disease"]
---

The historical data of deaths per week of the year are sinusoidal for many causes of death. They vary by season with peaks in winter and troughs in summer. 
<!--more-->
For heart disease, the periodic variation apparently is a combination of stress, overeating/drinking, extra exertion (like shovelling snow) - all apparently equates to more heart attacks.


These are heart-related weekly deaths in the US:
{{< figure src="weekly_deaths_heart_US.png" width="700px" caption="Heart disease deaths per week in the US" >}}

And cancer related deaths in the US:
{{< figure src="weekly_deaths_cancer_US.png" width="700px" caption="Cancer disease deaths per week in the US" >}}

And aggregate weekly deaths in the US, from all causes:
{{< figure src="weekly_deaths_US.png" width="700px" caption="Deaths per week in the US" >}}


**Note:** The drop at the far end is expected and comes from reporting delays. 


There is a periodic component and a mild growth trend which may be due to population growth. Thuse, one could think about modelling these as purely periodic, or adding a linear or exponential term.

For example, a possible model for weekly heart-related deaths in the US is shown below

{{< figure src="plot_heart_exp_sine_shared_growth_fixedE_drop8_Bpos_Cgt1.png" width="700px" caption="Heart disease deaths per week in the US together with sine + trend model" >}}

Interestingly, it seems that the COVID "noise" makes the sinusoidal fit not have period 365 days. If you tell the LLM to ignore the covid data for the fit, it does give period 1 year. Here is a graph summarizing this:

{{< figure src="weekly_deaths_covid_period.png" width="700px" caption="Sine fit for deaths per week in the US with and without Covid data" >}}


For a plot with other causes of death, see the [Scientific American Article](https://www.scientificamerican.com/article/covid-is-on-track-to-become-the-u-s-s-leading-cause-of-death-yet-again1/), or the graph below created form the raw data:

{{< figure src="weekly_deaths_by_cause_US.png" width="700px" caption="Deaths by cause" >}}



## Cleaned up data
All the data comes from *National Center for Health Statistics. Weekly Counts of Death by Jurisdiction and Select Causes of Death, date accessed [26 Feb 2026]*, available from https://data.cdc.gov/d/u6jv-9ijr.

*  [US data for heart related or cancer deaths only](us_weekly_cancer_and_heart_data_only.csv). Built from the raw CDC data (link below in the "Sources" section). This is the data that was used for the plots above. It combines "Heart failure" and "Ischemic heart disease" into one group (Heart) and relabels "Malignant neoplasms" into "Cancer". 
*  [US data for weekly deaths (aggregate of all causes)](us_weekly_all_causes_total_deaths.csv). Filtered and organized from the raw CDC data (link below in the "Sources" section).
*  [US data only](weekly_deaths_united_states_only.csv). Filtered and organized from the raw CDC data (link below in the "Sources" section). The raw data from the CDC in the sources gives weekly data for all states in a 80MB file, this is more manageable.


## Sources
*  Official source for the raw data: [CDC source of the data](https://data.cdc.gov/National-Center-for-Health-Statistics/Weekly-Counts-of-Death-by-Jurisdiction-and-Select-/u6jv-9ijr/about_data) (large 80MB csv file).
*  [Scientific American Article](https://www.scientificamerican.com/article/covid-is-on-track-to-become-the-u-s-s-leading-cause-of-death-yet-again1/) with a nice graph.
