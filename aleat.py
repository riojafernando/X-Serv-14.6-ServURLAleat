#!/usr/bin/python

"""
Mismo servidor de URLs aleatorias, pero hecho con orientacion a objetos
"""


import webapp
import random


class Nuevo_Servidor (webapp.webApp):


    def process (self, parsedRequest):
        x = random.randrange(1000000)
        url = "http://localhost:1234/" + str(x)
        Request = ("<html><body><h1>Hola!</h1>" +
                   "</p>" +
                   "<a href=" + url + " target=_blank>Dame otra"
                   "</body></html>"
                   "\r\n")
        return ("200 OK", Request)


if __name__ == "__main__":
    serv = Nuevo_Servidor("localhost", 1234)
