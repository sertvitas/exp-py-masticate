from multiprocessing import current_process

current_movies = {'The Grinch': '11am',
                  'Rudolph': '1pm',
                  'Frosty the Snowman': '3pm',
                  'Christmas Vacation': '5pm'
                  }
print("We're showing the following movies:")
for key in current_movies:
    print(key)
movie = input('Which movie do you want the showtime for?\n')

showtime = current_movies.get(movie)
if showtime == None:
    print("The requested movie isn't playing currently")
else:
    print(movie, 'is playing at', showtime)
