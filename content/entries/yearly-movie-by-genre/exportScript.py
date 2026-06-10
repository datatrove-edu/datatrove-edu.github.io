"""
IMDb Movies by Genre Analysis Script
------------------------------------

This script processes the IMDb 'title.basics.tsv.gz' dataset to count the number
of movies released each year (1950–2024) across selected genres. Because the
IMDb dataset is very large, the script reads it in chunks to avoid memory issues.

The output is a CSV file ("imdb_movies_by_genre_1950_2020.csv") that contains
a table with years as rows and genres as columns. Each cell contains the count
of movies for that genre in the corresponding year.

Requirements:
- pandas library
- IMDb 'title.basics.tsv.gz' file (download from https://datasets.imdbws.com/)

Usage:
    python imdb_genre_counts.py
"""

import pandas as pd

# Path to the IMDb basics dataset (must be downloaded separately).
file_path = "title.basics.tsv.gz"

# List of movie genres we want to analyze.
genres_of_interest = [
    "Romance", "Sport", "Horror", "Comedy", "Action", "Adventure",
    "Sci-Fi", "Crime", "Drama", "Family", "Mystery", "Thriller",
    "War", "Western", "Musical", "Documentary", "Biography", "Animation", 
    "Fantasy", "History"
]

# Prepare a dictionary to hold yearly counts for each genre.
# Structure: { "Genre": {year: count, ...}, ... }
yearly_counts = {genre: {} for genre in genres_of_interest}

# IMDb files are huge; process the dataset in chunks to avoid memory overload.
chunksize = 500000
for chunk in pd.read_csv(file_path, sep="\t", compression="gzip", chunksize=chunksize, dtype=str):
    # Keep only rows that are movies (exclude TV shows, shorts, etc.).
    movies = chunk[chunk["titleType"] == "movie"]

    # Filter out invalid years (must be numeric).
    movies = movies[movies["startYear"].str.isnumeric()]
    movies["startYear"] = movies["startYear"].astype(int)

    # Restrict to movies released between 1950 and 2024.
    movies = movies[(movies["startYear"] >= 1950) & (movies["startYear"] <= 2024)]

    # For each genre of interest, count movies per year.
    for genre in genres_of_interest:
        # Find rows where the genre is listed in the "genres" column.
        mask = movies["genres"].str.contains(genre, na=False)

        # Count how many movies in that genre were released per year.
        counts = movies.loc[mask, "startYear"].value_counts().to_dict()

        # Accumulate counts into our yearly_counts dictionary.
        for year, count in counts.items():
            yearly_counts[genre][year] = yearly_counts[genre].get(year, 0) + count

# Convert the nested dictionary into a pandas DataFrame for easier analysis.
df = pd.DataFrame(yearly_counts).fillna(0).astype(int)

# Sort rows by year (index).
df = df.sort_index()

# Save the result to a CSV file.
df.to_csv("imdb_movies_by_genre_1950_2024.csv")

# Display confirmation and a preview of the data.
print("Done! Saved imdb_movies_by_genre_1950_2024.csv")
print(df.head(15))
