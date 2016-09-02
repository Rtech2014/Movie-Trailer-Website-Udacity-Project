# Movie-Trailer-Project-Udacity 

A simple movie trailer website project for Udacity's full-stack. The project demonstrates the use of a Movie object class in Python to generate a static webpage, which displays a listing of favorite movies and links each movie to its trailers video on YouTube.

# Table of contents

- Download
- Documentation
- Copyright and License

# Download

The files for the project, may be [downloaded here](https://github.com/Rtech2014/Movie-Trailer-Website.git).

# Documentation

### Theatre object class

The Theatre object class consists of four class variables, a simple constructor method, and a class method for playing a Movie object's movie trailer. The code is located in [media.py](https://github.com/Rtech2014/Movie-Trailer-Website-Udacity-Project/blob/master/entertainment_center.py). 

#### Constructor method

The constructor method is called when a new Movie object is created and must include four arguments -- [title](#movietitle), [storyline](#moviestoryline), [poster_image](#movieposter_url), and [trailer_url](#youtubetrailer_url). Each of these arguments is discussed further below.

# Sample Code:
'''
import media

title = "Kabali"
movie_storyline = 1994
poster_image = "http://www.pikbo.com/wp-content/uploads/2016/07/Kabali-Movie-Poster.jpg"
trailer_youtube = "https://www.youtube.com/watch?v=9mdJV5-eias"

# Create Movie object
kabali = theatre_videos.Theatre("kabali",
                        "Gangster movie",
                        "http://www.pikbo.com/wp-content/uploads/2016/07/Kabali-Movie-Poster.jpg",
                        "https://www.youtube.com/watch?v=9mdJV5-eias")

'''
##### movie.title

movie.title is any string used to identify the movie object.

##### movie.storyline

movie.year is an integer representing the year the movie was released.  

##### movie.poster_image

movie.poster_image is a string containing a URL linking to an image which will be used to represent the Movie object.

##### movie.trailer_youtube

movie.trailer_youtube is a string containing a URL linking to the movie trailer on YouTube.com. The movie trailer page portion of the this project extracts the YouTube id from the URL, so while links to other video services are valid in the Movie class object, they will not work with the movie trailers page. 

##### show_trailer method

show_trailer can be called on any Movie class object to launch that object's movie trailer in a webpage. This method is useful for testing but is not used by the script that generates the finished movie trailers page.

### Movie Trailer Page Functions 

The functions used to create the final movie trailers page are located in [fresh_tomatoes.py](https://github.com/Rtech2014/Movie-Trailer-Website/blob/master/theatre_videos.py), along with HTML template variables used by these functions. This file must be imported to access the functions described below.

### open_movies_page function

# Create movie trailer page with array of Movie class objects

fresh_tomatoes.open_movies_page([movie1, movie2, movie3])

#### create_movie_tiles_content

The create_movie_tiles_content function is called by the open_movies_page function. It takes the array of Movie class objects as an argument and iterates through each Movie object and applies the object's data to the portion of the HTML template for each movie. While iterating through each object's class variables, it extracts the YouTube id.

## Copyright and License

- Project starter code (supplied without rights information) contributed by [Udacity](http://www.udacity.com).

- Additional code contributed by [Rajaraman]


# Movie-Trailer-Website-Udacity-Project
