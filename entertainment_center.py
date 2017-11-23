import media
import fresh_tomatoes
#creating multiple movie objects
toy_story = media.Movie("Toy Story",
                        "A boys toys come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", # NOQA
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                        81)

avatar = media.Movie("Avatar",
                     "A marine goes to an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", # NOQA
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY",
                     162)

the_avengers = media.Movie("The Avengers",
                           "Marvels the avengers",
                           "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg", # NOQA
                           "https://www.youtube.com/watch?v=eOrNdBpGMv8",
                           143)

lord_of_rings = media.Movie("Lord of the Rings",
                            "Journey to destroy the ring.",
                            "https://upload.wikimedia.org/wikipedia/en/9/9d/Lord_of_the_Rings_-_The_Return_of_the_King.jpg", # NOQA
                            "https://www.youtube.com/watch?v=Pki6jbSbXIY",
                            228)

dark_knight_rises = media.Movie("The Dark Knight Rises",
                                "Batman vs Bane",
                                "https://upload.wikimedia.org/wikipedia/en/8/83/Dark_knight_rises_poster.jpg", # NOQA
                                "https://www.youtube.com/watch?v=g8evyE9TuYk",
                                165)

finding_nemo = media.Movie("Finding Nemo",
                           "Nemo gets lost and his father is on a journey to find him.",
                           "https://upload.wikimedia.org/wikipedia/en/2/29/Finding_Nemo.jpg", # NOQA
                           "https://www.youtube.com/watch?v=wZdpNglLbt8",
                           100)

#list of all the movies to send to html
movies = [toy_story, avatar, the_avengers,
          lord_of_rings, dark_knight_rises,
          finding_nemo]
#sending list of movies to open_movies_page in fresh_tomatoes file
fresh_tomatoes.open_movies_page(movies)

