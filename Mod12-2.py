import requests
import json

locQ = list(input("Gimme a city in english: ").lower())
locQ[0] = locQ[0].upper()
locQ = "".join(locQ)
print(locQ)
APIKEY = "a2b48414c4f0f2600020156cedc5921f"
loc = requests.get(
    f"http://api.openweathermap.org/geo/1.0/direct?q={
        locQ}&appid={APIKEY}&limit=1"
)
loc = json.loads(loc.content)
lon = loc[0]["lon"]  # Screw you for having me need the index THEN the output
lat = loc[0]["lat"]
units = "metrics"  # Celcius
weather = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?lat={
        lat}&lon={lon}&appid={APIKEY}&units={units}"
)
weather = json.loads(weather.content)


# is tediously using floating decimals instead of doubles
print(weather["main"]["temp"]-273.15)
