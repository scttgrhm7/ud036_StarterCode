import media
import fresh_tomatoes

toy_story = media.Movie('Toy Story',
                        'Boy\'s toys come to life',
                        'http://www.impawards.com/1995/posters/toy_story_ver1_xlg.jpg',
                        'https://www.youtube.com/watch?v=KYz2wyBy3kc')

avatar = media.Movie('Avatar',
                     'Humans try to colonize alien planet',
                     'https://www.movieposter.com/posters/archive/main/98/MPW-49433',
                     'https://www.youtube.com/watch?v=5PSNL1qE6VY')

juno = media.Movie('Juno',
                   'Ellen page and Michael Cera have a baby',
                   'http://www.impawards.com/2007/posters/juno_ver2_xlg.jpg',
                   'https://www.youtube.com/watch?v=K0SKf0K3bxg')

# print(avatar.storyline)
# avatar.show_trailer()
# juno.show_trailer()

movies = [toy_story, avatar, juno]
fresh_tomatoes.open_movies_page(movies)
# print(media.Movie.VALID_RATINGS)

# use pre-defined class variables 
print(media.Movie.__module__)
