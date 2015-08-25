import webbrowser

class Movie():
    """Contains information about a single movie"""
    
    def __init__(self, title, year, storyline, poster_image_url, trailer_youtube_url):
        """Constructs an instance of Movie:

        Args:
            title: movie title
            year: release year
            synopsis: a brief plot description
            poster_image: a link to the movie's promotional image
            trailer: a link to the movie's trailer on YouTube
        """
        
        self.title = title
        self.year = year
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
