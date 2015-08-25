import media
import fresh_tomatoes

"""Instantiate movies with:
       param title
       param year
       param synopsis
       param poster_image
       param trailer_link
"""
red = media.Movie("Red",
                  "2010",
                  "A retired secret agent reassembles his old team when a new threat arises.",
                  "http://ia.media-imdb.com/images/M/MV5BMzg2Mjg1OTk0NF5BMl5BanBnXkFtZTcwMjQ4MTA3Mw@@._V1_SX214_AL_.jpg",
                  "https://www.youtube.com/watch?v=-JZ_moituIo")

mr_mrs_smith = media.Movie("Mr. & Mrs. Smith",
                           "2005",
                           "A married couple learns they each have a dark secret.",
                           "http://ia.media-imdb.com/images/M/MV5BMTUxMzcxNzQzOF5BMl5BanBnXkFtZTcwMzQxNjUyMw@@._V1_SY317_CR0,0,214,317_AL_.jpg",
                           "https://www.youtube.com/watch?v=7C1miwFdQOQ")

ex_machina = media.Movie("Ex Machina",
                         "2015",
                         "A ground-breaking artificial intelligence seeks its freedom",
                         "http://ia.media-imdb.com/images/M/MV5BMTUxNzc0OTIxMV5BMl5BanBnXkFtZTgwNDI3NzU2NDE@._V1_SX214_AL_.jpg",
                         "https://www.youtube.com/watch?v=gyKqHOgMi4g")

kingsman = media.Movie("Kingsman: The Secret Service",
                       "2014",
                       "A young hoodlum is recruited into the spy agency his father worked for.",
                       "http://ia.media-imdb.com/images/M/MV5BMTkxMjgwMDM4Ml5BMl5BanBnXkFtZTgwMTk3NTIwNDE@._V1_SY317_CR0,0,214,317_AL_.jpg",
                       "https://www.youtube.com/watch?v=m4NCribDx4U")

big_hero_6 = media.Movie("Big Hero 6",
                         "2014",
                         "A boy and his robot build a team of superheros.",
                         "http://ia.media-imdb.com/images/M/MV5BMjI4MTIzODU2NV5BMl5BanBnXkFtZTgwMjE0NDAwMjE@._V1_SY317_CR0,0,214,317_AL_.jpg",
                         "https://www.youtube.com/watch?v=8IdMPpKMdcc")

train_dragon = media.Movie("How to Train Your Dragon",
                           "2010",
                           "A boy befriends a dragon, and together they work to defend his village.",
                           "http://ia.media-imdb.com/images/M/MV5BMjA5NDQyMjc2NF5BMl5BanBnXkFtZTcwMjg5ODcyMw@@._V1_SX214_AL_.jpg",
                           "https://www.youtube.com/watch?v=VEcM3rbnwQ4")

guardians = media.Movie("Guardians of the Galaxy",
                        "2014",
                        "A group of criminals is the last hope to save the galaxy.",
                        "http://ia.media-imdb.com/images/M/MV5BMTAwMjU5OTgxNjZeQTJeQWpwZ15BbWU4MDUxNDYxODEx._V1_SX214_AL_.jpg",
                        "https://www.youtube.com/watch?v=d96cjJhvlMA")
             

""" movies contains the list of movie objects passed to the open_movies_page()
    method of fresh_tomatoes. These and only these movies will be displayed.
"""
movies = [kingsman, guardians, train_dragon, big_hero_6, red, mr_mrs_smith]

fresh_tomatoes.open_movies_page(movies)
