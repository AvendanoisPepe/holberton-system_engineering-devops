#!/usr/bin/python3
"""Usando lo que hizo en la tarea #0, extienda su
secuencia de comandos de Python para exportar
datos en formato CSV."""

import requests
import sys
import csv

if __name__ == "__main__":

    did = sys.argv[1]
    url = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                       .format(did))
    nombre = url.json().get('username')
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    with open('{}.csv'.format(did), mode="w") as archivo:
        writer = csv.writer(archivo, delimiter=',', quoting=csv.QUOTE_ALL,
                            lineterminator='\n', quotechar='"')
        for tareas in todos:
            if tareas.get('userId') == int(did):
                writer.writerow([did, nombre, str(tareas.get('completed')),
                                 tareas.get('title')])
