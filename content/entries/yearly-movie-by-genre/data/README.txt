# Movie genre counts by year (1950–2025)

Counts of films per genre per year, derived from Wikidata.

**Source:** Wikidata (https://www.wikidata.org), queried via SPARQL.  
**License:** CC0 1.0 (public domain) — free to host, redistribute, and modify, no attribution required.  
**Scope:** films (`wd:Q11424`) with a publication date (`P577`) and a genre (`P136`), counting distinct films per genre per year.

## Files

- One CSV per genre (e.g. `drama.csv`), columns `year,count`, with every year 1950–2025 present (zeros where no films).
- `all_genres_long.csv` — `genre,year,count`.
- `all_genres_wide.csv` — `year` plus one column per genre.
- `query.sparql` — the exact query used to produce the counts.

## Genre mapping

Each broad genre maps to a single canonical Wikidata genre label, with no sub-genre merging; a film is counted once per genre it is tagged with.

| Display name | Wikidata label | Total films 1950–2025 | File |
|---|---|---:|---|
| Drama | `drama film` | 68,200 | `drama.csv` |
| Comedy | `comedy film` | 32,326 | `comedy.csv` |
| Documentary | `documentary film` | 32,756 | `documentary.csv` |
| Action | `action film` | 12,482 | `action.csv` |
| Thriller | `thriller film` | 10,477 | `thriller.csv` |
| Horror | `horror film` | 10,094 | `horror.csv` |
| Crime | `crime film` | 8,601 | `crime.csv` |
| Romance | `romance film` | 9,063 | `romance.csv` |
| Adventure | `adventure film` | 5,764 | `adventure.csv` |
| Science Fiction | `science fiction film` | 4,809 | `science_fiction.csv` |
| Biography | `biographical film` | 4,874 | `biography.csv` |
| Fantasy | `fantasy film` | 4,121 | `fantasy.csv` |
| Musical | `musical film` | 4,578 | `musical.csv` |
| War | `war film` | 3,703 | `war.csv` |
| Mystery | `mystery film` | 2,629 | `mystery.csv` |
| History | `historical film` | 2,815 | `history.csv` |
| Western | `Western film` | 2,242 | `western.csv` |
| Family | `family film` | 1,937 | `family.csv` |

## Adult and exploitation films

Films whose Wikidata genres include adult or exploitation categories are excluded from these counts. Wikidata catalogues such films in large numbers and frequently cross-tags them into mainstream genres (drama, comedy, action, crime), where they would otherwise distort the per-genre yearly counts. A film is dropped if it carries adult-related genres. See the sparql query below.

## Notes on coverage

- Counts are conservative; Wikidata catalogues a subset of all films released, with thinner coverage of recent low-budget and international titles.
- The most recent years (about 2024–2025) are still being added to Wikidata and read artificially low.
- The dip around 2020 reflects the COVID-19 production slowdown.


## How the data was compiled
The counts come from a single [SPARQL](https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service) query against Wikidata: every film (`wd:Q11424`) with a publication date (`P577`) and a genre (`P136`), counted per genre and year. Films carrying an adult or exploitation genre are excluded, since Wikidata cross-tags many of them into mainstream genres. Data was accessed at [https://qlever.dev/wikidata/qlSpkJ#csv](https://qlever.dev/wikidata/qlSpkJ#csv) on June, 2026

```sparql
PREFIX wd:   <http://www.wikidata.org/entity/>
PREFIX wdt:  <http://www.wikidata.org/prop/direct/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?label ?year (COUNT(DISTINCT ?film) AS ?count) WHERE {
  ?film  wdt:P31  wd:Q11424 ;
         wdt:P577 ?date ;
         wdt:P136 ?genre .
  ?genre rdfs:label ?label .
  FILTER(LANG(?label) = "en")
  BIND(YEAR(?date) AS ?year)
  FILTER(?year >= 1950 && ?year <= 2025)
  MINUS {
    ?film wdt:P136 ?bad .
    ?bad rdfs:label ?badlabel .
    VALUES ?badlabel {
      "erotic film"@en "pornographic film"@en "sex film"@en "exploitation film"@en
      "sexploitation film"@en "erotic thriller"@en "erotic thriller film"@en
      "blaxploitation film"@en "pink film"@en "pornographic parody film"@en
      "Bavarian porn"@en "softcore pornography"@en "lesbian pornographic film"@en
      "gay pornographic film"@en "Nazi exploitation"@en "erotic drama film"@en
      "erotica"@en "gonzo pornography"@en "comedy porn film"@en "MILF pornography"@en
    }
  }
}
GROUP BY ?label ?year
ORDER BY ?label ?year
```
You can run it yourself and export the result as CSV. The official endpoint at [query.wikidata.org](https://query.wikidata.org) times out on this whole-database aggregation, so use the faster [QLever](https://qlever.cs.uni-freiburg.de/wikidata) mirror of Wikidata for the full pull (or query one genre at a time on the official endpoint). 