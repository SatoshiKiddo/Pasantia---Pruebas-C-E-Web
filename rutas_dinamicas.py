#!/usr/bin/env python3
from locust import HttpUser, TaskSet, SequentialTaskSet, task, User, constant, events
from locust.runners import MasterRunner, WorkerRunner
import os
import json

##Master configuration

# Fired when the worker recieves a message of type 'test_users'
def setup_test_users(environment, msg, **kwargs):
    for user in msg.data:
        print(f"User {user['name']} recieved")
    environment.runner.send_message('acknowledge_users', f"Thanks for the {len(msg.data)} users!")

# Fired when the master recieves a message of type 'acknowledge_users'
def on_acknowledge(msg, **kwargs):
    print(msg.data)

@events.init.add_listener
def on_locust_init(environment, **_kwargs):
    if not isinstance(environment.runner, MasterRunner):
        environment.runner.register_message('test_users', setup_test_users)
    if not isinstance(environment.runner, WorkerRunner):
        environment.runner.register_message('acknowledge_users', on_acknowledge)

@events.test_start.add_listener
def on_test_start(environment, **_kwargs):
    if not isinstance(environment.runner, MasterRunner):
        users = [
            {"name": "User1"},
            {"name": "User2"},
            {"name": "User3"},
        ]
        environment.runner.send_message('test_users', users)

####################

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
