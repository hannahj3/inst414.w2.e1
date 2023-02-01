import json
with open("imdb_movies_1985to2022.json", "r") as jsonFile:
    for line in jsonFile:
        #print(line)
        this_movie = json.loads(line)

    actors = this_movie["actors"]
    for actor in actors:
        actor_name = actor[1]
        movie_rating = rating
#pseudo code:  
        rating_total = 0
        if "Hugh Jackman" in actors:
            add rating to rating_total
            final rating = rating_total / num movies
            
            
