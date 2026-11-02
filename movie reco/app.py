
import os
from datetime import timedelta
from flask import (Flask, render_template, request, redirect,
                   url_for, session, jsonify, flash)
from recommender import Recommender
from watch_later import (get_user_id, get_watch_later,
                         add_to_watch_later, remove_from_watch_later,
                         is_in_watch_later)


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-change-me")
app.permanent_session_lifetime = timedelta(days=365)


recommender = Recommender("data/movies.csv")


ALL_GENRES = sorted({
    g.strip()
    for genres_cell in recommender.movies["genres"]
    for g in str(genres_cell).split(",")
    if g.strip()
})

YEAR_MIN = int(recommender.movies["year"].replace(0, recommender.movies["year"][recommender.movies["year"] > 0].min()).min())
YEAR_MAX = int(recommender.movies["year"].max())

PAGE_SIZE = 30          




def _paginate(movies_list, page):
    """Return one page slice of movies_list."""
    start = (page - 1) * PAGE_SIZE
    end   = start + PAGE_SIZE
    return movies_list[start:end]


def _apply_filters(movies_list, genres_sel, year_from, year_to, min_rating, keyword):
    
    kw = keyword.strip().lower() if keyword else ""

    filtered = []
    for m in movies_list:
        # -- Genre: at least one selected genre must appear in the movie's genres --
        if genres_sel:
            movie_genres = [g.strip() for g in str(m.get("genres", "")).split(",")]
            if not any(g in movie_genres for g in genres_sel):
                continue

        # -- Year lower bound --
        if year_from:
            try:
                if int(m.get("year") or 0) < int(year_from):
                    continue
            except (ValueError, TypeError):
                pass

        # -- Year upper bound --
        if year_to:
            try:
                if int(m.get("year") or 9999) > int(year_to):
                    continue
            except (ValueError, TypeError):
                pass

        # -- Minimum rating --
        if min_rating:
            try:
                if float(m.get("rating") or 0) < float(min_rating):
                    continue
            except (ValueError, TypeError):
                pass

        # -- Keyword in title or overview --
        if kw:
            in_title    = kw in str(m.get("title",    "")).lower()
            in_overview = kw in str(m.get("overview", "")).lower()
            if not in_title and not in_overview:
                continue

        filtered.append(m)

    return filtered


# ---------- Pages ----------

@app.route("/")
def home():
    
    get_user_id()                                   # ensure session ID exists
    page = int(request.args.get("page", 1))
    all_movies = recommender.popular(limit=len(recommender.movies))   # full list, popular-first
    total       = len(all_movies)
    movies      = _paginate(all_movies, page)
    has_more    = (page * PAGE_SIZE) < total

    return render_template(
        "home.html",
        movies=movies,
        page=page,
        has_more=has_more,
    )


@app.route("/api/browse")
def api_browse():
    
    get_user_id()
    page       = int(request.args.get("page", 1))
    all_movies = recommender.popular(limit=len(recommender.movies))
    movies     = _paginate(all_movies, page)
    has_more   = (page * PAGE_SIZE) < len(all_movies)
    return jsonify({"movies": movies, "has_more": has_more})


@app.route("/search")
def search_page():
   
    get_user_id()
    query   = request.args.get("q", "").strip()
    movies  = recommender.search(query, limit=60) if query else []
    return render_template("search.html", query=query, movies=movies)


@app.route("/movie/<int:movie_id>")
def movie_detail(movie_id):
    """Movie details page."""
    uid    = get_user_id()
    result = recommender.get_movies_by_ids([movie_id])
    if not result:
        flash("Movie not found.", "error")
        return redirect(url_for("home"))
    movie   = result[0]
    saved   = is_in_watch_later(uid, movie_id)
    return render_template("movie_detail.html", movie=movie, saved=saved)


# ---------- Recommendations ----------

@app.route("/recommend", methods=["GET", "POST"])
def recommend():
    
    
    get_user_id()

    if request.method == "POST":
        # ── Read movie selections (existing feature) ─────────────────────────
        raw_ids    = request.form.getlist("movie_ids")
        picked_ids = [int(i) for i in raw_ids if i.strip()]

        # ── Read preference filters ───────────────────────────────────────────
        genres_sel = request.form.getlist("genres")               # list[str]
        year_from  = request.form.get("year_from",  "").strip()
        year_to    = request.form.get("year_to",    "").strip()
        min_rating = request.form.get("min_rating", "").strip()
        keyword    = request.form.get("keyword",    "").strip()

        has_filters = bool(genres_sel or year_from or year_to or min_rating or keyword)

        # ── D: Nothing provided ───────────────────────────────────────────────
        if not picked_ids and not has_filters:
            flash(
                "Please select at least one movie or apply at least one filter "
                "(genre, year, rating, or keyword).",
                "error",
            )
            saved_picks = recommender.get_movies_by_ids(session.get("picked_ids", []))
            return render_template(
                "recommend_form.html",
                all_genres=ALL_GENRES,
                year_min=YEAR_MIN,
                year_max=YEAR_MAX,
                saved=saved_picks,
                # Restore filter field values so the form isn't wiped
                prev_genres=genres_sel,
                prev_year_from=year_from,
                prev_year_to=year_to,
                prev_min_rating=min_rating,
                prev_keyword=keyword,
            )

        # ── Persist new movie picks to session ────────────────────────────────
        if picked_ids:
            session.permanent = True
            session["picked_ids"] = picked_ids
        else:
            # No new picks in this POST – reuse whatever was saved before
            picked_ids = session.get("picked_ids", [])

        # ── Generate recommendations ──────────────────────────────────────────
        if picked_ids and has_filters:
            # Case B: content-based first, then filter the results
            # Use a larger top_n so filtering still leaves enough results
            base_recs = recommender.recommend(picked_ids, top_n=200)
            recs = _apply_filters(base_recs, genres_sel, year_from, year_to,
                                  min_rating, keyword)[:24]

        elif picked_ids:
            # Case A: pure content-based (existing algorithm, unchanged)
            recs = recommender.recommend(picked_ids, top_n=24)

        else:
            # Case C: filter-only – query the full 11 k-movie dataset directly
            recs = recommender.recommend_by_filters(
                genres=genres_sel,
                year_from=year_from,
                year_to=year_to,
                min_rating=min_rating,
                keyword=keyword,
                top_n=24,
            )

        picked = recommender.get_movies_by_ids(picked_ids)

        return render_template(
            "recommendations.html",
            picked=picked,
            recs=recs,
            genres_sel=genres_sel,
            year_from=year_from,
            year_to=year_to,
            min_rating=min_rating,
            keyword=keyword,
        )

    # ── GET: show the preference form ─────────────────────────────────────────
    saved_picks = recommender.get_movies_by_ids(session.get("picked_ids", []))
    return render_template(
        "recommend_form.html",
        all_genres=ALL_GENRES,
        year_min=YEAR_MIN,
        year_max=YEAR_MAX,
        saved=saved_picks,
        prev_genres=[],
        prev_year_from="",
        prev_year_to="",
        prev_min_rating="",
        prev_keyword="",
    )


# ---------- Original select route (kept for backward compatibility) ----------

@app.route("/select", methods=["GET", "POST"])
def select():
    """Original pick-movies page — still fully functional."""
    get_user_id()
    if request.method == "POST":
        ids = [int(i) for i in request.form.getlist("movie_ids")]
        if ids:
            session.permanent = True
            session["picked_ids"] = ids
            return redirect(url_for("recommend"))

    saved = recommender.get_movies_by_ids(session.get("picked_ids", []))
    return render_template("select.html", saved=saved)


@app.route("/api/search")
def api_search():
    """Live search used by the select page while typing."""
    return jsonify(recommender.search(request.args.get("q", "")))


@app.route("/reset")
def reset():
    """Clear picked movies and start over."""
    session.pop("picked_ids", None)
    return redirect(url_for("recommend"))


# ---------- Watch Later routes ----------

@app.route("/watch-later")
def watch_later():
    """Display the current visitor's Watch Later list."""
    uid    = get_user_id()
    ids    = get_watch_later(uid)
    movies = recommender.get_movies_by_ids(ids)
    return render_template("watch_later.html", movies=movies)


@app.route("/watch-later/add/<int:movie_id>", methods=["POST"])
def watch_later_add(movie_id):
    """Add a movie to Watch Later. Prevents duplicates."""
    uid  = get_user_id()
    added = add_to_watch_later(uid, movie_id)
    if added:
        flash("Added to Watch Later! 🎬", "success")
    else:
        flash("Already in your Watch Later list.", "info")
    # Go back to wherever the user came from
    return redirect(request.referrer or url_for("movie_detail", movie_id=movie_id))


@app.route("/watch-later/remove/<int:movie_id>", methods=["POST"])
def watch_later_remove(movie_id):
    """Remove a movie from Watch Later."""
    uid     = get_user_id()
    removed = remove_from_watch_later(uid, movie_id)
    if removed:
        flash("Removed from Watch Later.", "info")
    return redirect(request.referrer or url_for("watch_later"))


# ---------- Run ----------

if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("PORT", 5000)))
