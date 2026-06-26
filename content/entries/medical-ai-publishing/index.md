---
title: "AI medical publications double every 2 years"
date: 2026-06-26T09:40:19-05:00
# draft: true
type: "entry"
tags: ["Medical publishing"]         # See data/allowed_tags.yaml
topics: ["Public health"]       # See data/allowed_topics.yaml
functions: ["Exponential"]    # See data/allowed_functions.yaml
math_topics: ["Curve fitting"]  # See data/allowed_math_topics.yaml
---
AI-related medical publications on PubMed have grown roughly 35% per year since 2014, doubling approximately every 2 years.
<!--more-->

{{< figure src="pubmed_ai_publications.png" width="700px" caption="Number of AI-related publications by year according to PubMed together with exponential fit. Own creation with data linked below." >}}

## Data files
* [csv](PubMed_Timeline_Results_by_Year.csv): number of AI-related publications per year.  
  Data from [PubMed](https://pubmed.ncbi.nlm.nih.gov) (National Library of Medicine, US National Institutes of Health). Public domain. Accessed June 2026.


## How the data was obtained
Data was obtained by performing this [search](https://pubmed.ncbi.nlm.nih.gov/?term=%28artificial+intelligence%5Btiab%5D+OR+machine+learning%5Btiab%5D%29+AND+humans%5Bmesh%5D+AND+english%5Blang%5D) on [PubMed](https://pubmed.ncbi.nlm.nih.gov) (National Library of Medicine). 

The specific search term is:
```
(artificial intelligence[tiab] OR machine learning[tiab]) AND humans[mesh] AND english[lang]
```
Explanation of the search terms:
-  `[mesh]` refers to MeSH (Medical Subject Headings) which is the vocabulary that PubMed uses to tag and categorize articles. Adding `humans[mesh]` excludes things like:
    + Animal studies (mouse models, rat trials, etc.)
    + In vitro / lab studies
    + Pure computational/theoretical papers with no human data

-  `[tiab]` restricts the search to the title and abstract fields, so only papers that mention AI or machine learning in the title or abstract are included.




