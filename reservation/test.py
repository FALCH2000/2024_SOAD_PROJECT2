import requests
import json

# Realizar una solicitud GET para obtener la disponibilidad de las mesas
url = 'http://localhost:8080/disponibilidad'
response = requests.get(url)
print("Estado de la solicitud GET:", response.status_code)
print("Respuesta del servidor GET:", response.text)
print("Disponibilidad de mesas:", response.json())

# Realizar una solicitud POST para crear una reservación
url = 'http://localhost:8080/reservar'
reservacion_data = {
    "nombre": "Juan",
    "cedula": "118670690",
    "dia": "2024-04-07",
    "hora": "10:00",
    "mesa": "1"
}
response = requests.post(url, json=reservacion_data)
datos = response.json()
print("Estado de la solicitud POST:", response.status_code)
print("Respuesta del servidor POST:", response.text)
print("Datos de la reservación:", datos)
# Realizar una solicitud PUT para editar la reservación

url = 'http://localhost:8080/editar'
datos["nombre"] = "Justin Fernandez"
datos["cedula"] = "118670690"
datos["dia"] = "2024-04-07"
datos["hora"] = "12:00"
datos["mesa"] = "2"
response = requests.put(url, json=datos)
print("Estado de la solicitud PUT:", response.status_code)
print("Respuesta del servidor PUT:", response.text)


# Realizar una solicitud DELETE para eliminar la reservación
"""
url = 'http://localhost:8080/eliminar'
response = requests.delete(url, json=datos)
print("Estado de la solicitud DELETE:", response.status_code)
print("Respuesta del servidor DELETE:", response.text)
"""
