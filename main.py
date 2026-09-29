import requests
import json

url = "https://api.github.com/events"

response = requests.get(url)

data = response.json()


with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

print("Data berhasil disimpan!")