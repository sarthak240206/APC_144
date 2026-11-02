
import os
import pandas as pd

RAW_FILE = "TMDB_movie_dataset_v11.csv"     
OUT_FILE = os.path.join("data", "movies.csv")
MIN_VOTES = 200                              

# Only read the columns we need (saves memory)
COLUMNS = ["id", "title", "release_date", "status", "adult", "vote_average",
           "vote_count", "runtime", "original_language", "overview",
           "poster_path", "backdrop_path", "genres", "production_companies",
           "keywords"]

df = pd.read_csv(RAW_FILE, usecols=COLUMNS)
print("Movies in raw file:", len(df))

df = df[(df["status"] == "Released") & (~df["adult"].astype(bool))
        & (df["vote_count"] >= MIN_VOTES)]
df = df.dropna(subset=["title", "poster_path", "overview", "genres"])


df["year"] = pd.to_datetime(df["release_date"], errors="coerce").dt.year.fillna(0).astype(int)


for col in ["production_companies", "keywords"]:
    df[col] = df[col].fillna("")

df = df.drop(columns=["status", "adult", "release_date"])
df = df.sort_values("vote_count", ascending=False)

os.makedirs("data", exist_ok=True)
df.to_csv(OUT_FILE, index=False)
print("Movies kept:", len(df), "->", OUT_FILE)
