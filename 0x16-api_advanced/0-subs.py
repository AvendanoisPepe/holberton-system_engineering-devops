#!/usr/bin/python3
"""Escriba una función que consulte la API de Reddit y devuelva la
cantidad de suscriptores (usuarios no activos, suscriptores totales) para
un subreddit determinado. Si se proporciona un subreddit no válido,
la función debería devolver 0.
"""


def number_of_subscribers(subreddit):
    """Solicitud de reddit api y respuesta del proceso"""
    import requests

    url = requests.get("https://www.reddit.com/r/{}/about.json"
                       .format(subreddit),
                       headers={"Content-Type": "application/json",
                                "User-Agent": "platform"},
                       allow_redirects=False)

    if url.status_code == 200:
        return url.json().get("data").get("subscribers")
    else:
        return 0
