# DataTrove-edu

A site with interesting datasets for mathematics education (function family fits, smoothing, regression). A [MCWG](mcwg.github.io) site developed with Hugo (https://gohugo.io).

Live site: https://datatrove-edu.github.io/

## Prereqs
- Install Hugo (extended): https://gohugo.io/getting-started/installing/
- Python 3.10+ with PyYAML, only needed to run `scripts/update_taxonomy_reference.py`

## Content model
- Entries live in `content/entries/<entry-name>/` (one folder per entry, kebab-case names, e.g. `tucson-first-100f`).
- The main file describing the entry is `content/entries/<entry-name>/index.md`.
- Images and data files for the entry should be placed in the same `content/entries/<entry-name>/` folder.
- In `index.md`, use `<!--more-->` to separate the summary that shows up in the entry's card from the rest of the content.
- Run `hugo new entries/<entry-name>/index.md` to scaffold a new entry from `archetypes/entries.md`, which includes markdown tips and notes on linking standalone HTML files.

## Creating a new entry
1. Run `hugo new entries/<entry-name>/index.md` (kebab-case name) to scaffold the entry from `archetypes/entries.md`.
2. Fill in the frontmatter: `title`, `date`, `tags`, `topics`, `functions`, `math_topics` and `summary`. See the "Tags, topics, functions, math_topics" section below for reusing existing values.
3. Add any images and data files into `content/entries/<entry-name>/` and reference them with relative links/`{{< figure >}}` shortcodes.
4. Write the summary above `<!--more-->` and the rest of the entry below it.
5. Note the data source, its license/attribution, and the date accessed (see "Linking to data sources" below).
6. Preview with `hugo server -D` before committing.

## Tags, topics, functions, math_topics
These are free-form taxonomies (`tags`, `topics`, `functions`, `math_topics` in the frontmatter) — there's no enforced allow-list. To help reuse existing values instead of creating near-duplicates, run:

```bash
python scripts/update_taxonomy_reference.py
```

This regenerates `data/allowed_tags.yaml`, `data/allowed_topics.yaml`, `data/allowed_functions.yaml` and `data/allowed_math_topics.yaml` — sorted reference lists of values currently in use across all entries. Run it after adding new tags so the lists stay current.

## Linking to data sources
When linking to an external data source, note the date the data was retrieved (e.g. "Date accessed: 5 June 2026"), since some sources are updated periodically.

If a data file is hosted in this repo (rather than just linked externally), reference its license/attribution in the entry (e.g. "CC BY-SA 4.0", "public domain", "CC0") and confirm the source's terms allow redistribution before adding the file.

## Linking to standalone HTML files
Hugo treats `.html` files placed inside an entry's content bundle as pages, not static files, so a normal markdown link to one will produce a 404 error. Instead:
1. Place the HTML file in `static/standalone/<entry-name>/`.
2. Link to it with an absolute path: `[See this html file](/standalone/<entry-name>/my-plots.html)`.

See `content/entries/death-cause-by-age/index.md` for a working example.

## View site locally
```bash
hugo server -D
```
Visit the `localhost` site you are given in the terminal.

## Build for deployment
```bash
hugo --minify
```
Output in `public/`

## Deployment
Pushing to `main` triggers `.github/workflows/build.yml`, which builds the site with Hugo and deploys it to GitHub Pages at https://datatrove-edu.github.io/.
