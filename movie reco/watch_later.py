
import json
import os
import uuid
from flask import session

STORAGE_DIR = os.path.join(os.path.dirname(__file__), "storage")
JSON_FILE   = os.path.join(STORAGE_DIR, "watch_later.json")



def get_user_id():
    """Return (and create if needed) a unique ID stored in the Flask session."""
    if "user_id" not in session:
        session["user_id"] = str(uuid.uuid4())
        session.permanent = True          # keep it for 1 year (like picked_ids)
    return session["user_id"]




def _ensure_file():
    
    os.makedirs(STORAGE_DIR, exist_ok=True)
    if not os.path.exists(JSON_FILE):
        _write_data({"users": {}})


def _read_data():
    
    _ensure_file()
    try:
        with open(JSON_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        if not isinstance(data, dict) or "users" not in data:
            data = {"users": {}}
        return data
    except (json.JSONDecodeError, OSError):
        return {"users": {}}


def _write_data(data):
    _ensure_file()
    try:
        with open(JSON_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
    except OSError as e:
        # Log but don't crash the app
        print(f"[watch_later] Failed to write JSON: {e}")


def get_watch_later(user_id):
    """Return a list of movie IDs saved by this user (integers)."""
    data = _read_data()
    user_entry = data["users"].get(user_id, {})
    return [int(m) for m in user_entry.get("movies", [])]


def add_to_watch_later(user_id, movie_id):
   
    movie_id = int(movie_id)
    data = _read_data()


    if user_id not in data["users"]:
        data["users"][user_id] = {"movies": []}

    movies = [int(m) for m in data["users"][user_id]["movies"]]

    if movie_id in movies:
        return False        

    movies.append(movie_id)
    data["users"][user_id]["movies"] = movies
    _write_data(data)
    return True


def remove_from_watch_later(user_id, movie_id):
   
    movie_id = int(movie_id)
    data = _read_data()

    if user_id not in data["users"]:
        return False

    movies = [int(m) for m in data["users"][user_id]["movies"]]

    if movie_id not in movies:
        return False

    movies.remove(movie_id)
    data["users"][user_id]["movies"] = movies
    _write_data(data)
    return True


def is_in_watch_later(user_id, movie_id):
   
    return int(movie_id) in get_watch_later(user_id)

