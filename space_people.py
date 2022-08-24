"""simple api call/json parse"""
import requests

response = requests.get("http://api.open-notify.org/astros.json")
json = response.json()

print("Folks currently in space:\n")
for person in json["people"]:
    print(person["name"])
