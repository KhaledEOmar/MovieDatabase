import webbrowser
# Video class to created video objects


class Video:
    """
    Attributes:
        video_title (str): Name of the video (e.g. Toy Story)
        video_discripton (str): General overview of video
        video_poster (str): url to image of video poster
        video_trailer_url (str): url to youtube trailer
    """
    def __init__(self, video_title,
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
    """
    Inherits from video
    Attributes:
        runtime (int): runtime of the movie in minutes
    """
    def __init__(self, movie_title,
                 movie_description,
                 movie_poster,
                 movie_trailer_url,
                 movie_runtime):
        Video.__init__(self, movie_title,
                       movie_description,
                       movie_poster,
                       movie_trailer_url)
        self.runtime = movie_runtime


# Show class inherits from Video class
# and adds a number of seasons variable
class Show(Video):
    """
    Inherits from video
    Attributes:
        seasons (int): number of seasons of show
    """
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
