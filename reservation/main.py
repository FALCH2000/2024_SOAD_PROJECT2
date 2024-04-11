# Description: Este archivo contiene la lógica de negocio para la gestión de reservaciones en el restaurante.
# Se definen las funciones para obtener la disponibilidad de las mesas, hacer una reservación, editar una reservación y eliminar una reservación.
# Se utiliza un archivo JSON para almacenar la disponibilidad de las mesas y otro archivo JSON para almacenar las reservaciones.
# Se implementan las funciones para realizar las operaciones de gestión de reservaciones y se exponen como una Cloud Function de Google Cloud Functions.

import functions_framework
from markupsafe import escape
import json
import uuid
from google.cloud import storage

def get_last_id():
    """Obtiene el último ID de reservación."""
    with open('./data/reservaciones.json', 'r') as file:
        reservaciones = json.load(file)
    last_id = 0
    if len(reservaciones["Reservaciones"]) == 0:
        return last_id
    for reservacion in reservaciones["Reservaciones"]:
        last_id = reservacion["id_reservacion"]
    return last_id

def escribir_en_storage(datos, nombre_archivo):
    """Escribe los datos en un archivo en Google Cloud Storage."""
    # Inicializa el cliente de Google Cloud Storage
    storage_client = storage.Client()

    # Obtén el bucket donde almacenarás el archivo
    bucket = storage_client.bucket('nombre_del_bucket')

    # Crea un objeto Blob en el bucket con el nombre del archivo
    blob = bucket.blob(nombre_archivo)

    # Convierte los datos a formato JSON
    datos_json = json.dumps(datos)

    # Escribe los datos en el archivo en el bucket
    blob.upload_from_string(datos_json)

def obtener_disponibilidad_json():
    """Obtiene la disponibilidad de las mesas desde Google Cloud Storage."""
    storage_client = storage.Client()
    bucket = storage_client.bucket('nombre_del_bucket')
    blob = bucket.blob('disponibilidad.json')
    disponibilidad = json.loads(blob.download_as_string())
    respuesta = {
        "status_code": 200,
        "message": "OK",
        "data": disponibilidad
    }
    return json.dumps(respuesta, ensure_ascii=False)

def hacer_reservacion(nombre, cedula, dia, hora, mesa):
    """Realiza una reservación en el restaurante."""
    # Generar un ID de reservación único
    id_reservacion = get_last_id() + 1

    # Crear el objeto de reservación
    reservacion = {
        "nombre": nombre,
        "cedula": cedula,
        "dia": dia,
        "hora": hora,
        "mesa": str(mesa),
        "id_reservacion": id_reservacion
    }
    try:
        # Actualizar la disponibilidad de mesas y validar que la mesa esté disponible
        with open('./data/disponibilidad.json', 'r') as file:
            disponibilidad = json.load(file)
        # Segun dia, hora y mesa, se marca como no disponible, considera que se accede como 
        for disponibilidad_dia in disponibilidad["disponibilidad"]:
            if disponibilidad_dia["dia"] == dia:
                for disponibilidad_hora in disponibilidad_dia["horas"]:
                    if disponibilidad_hora["hora"] == hora:
                        for disponibilidad_mesa in disponibilidad_hora["mesas"]:
                            if disponibilidad_mesa == str(mesa) and disponibilidad_hora["mesas"][disponibilidad_mesa] == True:
                                disponibilidad_hora["mesas"][disponibilidad_mesa] = False
                            elif disponibilidad_mesa == str(mesa) and disponibilidad_hora["mesas"][disponibilidad_mesa] == False:
                                respuesta = {
                                    "status_code": 400,
                                    "message": "Error: Mesa no disponible.",
                                    "data": ""
                                }
                                return json.dumps(respuesta, ensure_ascii=False)
        with open('./data/disponibilidad.json', 'w') as file:
            json.dump(disponibilidad, file, indent=4)

        # Cargar las reservaciones existentes desde el archivo JSON
        with open('./data/reservaciones.json', 'r') as file:
            reservaciones = json.load(file)
        # Agregar la nueva reservación a la lista de reservaciones
        reservaciones["Reservaciones"].append(reservacion)

        # Guardar las reservaciones actualizadas en el archivo JSON
        with open('./data/reservaciones.json', 'w') as file:
            json.dump(reservaciones, file, indent=4)  # Indentación para una mejor legibilidad
        
        respuesta = {
            "status_code": 200,
            "message": "OK",
            "data": reservacion
        }

        return json.dumps(respuesta, ensure_ascii=False)
    except Exception as e:
        return f"Error: {e}"

def editar_reservacion(nombre, cedula, dia, hora, mesa, id_reservacion):
    """Edita una reservación existente en el restaurante."""
    with open('./data/reservaciones.json', 'r') as file:
        reservaciones = json.load(file)
    for reservacion in reservaciones["Reservaciones"]:
        if reservacion["id_reservacion"] == id_reservacion:
            # Actualizar la disponibilidad de mesas y validar que la mesa esté disponible
            with open('./data/disponibilidad.json', 'r') as file:
                disponibilidad = json.load(file)
            # Segun dia, hora y mesa, se marca como no disponible, considera que se accede como 
            for disponibilidad_dia in disponibilidad["disponibilidad"]:
                if disponibilidad_dia["dia"] == dia:
                    for disponibilidad_hora in disponibilidad_dia["horas"]:
                        if disponibilidad_hora["hora"] == hora:
                            for disponibilidad_mesa in disponibilidad_hora["mesas"]:
                                if disponibilidad_mesa == str(mesa) and disponibilidad_hora["mesas"][disponibilidad_mesa] == True:
                                    disponibilidad_hora["mesas"][disponibilidad_mesa] = False
                                elif disponibilidad_mesa == str(mesa) and disponibilidad_hora["mesas"][disponibilidad_mesa] == False:
                                    respuesta = {
                                        "status_code": 400,
                                        "message": "Error: Mesa no disponible.",
                                        "data": ""
                                    }
                                    return json.dumps(respuesta, ensure_ascii=False)
            with open('./data/disponibilidad.json', 'w') as file:
                json.dump(disponibilidad, file, indent=4)

            # Habilitar disponibilidad de la mesa original
            for disponibilidad_dia in disponibilidad["disponibilidad"]:
                if disponibilidad_dia["dia"] == reservacion["dia"]:
                    for disponibilidad_hora in disponibilidad_dia["horas"]:
                        if disponibilidad_hora["hora"] == reservacion["hora"]:
                            for disponibilidad_mesa in disponibilidad_hora["mesas"]:
                                if disponibilidad_mesa == reservacion["mesa"] and disponibilidad_hora["mesas"][disponibilidad_mesa] == False:
                                    disponibilidad_hora["mesas"][disponibilidad_mesa] = True
                                elif disponibilidad_mesa == reservacion["mesa"] and disponibilidad_hora["mesas"][disponibilidad_mesa] == True:
                                    respuesta = {
                                        "status_code": 400,
                                        "message": "Error: Mesa no coincide con reservación.",
                                        "data": ""
                                    }
                                    return json.dumps(respuesta, ensure_ascii=False)
            
            with open('./data/disponibilidad.json', 'w') as file:
                json.dump(disponibilidad, file, indent=4)

            # eliminar la reservacion original
            reservaciones["Reservaciones"].remove(reservacion)
            with open('./data/reservaciones.json', 'w') as file:
                json.dump(reservaciones, file, indent=4)
            # agregar la reservacion editada
            reservacion["nombre"] = nombre
            reservacion["cedula"] = cedula
            reservacion["dia"] = dia
            reservacion["hora"] = hora
            reservacion["mesa"] = str(mesa)
            reservaciones["Reservaciones"].append(reservacion)
            with open('./data/reservaciones.json', 'w') as file:
                json.dump(reservaciones, file, indent=4)
            
            respuesta = {
                "status_code": 200,
                "message": "OK",
                "data": reservacion
            }

            return json.dumps(respuesta, ensure_ascii=False)

def eliminar_reservacion(nombre, cedula, dia, hora, mesa, reservacion_original):
    """Elimina una reservación existente en el restaurante."""
    with open('./data/reservaciones.json', 'r') as file:
        reservaciones = json.load(file)
    for reservacion in reservaciones["Reservaciones"]:
        if reservacion["id_reservacion"] == reservacion_original:
            # Actualizar la disponibilidad de mesas y validar que la mesa esté disponible
            with open('./data/disponibilidad.json', 'r') as file:
                disponibilidad = json.load(file)
            # Segun dia, hora y mesa, se marca como no disponible, considera que se accede como 
            for disponibilidad_dia in disponibilidad["disponibilidad"]:
                if disponibilidad_dia["dia"] == dia:
                    for disponibilidad_hora in disponibilidad_dia["horas"]:
                        if disponibilidad_hora["hora"] == hora:
                            for disponibilidad_mesa in disponibilidad_hora["mesas"]:
                                if disponibilidad_mesa == str(mesa) and disponibilidad_hora["mesas"][disponibilidad_mesa] == False:
                                    disponibilidad_hora["mesas"][disponibilidad_mesa] = True
            with open('./data/disponibilidad.json', 'w') as file:
                json.dump(disponibilidad, file, indent=4)
            
            reservaciones["Reservaciones"].remove(reservacion)
            with open('./data/reservaciones.json', 'w') as file:
                json.dump(reservaciones, file, indent=4)
            respuesta = {
                "status_code": 200,
                "message": "OK",
                "data": ""
            }
            return json.dumps(respuesta, ensure_ascii=False)
    respuesta = {
        "status_code": 400,
        "message": "Error: Reservación no encontrada.",
        "data": ""
    }
    return json.dumps(respuesta, ensure_ascii=False)

@functions_framework.http
def gestionar_reservacion2(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    request_json = request.get_json(silent=True)
    if request.method == 'OPTIONS':
        # Allows GET requests from any origin with the Content-Type
        # header and caches preflight response for an 3600s
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }

        return ('', 204, headers)
    request_args = request.args
    path = (request.path)
    respuesta = {
        "status_code": 200,
        "message": "OK",
        "data": ""
    }
    if path == "/disponibilidad" and request.method == 'GET':
        # Set CORS headers for the main request
        headers = {
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Origin': '*',
            "Access-Control-Allow-Credentials": "true",

        }
        datos= obtener_disponibilidad_json()
        return (datos, 200, headers)
    elif path == "/reservar" and request.method == 'POST':
        return f"{hacer_reservacion(request_json['nombre'], request_json['cedula'], request_json['dia'], request_json['hora'], request_json['mesa'])}"
    elif path == "/editar" and request.method == 'PUT':
        return f"{editar_reservacion(request_json['nombre'], request_json['cedula'], request_json['dia'], request_json['hora'], request_json['mesa'], request_json['id_reservacion'])}"
    elif path == "/eliminar" and request.method == 'DELETE':
        return f"{eliminar_reservacion(request_json['nombre'], request_json['cedula'], request_json['dia'], request_json['hora'], request_json['mesa'], request_json['id_reservacion'])}"
    else:
        respuesta["status_code"] = 404
        respuesta["message"] = "Error: Método no válido."
        return f"{json.dumps(respuesta, ensure_ascii=False)}"

