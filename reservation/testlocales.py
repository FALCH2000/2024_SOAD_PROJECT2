import requests
import json
"""
url = "https://us-central1-groovy-rope-416616.cloudfunctions.net/gestionar_reservacion/disponibilidad"

response = requests.get(url)
print("Estado de la solicitud GET:", response.status_code)
print("Respuesta del servidor GET:", response.text)
print("Disponibilidad de mesas:", response.json()["data"]["disponibilidad"])
"""
# Reservar una mesa
url = "https://us-central1-groovy-rope-416616.cloudfunctions.net/gestionar_reservacion/reservar"
reservacion_data = {
    "nombre": "Justin Fernandez",
    "cedula": "118670690",
    "dia": "2024-04-09",
    "hora": "12:00",
    "mesa": "8"
}

response = requests.post(url, json=reservacion_data)
print("Estado de la solicitud POST:", response.status_code)
print("Respuesta del servidor POST:", response.text)
print("Datos de la reservación:", response.headers)
