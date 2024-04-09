import requests
import json


url = "http://localhost:8080"

data = {
    "texto": "Estoy muy enojado, este restaurante tiene un pesimo servicio."
}

response = requests.get(url, params=data)
print(response.json())

