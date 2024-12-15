import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")
#print(toy_story.storyline)
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "http://www.youtube.com/watch?v=-9ceBgWV8io")
#print(avatar.storyline)
#avatar.show_trailer()
school_of_work = media.Movie("School of work",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                     "http://www.youtube.com/watch?v=-3PsUJFEBC74")
ratatouille = media.Movie("Ratatouille",
                     "A storyline on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                     "http://www.youtube.com/watch?v=-c3sBBRxDAgk")
midnight_in_paris = media.Movie("Midnight in paris",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                     "http://www.youtube.com/watch?v=-atLg2wQQxvU")
hunger_games = media.Movie("Hunger Games",
                     "A Hunger Games on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                     "http://www.youtube.com/watch?v=-PbA63a7H0bo")

movies = [toy_story, avatar, school_of_work, ratatouille, midnight_in_paris, hunger_games]
fresh_tomatoes.open_movies_page(movies)