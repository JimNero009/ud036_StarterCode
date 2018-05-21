class Movie:
    # a simple class, storing a title, poster_url and movie_url
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
