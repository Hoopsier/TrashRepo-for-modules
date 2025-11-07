import requests
import json

response = requests.get("https://api.chucknorris.io/jokes/random")
response = json.loads(response.content)

print(response["value"])
