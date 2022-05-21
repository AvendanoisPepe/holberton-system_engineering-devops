#!/usr/bin/python3
"""Escriba una función que consulte la API de Reddit e imprima los títulos de
las primeras 10 publicaciones populares enumeradas para un subreddit
determinado.
"""


def top_ten(subreddit):
    """Solicitud de reddit api y respuesta del proceso"""
    import requests

    url = requests.get("https://www.reddit.com/r/{}/top.json?limit=10"
                       .format(subreddit),
                       headers={"Content-Type": "application/json",
                                "User-Agent": "platform"},
                       allow_redirects=False)

    if url.status_code == 200:
        for titulos in url.json().get("data").get("children"):
            print(titulos.get("data").get("title"))
    else:
        print(None)
