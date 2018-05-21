from fresh_tomatoes import open_movies_page
from media import Movie

movies = [
    Movie(
        'The Fellowship of the Ring',
        'https://images-na.ssl-images-amazon.com/images/I/51MDpDiZKOL._SY300_.jpg',
        'https://www.youtube.com/watch?v=V75dMMIW2B4'
    ),
    Movie(
        '12 Angry Men',
        'https://ia.media-imdb.com/images/M/'
        'MV5BMWU4N2FjNzYtNTVkNC00NzQ0LTg0MjAtYTJlMjFhNGUxZDFmXkEyXkFqcGdeQXVyNjc1NTYyMjg@'
        '._V1_UX182_CR0,0,182,268_AL_.jpg',
        'https://www.youtube.com/watch?v=A7CBKT0PWFA'
    ),
    Movie(
        'V for Vendetta',
        'https://i.pinimg.com/originals/07/38/b8/0738b8c6ca33ff27812fb9dfa8d8cce7.jpg',
        'https://www.youtube.com/watch?v=k_13fFIrhPk'
    ),
    Movie(
        'Goldfinger',
        'https://1.bp.blogspot.com/-n9BvJyMC3cw/T6dgT7oTs5I/AAAAAAAADe0/'
        '-JlhCGv_3lg/s1600/goldfinger-tribute-poster.jpg',
        'https://www.youtube.com/watch?v=MA65V-oLKa8'
    ),
    Movie(
        '1984',
        'https://www.movieposter.com/posters/archive/main/38/MPW-19416',
        'https://www.youtube.com/watch?v=Z4rBDUJTnNU'
    )
]

if __name__ == '__main__':
    open_movies_page(movies)
