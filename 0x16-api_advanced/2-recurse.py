#!/usr/bin/python3
"""Escriba una función recursiva que consulte la API de Reddit y
devuelva una lista que contenga los títulos de todos los artículos
populares para un subreddit determinado. Si no se encuentran
resultados para el subreddit dado, la función debería devolver
Ninguno.
"""
import requests
sesion = requests.Session()
sesion.headers.update({'User-agent': 'My User Agent'})
sesion.allow_redirects = False


def recurse(subreddit, hot_list=[]):
    URL = "https://www.reddit.com/r/" + subreddit + "/hot.json"
    req = sesion.get(URL).json()
    try:
        for i in req['data']['children']:
            hot_list.append(i['data']['title'])
        if req['data']['after']:
            sesion.params = {'after': req['data']['after']}
            return recurse(subreddit, hot_list)
        return hot_list
    except Exception:
        return None
