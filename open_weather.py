import requests

api_key = "9ca3700ce771a59d1cd0c6ec305030d5"

city = "Townsend"
state = "MA"
country = "US"

lat="42.7129142"
long="-71.7385216"

##url = "http://api.openweathermap.org/data/2.5/weather?lat="+lat+"&lon="+long+"&appid="+api_key+"&units=imperial"

url = "http://api.openweathermap.org/data/2.5/weather?q="+city+","+state+","+country+"&appid="+api_key+"&units=imperial"

print(url)

request = requests.get(url)
json = request.json()

print(json)

