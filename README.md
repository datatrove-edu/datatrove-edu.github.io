# DataTrove

A site with interesting datasets for mathematics eduction (function family fits, smoothing, regression). A [MCWG](mcwg.github.io) site developed with with Hugo[https://gohugo.io].

## Prereqs
- Install Hugo (extended): https://gohugo.io/getting-started/installing/
- Python 3.10+ (for the tag validator)

## Content model
-  Entries live in `content/entries/*` (one folder per entry, with no spaces in its name).
-  Main file describing the data entry is in `content/entries/<myExample>/index.md` where `<myExample>` is the name of the folder for the entry.
-  Images and data files for the entry should be placed in the same `content/entries/<myExample>/` folder. 
-  See existing `index.md` files for the structure of the entry files. For example, entry [tucsonFirst100F](content/entries/tucsonFirst100F/index.md)_
- In the `index.md`, Use `<!--more-->` to separate the summary which shows up in the info card for the entry from the rest of the content.

## Allowed tags
Edit `data/allowed-tags.yaml`. The CI step (and local script) will fail builds if a tag isn't in this list.

## View site locally
```bash
python -m pip install pyyaml
python scripts/validate_tags.py   # ensure tags are allowed
hugo server -D
```
Visit the `localhost` site you are given in the terminal.

## Build for deployment
```bash
python scripts/validate_tags.py
hugo -D
```
Output in `public/`


