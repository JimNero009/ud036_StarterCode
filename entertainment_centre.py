from fresh_tomatoes import open_movies_page
from media import Movie

movies = [
    Movie(
        'The Fellowship of the Ring',
        'https://images-na.ssl-images-amazon.com/images/I/51MDpDiZKOL._SY300_.jpg',
        'https://www.youtube.com/watch?v=V75dMMIW2B4'
    )
]

if __name__ == '__main__':
    open_movies_page(movies)