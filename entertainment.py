"""List of movies with data associated with them"""
import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toyes that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

your_name = media.Movie("Kimi No Na Wa (Your Name)",
                        "Red ribbon of fate",
                        "http://i.imgur.com/xNPlWgd.jpg",
                        "https://www.youtube.com/watch?v=hRfHcp2GjVI")

dunkirk = media.Movie("Dunkirk",
                      "A story of survival despite the odds",
                      "https://upload.wikimedia.org/wikipedia/en/1/15/Dunkirk_Film_poster.jpg",  # NOQA
                      "https://www.youtube.com/watch?v=F-eMt3SrfFU")

logan = media.Movie("Logan",
                    "Hugh Jackman's last performance as Wolverine",
                    "https://upload.wikimedia.org/wikipedia/en/3/37/Logan_2017_poster.jpg",  # NOQA
                    "https://www.youtube.com/watch?v=Div0iP65aZo")

anastasia = media.Movie("Anastasia",
                        "The journey of the lost heir to the Tsar",
                        "https://upload.wikimedia.org/wikipedia/en/3/36/Anastasia-don-bluth.jpg",
                        "https://www.youtube.com/watch?v=eNj53-mu7xw")

atlantis = media.Movie("Atlantis: The Lost Empire",
                       "Finding the mythical lost city of Atlantis",
                       "https://upload.wikimedia.org/wikipedia/en/d/de/Atlantis_The_Lost_Empire_poster.jpg",
                       "https://www.youtube.com/watch?v=DeOo19iAJ1E")

meet_the_robinsons = media.Movie("Meet the Robinsons",
                                 "A boy in search of family",
                                 "https://upload.wikimedia.org/wikipedia/en/d/dc/Meet_the_robinsons.jpg",
                                 "https://www.youtube.com/watch?v=S396-fnLldk")

# An array to hold all movie instances to be displayed
movies = [your_name, logan, dunkirk, anastasia, atlantis, meet_the_robinsons, toy_story, avatar]

# Opens up the HTML file to display the movies listed from the array
fresh_tomatoes.open_movies_page(movies)
