import webbrowser

class Movie():
    def __init__(self,movie_title,movie_storyline,post_image,trailer_youtube):
        self.title = movie_title
        self.storyline = movie_title
        self.poster_image_url = post_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
