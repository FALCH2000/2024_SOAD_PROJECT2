import json
import pytest
import os
from .main import editar_reservacion, hacer_reservacion, eliminar_reservacion

def test_copiar_json_originales():
    # Copiar los archivos originales
    with open('./data/disponibilidad.json', 'r') as file:
        disponibilidad_original = json.load(file)
    with open('./data/disponibilidad_backup.json', 'w') as file:
        json.dump(disponibilidad_original, file, indent=4)
    
    with open('./data/reservaciones.json', 'r') as file:
        reservaciones_original = json.load(file)
    with open('./data/reservaciones_backup.json', 'w') as file:
        json.dump(reservaciones_original, file, indent=4)
    
    assert disponibilidad_original == disponibilidad_original
    assert reservaciones_original == reservaciones_original

def test_agregar_reservacion():
    # Crear una reservación
    nombre = "Juan"
    cedula = "118670690"
    dia = "2024-04-07"
    hora = "10:00"
    mesa = 1
    reservacion = hacer_reservacion(nombre, cedula, dia, hora, mesa)
    assert reservacion != json.dumps("Mesa no disponible", ensure_ascii=False)

    # Crear una reservación en una mesa no disponible
    nombre = "Juan"
    cedula = "118670690"
    dia = "2024-04-07"
    hora = "10:00"
    mesa = 1
    reservacion = hacer_reservacion(nombre, cedula, dia, hora, mesa)
    assert reservacion == json.dumps("Mesa no disponible", ensure_ascii=False)

def test_editar_reservacion():
    # Crear una reservación para editar
    nombre = "Juan"
    cedula = "118670690"
    dia = "2024-04-07"
    hora = "12:00"
    mesa = 1
    reservacion = hacer_reservacion(nombre, cedula, dia, hora, mesa)
    assert reservacion != json.dumps("Mesa no disponible", ensure_ascii=False)
    
    # Editar la reservación creada
    nombre = "Justin Fernandez"
    cedula = "118670690"
    dia = "2024-04-07"
    hora = "12:00"
    mesa = 2
    reservacion = json.loads(reservacion)
    id_reservacion = reservacion["id_reservacion"]
    reservacion = editar_reservacion(nombre, cedula, dia, hora, mesa, id_reservacion)
    assert reservacion != json.dumps("Mesa no disponible", ensure_ascii=False)

def test_eliminar_reservacion():
    # Crear una reservación para eliminar
    nombre = "Juan"
    cedula = "118670690"
    dia = "2024-04-07"
    hora = "10:00"
    mesa = 6
    reservacion = hacer_reservacion(nombre, cedula, dia, hora, mesa)
    assert reservacion != json.dumps("Mesa no disponible", ensure_ascii=False)
    # Eliminar la reservación creada
    reservacion = json.loads(reservacion)
    reservacion_original = reservacion["id_reservacion"]
    reservacion = eliminar_reservacion(nombre, cedula, dia, hora, mesa, reservacion_original)
    assert reservacion == json.dumps("Exito", ensure_ascii=False)

def test_restaurar_json_originales():
    # Restaurar los archivos originales
    with open('./data/disponibilidad_backup.json', 'r') as file:
        disponibilidad_original = json.load(file)
    with open('./data/disponibilidad.json', 'w') as file:
        json.dump(disponibilidad_original, file, indent=4)
    
    with open('./data/reservaciones_backup.json', 'r') as file:
        reservaciones_original = json.load(file)
    with open('./data/reservaciones.json', 'w') as file:
        json.dump(reservaciones_original, file, indent=4)
    
    assert disponibilidad_original == disponibilidad_original
    assert reservaciones_original == reservaciones_original

    # eliminar backup
    os.remove('./data/disponibilidad_backup.json')
    os.remove('./data/reservaciones_backup.json')