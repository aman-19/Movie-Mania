from movies.models import Cast_List, Movies_list

# helper funtion to read data from csv and create database

def saveMovies():
    with open("moviesList.csv","r") as file:
        for line in file:
            # line = file.readline()
            movieInfo = list(line.strip().split("\t"))
            movieName = movieInfo[0].strip()
            year = movieInfo[1].strip()
            rating = movieInfo[2].strip()
            stars =  list(movieInfo[3].strip().split('*'))
            Movie_Object = Movies_list()

            # print(movieName)
            # print(year)
            # print(rating)
            # print(stars)
            
            Movie_Object.movie_name = movieName
            Movie_Object.rating = float(rating)
            Movie_Object.year = int(year.strip())
            Movie_Object.save()
            for casting in stars:
                cast = casting.strip()
                try:
                    print(cast, "A")
                    query = Cast_List.objects.get(cast_name = cast)
                except:
                    print(cast, "B")
                    query = Cast_List()
                    query.cast_name = cast
                    query.save()
                Movie_Object.cast.add(query)
            Movie_Object.save()
    file.close()

# movie_name =  models.CharField(max_length=200)
# rating = models.FloatField(null=True, blank=True, default=None)
# year = models.IntegerField(default= None ,null=True,blank=True)
# cast = models.ManyToManyField(Cast_List)
