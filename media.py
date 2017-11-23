import webbrowser
# Video class to created video objects
class Video:
    # Video takes in the video title,
    # description, poster URL, and youtube
    # trailer URL
    def __init__(self,video_title,
                 video_description,
                 video_poster,
                 video_trailer_url):
        self.title = video_title
        self.description = video_description
        self.poster = video_poster
        self.trailerURL = video_trailer_url

# Movie class inherits from Video class
# and adds a runtime variable
class Movie(Video):
    def __init__(self, movie_title,
                 movie_description,
                 movie_poster,
                 movie_trailer_url,
                 movie_runtime):
        Video.__init__(self,movie_title,
                       movie_description,
                       movie_poster,
                       movie_trailer_url)
        self.runtime = movie_runtime

        
# Show class inherits from Video class
# and adds a number of seasons variable    
class Show(Video):
    def __init__(self, show_title,
                 show_description,
                 show_poster,
                 show_trailer_url,
                 show_seasons):
        Video.__init__(self, show_title,
                       show_description,
                       show_poster,
                       show_trailer_url)
        self.seasons = show_seasons

