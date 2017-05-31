import webbrowser

class Movie():
    """ This class provides a way to store movie related information"""
    # class variables
    VALID_RATINGS = ["G","PG","PG-13", "R"]
    
    # create constructor 
    def __init__(self, title, storyline, poster_image_url, trailer_youtube_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url 
        self.trailer_youtube_url = trailer_youtube_url

    # instance method 
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
    
