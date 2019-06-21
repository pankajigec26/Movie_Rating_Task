import requests
import sys


class imdb:
    def __init__(self, title):
        self.url = 'http://www.omdbapi.com'
        self.title = title
        self.api_key = 'b1c41fdf'
        self.values = {}

    def check_error(self):
        self.payload = {'t': self.title, 'r': 'json', 'apikey': self.api_key}
        try:
            self.values = requests.get(self.url, params=self.payload).json()
            print (self.values['Error'])
        except ValueError:
            print (
                'Caught ValueError Exception, Please check if URL is correct and Up and running')
        except KeyError:
            pass
        return self.values
    def parse_data(self):
        self.movie_data = self.check_error()
        try:
            list_of_movies = self.movie_data["Ratings"]
            print ('Movie Name ==>'+str(sys.argv[1]))
            test = list(filter(lambda movie: movie['Source'] == 'Rotten Tomatoes', list_of_movies))
            if test:
                print ("Rotten Tomatoes Ratings -->" + [value['Value'] for value in test][0])
            else:
                print ("Rotten Tomatoes Ratings not present, Displaying others rating \n")
                print ([value['Source'] for value in list_of_movies][0], [value['Value'] for value in list_of_movies][0])
        except KeyError:
            pass
        except IndexError:
            print ("Ratings not avialable")

   
if len(sys.argv) == 1:
    raise Exception('Please provide movie name as an argument')
else:
    movie = imdb(sys.argv[1])
    movie.parse_data()
