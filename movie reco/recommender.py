
import numpy as np
import pandas as pd
from scipy.sparse import hstack
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

IMAGE_BASE = "https://image.tmdb.org/t/p/"   # TMDB's free image server


def _tokens(cell):
    
    parts = [p.strip().lower().replace(" ", "_") for p in str(cell).split(",")]
    return " ".join(p for p in parts if p)


class Recommender:
    def __init__(self, csv_path):
        #  load the dataset
        self.movies = pd.read_csv(csv_path).fillna("")
        self.movies["id"] = self.movies["id"].astype(int)
        self.movies["genres"] = self.movies["genres"].astype(str)

       
        tags = (
            (self.movies["genres"].map(_tokens) + " ") * 2
            + (self.movies["production_companies"].map(_tokens) + " ") * 2
            + self.movies["keywords"].map(_tokens)
        )

       
        tag_matrix = TfidfVectorizer(token_pattern=r"\S+").fit_transform(tags)

  
        story_matrix = TfidfVectorizer(
            stop_words="english", max_features=20000, min_df=2
        ).fit_transform(self.movies["overview"])

        
        self.matrix = hstack([tag_matrix * 1.0, story_matrix * 0.7]).tocsr()

        
        self.row_of = {mid: i for i, mid in enumerate(self.movies["id"])}
        self.titles_lower = self.movies["title"].str.lower().tolist()

    

    @staticmethod
    def _to_dict(row):
        """Convert one movie row into a small dict for the web pages."""
        return {
            "id": int(row["id"]),
            "title": row["title"],
            "year": int(row["year"]) or "",
            "genres": row["genres"],
            "rating": round(float(row["vote_average"]), 1),
            "overview": row["overview"],
            "poster": IMAGE_BASE + "w342" + row["poster_path"],
            "backdrop": (IMAGE_BASE + "w780" + row["backdrop_path"])
                        if row["backdrop_path"] else "",
        }

    

    def popular(self, limit=30):
        """Most voted movies (file is already sorted by votes)."""
        return [self._to_dict(r) for _, r in self.movies.head(limit).iterrows()]

    def search(self, query, limit=30):
        """Movies whose title contains the typed text (most popular first)."""
        q = query.strip().lower()
        if not q:
            return self.popular(limit)
        hits = [i for i, t in enumerate(self.titles_lower) if q in t][:limit]
        return [self._to_dict(self.movies.iloc[i]) for i in hits]

    def get_movies_by_ids(self, ids):
        """Return the movies with the given ids."""
        rows = self.movies[self.movies["id"].isin(ids)]
        return [self._to_dict(r) for _, r in rows.iterrows()]

    def recommend(self, selected_ids, top_n=20):
        """
        Given the ids of ALL movies the user picked (1 or more), return the
        top_n most similar movies (excluding the ones already picked).
        """
        rows = [self.row_of[i] for i in selected_ids if i in self.row_of]
        if not rows:
            return []

        
        profile = np.asarray(self.matrix[rows].mean(axis=0))

        # Step 5: similarity of every movie to that profile (0 to 1)
        scores = cosine_similarity(profile, self.matrix).flatten()

        results = []
        for idx in scores.argsort()[::-1]:        
            movie = self.movies.iloc[idx]
            if int(movie["id"]) in selected_ids:
                continue                          
            item = self._to_dict(movie)
            item["score"] = min(99, round(float(scores[idx]) * 100 * 2))
            item["reason"] = self._reason(movie, rows)
            results.append(item)
            if len(results) == top_n:
                break
        return results

    def recommend_by_filters(self, genres=None, year_from=None, year_to=None,
                             min_rating=None, keyword=None, top_n=24):
   
        
        df = self.movies.copy()

        # ---- Genre filter
        if genres:
            genres_clean = [g.strip() for g in genres if g.strip()]
            if genres_clean:
                pattern = "|".join(genres_clean)   # regex OR
                df = df[df["genres"].str.contains(pattern, case=False, na=False, regex=True)]

        # ---- Year range ----
        if year_from:
            try:
                df = df[df["year"] >= int(year_from)]
            except (ValueError, TypeError):
                pass

        if year_to:
            try:
                df = df[df["year"] <= int(year_to)]
            except (ValueError, TypeError):
                pass

        # ---- Minimum rating ----
        if min_rating:
            try:
                df = df[df["vote_average"] >= float(min_rating)]
            except (ValueError, TypeError):
                pass

        # ---- Keyword: -
        if keyword and keyword.strip():
            kw = keyword.strip().lower()
            title_match   = df["title"].str.lower().str.contains(kw, na=False, regex=False)
            overview_match = df["overview"].str.lower().str.contains(kw, na=False, regex=False)
            df = df[title_match | overview_match]

     
        df = df.sort_values("vote_count", ascending=False).head(top_n)

        results = []
        for _, row in df.iterrows():
            item = self._to_dict(row)
            # Compute a simple relevance score (0-99) based on normalised rating
            raw_score = float(row["vote_average"]) / 10.0   # 0.0 – 1.0
            item["score"] = min(99, round(raw_score * 99))
            item["reason"] = self._filter_reason(row, genres, keyword)
            results.append(item)

        return results

    def _filter_reason(self, movie, genres, keyword):
       
        parts = []
        if genres:
            matched = [g for g in genres
                       if g.lower() in str(movie["genres"]).lower()]
            if matched:
                parts.append(", ".join(matched[:2]) + " genre")
        if keyword and keyword.strip():
            parts.append(f'keyword "{keyword.strip()}"')
        return "Matches: " + " · ".join(parts) if parts else "Highly rated & popular"

    def _reason(self, movie, selected_rows):
        
        picked = self.movies.iloc[selected_rows]

        def shared(column):
            
            mine = [x.strip() for x in str(movie[column]).split(",") if x.strip()]
            theirs = {x.strip() for c in picked[column] for x in str(c).split(",")}
            return [x for x in mine if x in theirs]

        parts = []
        if shared("production_companies"):
            parts.append(shared("production_companies")[0])
        if shared("genres"):
            parts.append(", ".join(shared("genres")[:2]))
        if shared("keywords"):
            parts.append(", ".join(shared("keywords")[:2]))
        return "Because you like: " + " · ".join(parts) if parts else "Similar overall style"
