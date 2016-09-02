import theatre_videos  # Importing the theatre_videos module where the constructer is initialized for movies as parameters
import fresh_tomatoes  # Importing the fresh_tomatoes module which helps to generate & render the html page using python code

# Creates 6 different movie trailer instance of Theatre class with 4 parameters(movie_title, movie_storyline, poster_image, trailer_youtube)
kabali = theatre_videos.Theatre("kabali",
                        "Gangster movie",
                        "http://www.pikbo.com/wp-content/uploads/2016/07/Kabali-Movie-Poster.jpg",
                        "https://www.youtube.com/watch?v=9mdJV5-eias")

roopam = theatre_videos.Theatre("vishwaroopam",
                        "Action movie",
                        "http://moviegalleri.net/wp-content/gallery/viswaroopam-telugu-movie-posters/kamal_hassan_viswaroopam_telugu_movie_posters_699f9a2.jpg",
                        "https://www.youtube.com/watch?v=T2F6euNVT5Y")
theri = theatre_videos.Theatre("Theri",
                        "Indian Cop movie",
                        "http://www.vijayfansclub.com/wp-content/uploads/2016/03/vijay-theri-latest-stills-exclusive-04.jpg",
                        "https://www.youtube.com/watch?v=ZK4uGLpkAKk")

vedhalam = theatre_videos.Theatre("Vedhalam",
                        "Commercial movie",
                        "http://www.tamilfreeringtones.com/wp-content/uploads/2015/09/vedhalam-ringtones-free-download.jpg",
                        "https://www.youtube.com/watch?v=3l3K4Tl4XEQ")

twenty_four = theatre_videos.Theatre("24",
                        "Science Fiction movie",
                        "http://www.stage3.in/wp-content/uploads/2015/11/24_firstlook-poster1.jpg",
                        "https://www.youtube.com/watch?v=wqXE_es_I3M")

i = theatre_videos.Theatre("I",
                        "Bodybuilder movie",
                        "http://malligadu.com/wp-content/uploads/2014/10/Shankar_Ai_NewPoster.jpg",
                        "https://www.youtube.com/watch?v=8uPK9Ov6Zd4")

# Storing all the instances as a list and passing it to the function called open_movie_page inside the fresh_tomatoes module
movie_list = [kabali, roopam, theri, vedhalam, twenty_four, i]
fresh_tomatoes.open_movies_page(movie_list)
