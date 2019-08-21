# Movie_Rating_Task
This utility will let you know the rating of movies.

# Prerequisite:
Docker environment is setup at the user end.

# How to run this utility?
Log in to your docker account 

# commands 

pull the  image from docker hub by running below command


    docker pull pankajigec26/python_script:poc
get the image id


    docker images

run the image as a container


    docker run -ti -d [imagedid]

Get the container id


    docker ps

Get inside container to execute script 


    docker exec -it [containerid] /bin/bash

run the script , by passing movie name as an argument, note instead of python , we would be using command python3


    python3 Imdb3.py Avengers


# expected output
    
    
    Movie Name ==>Avengers
    Rotten Tomatoes Ratings -->92%

# Error Handled
    
    API Key Wrong
    Movie name not found
    Rotten Tomatoes ratings not present
    URL is not responding 
    No Ratings are present
    


