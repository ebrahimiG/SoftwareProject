import json
import random

movies = [
    ("Inception", "2010", "Science Fiction", "Christopher Nolan"),
    ("The Godfather", "1972", "Crime", "Francis Ford Coppola"),
    ("Parasite", "2019", "Thriller", "Bong Joon-ho"),
    ("Interstellar", "2014", "Adventure", "Christopher Nolan"),
    ("Spirited Away", "2001", "Animation", "Hayao Miyazaki"),
    ("The Dark Knight", "2008", "Action", "Christopher Nolan"),
    ("Schindler's List", "1993", "Drama", "Steven Spielberg"),
    ("Avengers: Endgame", "2019", "Superhero", "Anthony Russo, Joe Russo"),
    ("Fight Club", "1999", "Drama", "David Fincher"),
    ("La La Land", "2016", "Musical", "Damien Chazelle"),
    ("The Shawshank Redemption", "1994", "Drama", "Frank Darabont"),
    ("Pulp Fiction", "1994", "crime", "Quentin Tarantino"),
    ("The Matrix", "1999", "Science Fiction", "Lana & Lili Wachwski"),
    ("Gladiator", "2000", "Historical Epic", "Ridley Scott"),
    ("Titanic", "1997", "Romance", "James Cameron"),
    ("Goodfellas", "1990", "Crime", "Martin Scoreses"),
    ("The Silence of the Lambs", "1991", "Thriller", "Jonathan Demme"),
    ("Seven Samurai", "1954", "Adventure", "Akira Kurosawa"),
    ("casablanca", "1942", "Romance", "Michael Curtiz"),
    ("Citizen Kane", "1941", "Drama", "Orson Welles"),
    ("Joker", "2019", "Drama", "Todd Phillips"),
    ("Whiplash", "2014", "Drama", "Damien Chazelle"),
    ("Black Panther", "2018", "Superhero", "Ryan Coogler"),
    ("The Lion King", "1994", "Animation", "John Lasseter"),
    ("Coco", "2017", "Animation", "Lee Unkrich"),
    
]

dataset = []
for i in range(250):
    title, year, genre, director = random.choice(movies)
    entry = {
        "input": f"Extract the movie information:\n<div class='movie'><h2>{title}</h2><span class='year'>{year}</span><span class='genre'>{genre}</span><span class='director'>{director}</span></div>",
        "output": {
            "title": title,
            "year": year,
            "genre": genre,
            "director": director
        }
    }
    dataset.append(entry)

with open("movie_dataset_500.json", "w") as f:
    json.dump(dataset, f, indent=2)
