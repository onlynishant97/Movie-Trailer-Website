import media
import fresh_tomatoes

toy_story = media.Movie("Toy story",
                        "A story of a boy and his toys that came to life",
                        "http://bit.ly/1LYSb5Z",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "Sam Worthington, Zoe Saldana, S. Weaver",
                     "http://ecx.images-amazon.com/images/I/41vuODnDSuL.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

hunger_games = media.Movie("Hunger Games",
                           "Josh Hutcherson, Liam Hemsworth, J. Lawrence",
                           "http://bit.ly/1KKnRuk",
                           "https://www.youtube.com/watch?v=mfmrPu43DF8")

sanju = media.Movie("Sanju","A biopic of Sanjay Dutt","https://en.wikipedia.org/wiki/Sanju#/media/File:Sanju_-_Theatrical_poster.jpg","https://www.youtube.com/watch?v=1J76wN0TPI4")


bumblebee = media.Movie("BumbleBee","BUMBLEBEE Official Trailer Teaser Transformers Movie HD in theatre christmas.","https://www.google.co.in/imgres?imgurl=https://pbs.twimg.com/profile_images/1002277877839151104/tEg3fjQh_400x400.jpg&imgrefurl=http://t1.gstatic.com/images?q%3Dtbn:ANd9GcQ8B6TyVclQydqtKEw7ZkQFOOcNiBYneQZM7T-dn4JzTihdy0qi&h=400&w=400&tbnid=Tf0ZRnN7c1tVmM:&q=bumblebee&tbnh=160&tbnw=160&usg=__xIErmllKWKsaO9VV5XEF06tHlzI%3D&vet=10ahUKEwiJ5OeG5rzbAhUEOisKHS8yD_gQ_B0I1wEwHw..i&docid=OV7SU9CYXuVkcM&itg=1&sa=X&ved=0ahUKEwiJ5OeG5rzbAhUEOisKHS8yD_gQ_B0I1wEwHw","https://www.youtube.com/watch?v=jZ6Q1B6x3p0")

joke=media.Movie("The Joker","Have you ever had a really...bad...day?The madness begins. TheJoker 2019","https://www.google.co.in/imgres?imgurl=https://www.sideshowtoy.com/wp-content/uploads/2017/05/dc-comics-batman-arkham-origins-the-joker-statue-prime1-studio-thumb-903037-1.jpg&imgrefurl=https://www.sideshowtoy.com/collectibles/dc-comics-the-joker-prime-1-studio-9030371/&h=350&w=350&tbnid=3FfM5Hik_GSVcM:&q=the+joker&tbnh=186&tbnw=186&usg=__doNzgxEZ5G-71BITAO0r5BQJtDU%3D&vet=10ahUKEwjlhPXJ5rzbAhWYXCsKHemhBhgQ_B0I1gEwEg..i&docid=MEoDiKIpm2kLgM&itg=1&sa=X&ved=0ahUKEwjlhPXJ5rzbAhWYXCsKHemhBhgQ_B0I1gEwEg","https://www.youtube.com/watch?v=8C_E6E0UTqo")

res_evil = media.Movie("Resident Evil",
                           "Zombie-causing virus escapes from the lab",
                           "https://upload.wikimedia.org/wikipedia/en/a/a1/Resident_evil_ver4.jpg",
                           "https://www.youtube.com/watch?v=u6uDnd_v5Bw")

matrix = media.Movie("The Matrix",
                         "The world is a simulation",
                         "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                         "https://www.youtube.com/watch?v=vKQi3bBA1y8")
movies=[matrix,res_evil,joke,bumblebee,sanju,hunger_games,toy_story,avatar]
fresh_tomatoes.open_movies_page(movies);
