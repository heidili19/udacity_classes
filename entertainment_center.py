import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.storyline)
#
avatar = media.Movie("Avatar",
                    "A marine on an alien planet",
                    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                    "https://www.youtube.com/watch?v=cRdxXPV9GNQ")
#print(avatar.storyline)
#print(avatar.show_trailer())

et = media.Movie("ET",
                 "An ET get stuck in the World and meets some friends",
                 "http://originalvintagemovieposters.com/wp-content/uploads/2015/01/ET-3825.jpg",
                 "https://www.youtube.com/watch?v=qYAETtIIClk")
print(et.title)
et.show_trailer()
