import requests
import os

# Replace with your actual TMDb API key
TMDB_API_KEY = "YOUR_TMDB_API_KEY" 
MOVIE_ID = TMDB_MOVIE_ID

# Base URLs for TMDb API
BASE_URL = "https://api.themoviedb.org/3"
IMAGE_BASE_URL = "https://image.tmdb.org/t/p"

def get_movie_details():
    """Fetches movie details from the TMDb API."""

    movie_url = f"{BASE_URL}/movie/{MOVIE_ID}?api_key={TMDB_API_KEY}"
    credits_url = f"{BASE_URL}/movie/{MOVIE_ID}/credits?api_key={TMDB_API_KEY}"

    try:
        movie_response = requests.get(movie_url)
        movie_data = movie_response.json()

        credits_response = requests.get(credits_url)
        credits_data = credits_response.json()

        results = {
            "Name": movie_data.get("title"),
            "Tagline": movie_data.get("tagline"),
            "Genre": ", ".join([genre['name'] for genre in movie_data.get("genres", [])]),
            "Runtime": movie_data.get("runtime"),
            "Release Date": movie_data.get("release_date"),
            "Country Of Origin": ", ".join([country['name'] for country in movie_data.get("production_countries", [])]),
            "Language": movie_data.get("original_language"),
            "Rating": movie_data.get("vote_average"),
            "Movie Budget": movie_data.get("budget"),
            "Overview": movie_data.get("overview"),
            "Director Name": ", ".join([crew['name'] for crew in credits_data.get("crew", []) if crew['job'] == 'Director']),
            "Poster Link": f"{IMAGE_BASE_URL}/w500{movie_data.get('poster_path')}",
            "Backdrop Link": f"{IMAGE_BASE_URL}/original{movie_data.get('backdrop_path')}",
            "All the Actors Name": ", ".join([actor['name'] for actor in credits_data.get("cast", [])])
        }

        return results

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    movie_info = get_movie_details()

    if movie_info:
        for key, value in movie_info.items():
            print(f"{key}: {value}")
    else:
        print("Failed to retrieve movie details.")
      
