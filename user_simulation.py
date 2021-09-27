#!/usr/bin/env python3
from locust import HttpUser, TaskSet, SequentialTaskSet, task, User, constant, tag
import os
import random
from web_driver import testCases

class TareasSimuladas(SequentialTaskSet):

    @task
    def on_start(self):
        self.tester = testCases()
        self.tester.ingresoPagina()
        self.tester.inicioSesion()

    @tag('compra-libro')
    @task
    def entrada_catalogo(self):
        self.tester.addLibro('menu-item-4165')
        self.tester.compraLibro()

class EjecucionPruebas(HttpUser):
    host=os.getenv('HOST') + os.getenv('PORT')
    tasks= [TareasSimuladas]
    wait_time = constant(1)
