import requests

api_key = "redacted"

city = "Townsend"
state = "MA"
country = "US"

lat = "42.7129142"
long = "-71.7385216"

## url = "http://api.openweathermap.org/data/2.5/weather?lat="+lat+"&lon="+long+"&appid="+api_key+"&units=imperial"

url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "," + state + "," + country + "&appid=" + api_key + "&units=imperial"

print(url)

request = requests.get(url)
json = request.json()

# print(json)

description = json.get("weather")[0].get("description")

print("The weather is", description)

temp = json.get("main").get("temp")
temp_min = json.get("main").get("temp_min")
temp_max = json.get("main").get("temp_max")
humidity = json.get("main").get("humidity")

print("The temperature is", temp)
print("The low temperature will be", temp_min, "with a high of", temp_max)
print("Relative humidity of", humidity, "percent")
