#!/usr/bin/python3
"""Usando lo que hizo en la tarea #0, amplíe su secuencia
de comandos de Python para exportar datos en formato
JSON."""

import requests
import sys
import json

if __name__ == "__main__":

    did = sys.argv[1]
    url = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                       .format(did))
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    usu = url.json()

    with open('{}.json'.format(did), mode="w") as archivo:
        arreglo = []
        for llenar in todos:
            arreglo.append({"task": llenar.get("title"),
                            "completed": llenar.get("completed"),
                            "username": usu.get("username")})
        comple = {"{}".format(did): arreglo}
        json.dump(comple, archivo)
