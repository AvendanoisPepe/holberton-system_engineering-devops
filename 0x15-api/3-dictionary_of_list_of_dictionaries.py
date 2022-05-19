#!/usr/bin/python3
"""Usando lo que hizo en la tarea #0, amplíe su secuencia
de comandos de Python para exportar datos en formato
JSON."""

if __name__ == "__main__":
    import requests
    import sys
    import json

    url = requests.get("https://jsonplaceholder.typicode.com/users").json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    dicci = {}

    for ur in url:
        arreglo = []
        for tareas in todos:
            if tareas.get('userId') == ur.get('id'):
                arreglo.append({"username": ur.get("username"),
                                "task": tareas.get("title"),
                                "completed": tareas.get("completed")})
        dicci[ur.get('id')] = arreglo

    with open('todo_all_employees.json', mode="w") as archivo:
        json.dump(dicci, archivo)
