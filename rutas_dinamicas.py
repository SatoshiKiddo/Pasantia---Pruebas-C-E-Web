#!/usr/bin/env python3

from locust import HttpUser, TaskSet, SequentialTaskSet, task, User, constant
import os
import json

with open("./scrappage/urls.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()
    repetidos=jsonObject
    repetidos2=[]
    for ruta in jsonObject:
        for ruta2 in repetidos:
            if(ruta['url_route'] == ruta2['url_route']):
                try:
                    repetidos2.index(ruta['url_route'])
                    jsonObject.remove(ruta)
                except ValueError as e:
                    repetidos2.append(ruta['url_route'])
    print(jsonObject)

class TareasSecuenciales(SequentialTaskSet):

    routes=jsonObject

    def get_request(self,route):
        self.client.get(route)

    def read_request(self,routes):
        for route in routes:
                self.get_request(route['url_route'])

    @task
    def secuencia_rutas(self):
        if(self.routes):
            self.read_request(self.routes)

class EjecucionPruebas(HttpUser):
    host=os.getenv('HOST') + os.getenv('PORT')
    tasks= [TareasSecuenciales]
    wait_time = constant(1)
