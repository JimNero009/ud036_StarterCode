class Movie:
    '''A simple class, storing a title, poster_url and movie_url.
    Call the constructor with a movie title and (optionally)
    a poster URL and movie trailer URL
    '''

    def __init__(
        self,
        title,
        poster_url='',
        trailer_url=''
    ):
        self.title = title
        self.poster_image_url = poster_url
        self.trailer_youtube_url = trailer_url

    # TODO: add more functionality here
