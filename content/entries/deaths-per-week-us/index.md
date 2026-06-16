---
title: "Deaths per week in the US by cause"
date: 2026-02-25
type: "entry"
# banner: "TucsonHeat.jpg" 
# banner_ref: "Picture from [Wikipedia](https://commons.wikimedia.org/wiki/File:Saguaro_Sunset.jpg), CC-BY 3.0" 
functions: ["Trigonometric"]
topics: ["Public health"]
tags: ["Cancer", "Heart disease"]
---

The historical data of deaths per week of the year are sinusoidal for many causes of death. They vary by season with peaks in winter and troughs in summer. 
<!--more-->
For heart disease, the periodic variation apparently is a combination of stress, overeating/drinking, extra exertion (like shovelling snow) - all apparently equates to more heart attacks.


These are heart-related weekly deaths in the US:
{{< figure src="weekly_deaths_heart_US.png" width="700px" caption="Heart disease deaths per week in the US" >}}

And cancer related deaths in the US:
{{< figure src="weekly_deaths_cancer_US.png" width="700px" caption="Cancer disease deaths per week in the US" >}}

**Note:** The drop at the far end is expected and comes from reporting delays. 

Here are aggregate weekly deaths in the US, from all causes, which show a noticeable increase due to COVID-19 after 2020:
{{< figure src="weekly_deaths_US.png" width="700px" caption="Deaths per week in the US" >}}



There is a periodic component and a mild growth trend which may be due to population growth. Thus, one could think about modelling these as purely periodic, or adding a linear or exponential term.

For example, a possible model for weekly heart-related deaths in the US is shown below

{{< figure src="plot_heart_exp_sine_shared_growth_fixedE_drop8_Bpos_Cgt1.png" width="700px" caption="Heart disease deaths per week in the US together with sine + trend model" >}}

For a plot with other causes of death, see the [Scientific American Article](https://www.scientificamerican.com/article/covid-is-on-track-to-become-the-u-s-s-leading-cause-of-death-yet-again1/), or the graph below created from the raw data:

{{< figure src="weekly_deaths_by_cause_US.png" width="700px" caption="Deaths by cause" >}}



## Cleaned up data
The cause-specific data comes from *National Center for Health Statistics. Weekly Counts of Death by Jurisdiction and Select Causes of Death*, accessed on 26 Feb 2026, available from the CDC site https://data.cdc.gov/d/u6jv-9ijr. The aggregate all-cause weekly totals come from *National Center for Health Statistics. Excess Deaths Associated with COVID-19*, accessed on 16 Jun 2026, available from https://data.cdc.gov/d/xkkf-xrst.

*  [US data for weekly deaths (aggregate of all causes)](us_weekly_all_cause_deaths.csv). Filtered from the CDC "Excess Deaths Associated with COVID-19" dataset (see Sources). Weighted counts, which correct the most recent weeks for reporting delays and so drop the falling tail visible in the plots above. Raw counts are in the [unweighted version](us_weekly_all_cause_deaths_unweighted.csv).
*  [US data for heart related or cancer deaths only](us_weekly_cancer_and_heart_data_only.csv). Built from the raw CDC data; weighted counts that correct the most recent weeks for reporting delays. It combines "Heart failure" and "Ischemic heart disease" into one group (Heart) and relabels "Malignant neoplasms" into "Cancer". The plots above use the [unweighted version](us_weekly_cancer_and_heart_data_only_unweighted.csv), so they won't match this file at the right edge.
*  [US data only](weekly_deaths_united_states_only.csv). Filtered and organized from the raw CDC data. (The raw data gives weekly data for all states in large file, this is more manageable.)


## Sources
*  Official source for the all-cause raw data: [CDC "Excess Deaths Associated with COVID-19" dataset](https://data.cdc.gov/NCHS/Excess-Deaths-Associated-with-COVID-19/xkkf-xrst/about_data).
*  [Scientific American Article](https://www.scientificamerican.com/article/covid-is-on-track-to-become-the-u-s-s-leading-cause-of-death-yet-again1/) with a nice graph.
*  Official source for the cause-specific raw data: [CDC source of the data](https://data.cdc.gov/National-Center-for-Health-Statistics/Weekly-Counts-of-Death-by-Jurisdiction-and-Select-/u6jv-9ijr/about_data) (large 80MB csv file). **Warning:** this dataset only covers a handful of *select* causes of death (Alzheimer's, circulatory diseases, cancer, respiratory diseases, diabetes, renal failure, and sepsis) — it does **not** contain all causes of death, so its totals fall well short of true all-cause mortality.
