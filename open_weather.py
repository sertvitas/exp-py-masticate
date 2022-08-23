import requests

API_KEY = "redacted"

CITY = "Townsend"
STATE = "MA"
COUNTRY = "US"

LAT = "42.7129142"
LONG = "-71.7385216"

## URL = "http://api.openweathermap.org/data/2.5/weather?LAT="+LAT+"&lon="+LONG+"&appid="+API_KEY+"&units=imperial" # pylint: disable=line-too-long


URL = (
    "http://api.openweathermap.org/data/2.5/weather?q="
    + CITY
    + ","
    + STATE
    + ","
    + COUNTRY
    + "&appid="
    + API_KEY
    + "&units=imperial"
)

print(URL)

request = requests.get(URL)
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
print("ReLATive humidity of", humidity, "percent")
