"""Creates Movie instances"""
import webbrowser

class Movie(object):
    """Creating a movie instance"""
    def __init__(self, title, storyline, poster_image, trailer_youtube_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        """Opens up a browser to display the HTML website"""
        webbrowser.open(self.trailer)
