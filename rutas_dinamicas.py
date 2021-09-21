#!/usr/bin/env python3

from locust import HttpUser, TaskSet, SequentialTaskSet, task, User, constant
from environment_config import carga_variables_entorno
import os
import json

carga_variables_entorno()
with open("./scrappage/urls.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

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
