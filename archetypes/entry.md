---
title: "{{ replace .Name "-" " " | title }}"
date: {{ .Date }}
type: "entry"
tags: []         # See data/allowed_tags.yaml
topics: []       # See data/allowed_topics.yaml
functions: []    # See data/allowed_functions.yaml
math_topics: []  # See data/allowed_math_topics.yaml
summary: ""
---
Write the entry. Everything before the "more" comment gets displayed in the card.
<!--more-->
Everything after the "more" comment is only visible in the page for the entry.

To insert images, place the image in the same folder as the entry and use:

{{< figure src="my-image.png" width="700px" caption="Description of the image" >}}

## Markdown tips

*  Headings: start a line with `##` (or more `#`s for sub-sections), e.g. `## Data`.
*  Links: `[link text](https://example.com)` or, for a file in this same folder, `[data file](my-data.csv)`.
*  Bold/italic: `**bold**` and `*italic*`.
*  Lists: start lines with `*` or `-`.
*  Math: inline with `\( ... \)` or `$ ... $`, and display equations with `\[ ... \]` or `$$ ... $$`.

## Linking to a standalone HTML file

Hugo treats any `.html` file placed in this folder as a page, not a static
file, so a normal `[link](my-plots.html)` will give a "Page Not Found" error.
To link to a standalone HTML file (e.g. an exported Plotly/Jupyter HTML
report), instead:

1.  Put the HTML file in `static/standalone/<this-entry's-folder-name>/`.
2.  Link to it with an absolute path: `[See this html file](/standalone/<this-entry's-folder-name>/my-plots.html)`.

See `content/entries/death-cause-by-age/index.md` for a working example.
