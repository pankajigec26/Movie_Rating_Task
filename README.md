# Movie_Rating_Task
This utility will let you know the rating of movies.

How to run this utility?

Log in to your docker account 

run command 

#This will pull the image where the script is present


    docker pull pankajigec26/movie_rating

#get the image id


    docker images

#run the image as a container


    docker -ti -d [imagedid]

#Get the container id


    docker ps

#Get inside container to execute script 


    docker exec -ti [containerid] /bin/bash

#run the script , by passing movie name as an argument


    python Imdb.py Avengers

#expected output


