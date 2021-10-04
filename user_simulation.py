#!/usr/bin/env python3
from locust import HttpUser, TaskSet, SequentialTaskSet, task, User, constant, tag, events
from environment_config import carga_variables_entorno
from webdriver.clientrpc import XmlRpcUser
from locust.runners import MasterRunner, WorkerRunner
import os
import random

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

carga_variables_entorno()

class TareasSimuladas(SequentialTaskSet):

    @task
    def on_start(self):
        pass

    @tag('compra-libro')
    @task
    def compraLibro(self):
        self.client.compraLibro()

class EjecucionPruebas(XmlRpcUser):
    host="http://127.0.0.1:8878/"
    tasks= [TareasSimuladas]
    wait_time = constant(1)

