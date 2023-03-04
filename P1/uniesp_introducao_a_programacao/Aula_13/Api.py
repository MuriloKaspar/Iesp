import requests
import json

API_KEY = "a7068901bb6807af688dc37c556fdf9a"
LAT = -7.11532
LOG = -34.861
url = (f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LOG}&appid={API_KEY}")

response = requests.request("GET", url)
objects = json.loads(response.text)

print(objects)
print(type(objects))

for i in objects:
    print(f"{i} :: {objects[i]}")