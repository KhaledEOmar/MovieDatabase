# MovieDatabase
MovieDatabase uses python to dynamically create a single page html movie website. 

# Installation
In order to run MovieDatabase: Install Python 2.7.14 package, and ensure that the Python Path option is selected during installation.
```
$ git clone https://github.com/KhaledEOmar/MovieDatabase.git
```
# Starting the movie website
Run entertainment_center.py to open the trailer website. 

# Adding a new movie
In the entertainment_center.py file, add the following code:
```
OBJECT_NAME = media.Movie("MOVIE TITLE",
                           "MOVIE DESCRIPTION",
                           "URL TO MOVIE POSTER", 
                           "URL TO YOUTUBE MOVIE TRAILER",
                           MINUTE LENGTH MOVIE)
```
Then add the new created object to the movies list
