import webbrowser # Importing Webbrowser module

# Creating class Theatre for the movie trailer 
class Theatre():
    # initializing constructor with 4 arguments 
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    # displaying trailer using webbrower.open method
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


