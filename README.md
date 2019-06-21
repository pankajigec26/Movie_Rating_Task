# Movie_Rating_Task
This utility will let you know the rating of movies.

Prerequisite:
Docker environment is setup at the user end.

How to run this utility?

Log in to your docker account 

run command 

#This will pull the image where the script is present


    docker pull pankajigec26/python_script:poc

#get the image id


    docker images

#run the image as a container


    docker run -ti -d [imagedid]

#Get the container id


    docker ps

#Get inside container to execute script 


    docker exec -it [containerid] /bin/bash

#run the script , by passing movie name as an argument


    python Imdb3.py Avengers


#expected output
    
    
    Movie Name ==>Avengers
    Rotten Tomatoes Ratings -->92%



