from locust import HttpUser, TaskSet, SequentialTaskSet, task, User, constant
from environment_config import carga_variables_entorno
import os

carga_variables_entorno()

class TareasSecuenciales(SequentialTaskSet):

    FILE_ROUTES=""
    FILE_DEPENDENCIES=""

    def get_request(self,datos):
        self.client.get(datos[1])

    def post_request(self,datos):
        self.client.post(datos[1], datos[2])

    def read_request(self,archivo):
        with open(archivo) as f:
            for line in f.readlines():
                datos = line.split(',')
                if (datos[0] == "GET"): 
                    self.get_request(datos)
                if (datos[0] == "POST"): 
                    self.post_request(datos)

    @task
    def on_start(self):
        self.FILE_ROUTES=os.getenv('FILE_ROUTES')
        self.FILE_DEPENDENCIES=os.getenv('FILE_DEPENDENCIES')
        if(self.FILE_DEPENDENCIES):
            self.read_request(self.FILE_DEPENDENCIES)

    @task
    def secuencia_rutas(self):
        if(self.FILE_ROUTES):
            self.read_request(self.FILE_ROUTES)

class EjecucionPruebas(HttpUser):
    host=os.getenv('HOST') + os.getenv('PORT')
    tasks= [TareasSecuenciales]
    wait_time = constant(1)
