import webbrowser

class Video:
    def __init__(self,video_title, video_description, video_poster, video_trailer_url):
        self.title = video_title
        self.description = video_description
        self.poster = video_poster
        self.trailerURL = video_trailer_url
    def getTitle(self):
        return self.title
    def getPoster(self):
        return self.poster
    def getTrailerURL(self):
        return self.trailerURL
    
class Movie(Video):
    def __init__(self, movie_title, movie_description, movie_poster, movie_trailer_url, movie_runtime):
        Video.__init__(self,movie_title, movie_description, movie_poster,movie_trailer_url)
        self.runtime = movie_runtime

    def getMovieDetails(self):
        print(self.getTitle + " " + self.runtime)
        
        
class Show(Video):
    def __init__(self, show_title, show_description,show_poster, show_trailer_url, show_seasons):
        Video.__init__(self, show_title,show_description, show_poster,show_trailer_url)
        self.seasons = show_seasons

    def getMovieDetails(self):
        print(self.getTitle + " " + self.runtime)
