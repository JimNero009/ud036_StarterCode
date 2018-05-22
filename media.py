class Movie:
    '''A simple class, storing a title, poster_url and movie_url.
    Attributes:
        title (str): Title of the film.
        poster_url (str, optional): URL to the film's poster.
        trailer_url (str, optional): URL for the film's trailer.
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
