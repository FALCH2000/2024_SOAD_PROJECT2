import requests
import json

url = "https://us-west1-groovy-rope-416616.cloudfunctions.net/chatbot"

data = {
    "texto": "Estoy muy enojado, este restaurante tiene un pesimo servicio."
}

response = requests.get(url, params=data)
print(response.json())

