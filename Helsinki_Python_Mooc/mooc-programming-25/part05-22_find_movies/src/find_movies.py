# Write your solution here
def find_movies(database: list, search_term: str):
    relevant_movies = []
    for movies in database:
        if search_term.lower() in movies['name'].lower():
            relevant_movies.append(movies)
    return relevant_movies
