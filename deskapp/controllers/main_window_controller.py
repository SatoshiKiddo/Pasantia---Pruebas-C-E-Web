from PySide2.QtCore import Qt
from PySide2.QtWidgets import QFileDialog, QTableWidgetItem, QWidget
from views.main_window import MainWindowForm
from dotenv import load_dotenv
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import PySide2.Qt
import os
import multiprocessing
import threading
import time

load_dotenv()

class EjecucionLoadThread(threading.Thread):

    def __init__(self, command):
        threading.Thread.__init__(self)
        self.command=command
        self._stop_event = threading.Event()


    def run(self):
        os.system(self.command)

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

class ThreadAlive(threading.Thread):

    def __init__(self, buttonDinamic, buttonStatic, hilo):
        threading.Thread.__init__(self)
        self.buttonDinamic= buttonDinamic
        self.buttonStatic= buttonStatic
        self.hilo=hilo
        self._stop_event = threading.Event()


    def run(self):
        self.buttonDinamic.setDisabled(True)
        self.buttonStatic.setDisabled(True)
        while(self.hilo.is_alive()):
            time.sleep(5)
        self.buttonDinamic.setDisabled(False)
        self.buttonStatic.setDisabled(False)

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()
        

class MainWindowController(QWidget, MainWindowForm):

    HOST=os.getenv('HOST')
    PORT=os.getenv('PORT')
    FILE_ROUTES_APP=os.getenv('FILE_ROUTES_APP')
    FILE_ALEATORY_EX_APP=os.getenv('FILE_ALEATORY_EX_APP')
    FILE_DEPENDENCIES_APP=os.getenv('FILE_DEPENDENCIES_APP')
    FILE_ALEATORY_APP=os.getenv('FILE_ALEATORY_APP')
    FILE_SELECTED=None
    exclude_tag_ruta="rutas_ejecucion"
    exclude_tag_ruta_ale="rutas_aleatorias_ejecucion"
    exclude_route=False
    exclude_route_ale=False
    proceso_ejecucion=None
    proceso=None

    rutas=[]

    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.Routes.clicked.connect(self.select_routes)
        self.Dependencies.clicked.connect(self.select_dependencies)
        self.RoutesAle.clicked.connect(self.select_routes_ale)
        self.DependenciesAle.clicked.connect(self.select_dependencies_ale)
        self.LineDependency.textChanged.connect(self.change_file_dependencies)
        self.LineDependencyAle.textChanged.connect(self.change_file_dependencies_ale)
        self.LineRoute.textChanged.connect(self.change_file_routes)
        self.LineRouteAle.textChanged.connect(self.change_file_routes_ale)
        self.LineHost.textChanged.connect(self.change_host)
        self.LinePort.textChanged.connect(self.change_port)
        self.RouteFile.clicked.connect(self.select_file_routes)
        self.RouteAleFile.clicked.connect(self.select_file_routes_ale)
        self.DependencyFile.clicked.connect(self.select_file_dependencies)
        self.DependencyAleFile.clicked.connect(self.select_file_dependencies_ale)
        self.DinamicExecution.clicked.connect(self.execution_dinamic)
        self.StaticExecution.clicked.connect(self.execution_static)
        self.LinePort.setPlaceholderText(self.PORT)
        self.LineHost.setPlaceholderText(self.HOST)
        self.LineRoute.setPlaceholderText(self.FILE_ROUTES_APP)
        self.LineDependency.setPlaceholderText(self.FILE_DEPENDENCIES_APP)
        self.LineDependencyAle.setPlaceholderText(self.FILE_ALEATORY_APP)
        self.LineRouteAle.setPlaceholderText(self.FILE_ALEATORY_EX_APP)
        self.table_config()

    def refresh(self):
        pass

    def refresh_table(self, archivo):
        os.remove(archivo)
        with open(archivo, 'w') as f:
            f.writelines(self.rutas)

    def refreshTable(self):
        self.populate_table(self.rutas)
        self.refresh_table(self.FILE_SELECTED)


    def closeEvent(self, event):
        if(self.proceso_ejecucion):
            if(self.proceso_ejecucion.is_alive()):
                self.proceso_ejecucion.stop()
        if(self.proceso):
            if(self.proceso.is_alive()):
                self.proceso.stop()
        event.accept()

    def select_routes(self):
        self.FILE_SELECTED=self.FILE_ROUTES_APP
        with open(self.FILE_ROUTES_APP) as f:
            self.rutas=[]
            rutas = f.readlines()
            rutas_items = []
            for r in rutas:
                self.rutas.append(r)
                ruta = r.replace('\n','').split(',')
                rutas_items.append(ruta)
            self.populate_table(rutas_items)

    def select_routes_ale(self):
        self.FILE_SELECTED=self.FILE_ALEATORY_EX_APP
        with open(self.FILE_ALEATORY_EX_APP) as f:
            self.rutas=[]
            rutas = f.readlines()
            rutas_items = []
            for r in rutas:
                self.rutas.append(r)
                ruta = r.replace('\n','').split(',')
                rutas_items.append(ruta)
            self.populate_table(rutas_items)

    def select_dependencies(self):
        self.FILE_SELECTED=self.FILE_DEPENDENCIES_APP
        with open(self.FILE_DEPENDENCIES_APP) as f:
            self.rutas=[]
            rutas = f.readlines()
            rutas_items = []
            for r in rutas:
                self.rutas.append(r)
                ruta = r.replace('\n','').split(',')
                rutas_items.append(ruta)
            self.populate_table(rutas_items)

    def select_dependencies_ale(self):
        self.FILE_SELECTED=self.FILE_ALEATORY_APP
        with open(self.FILE_ALEATORY_APP) as f:
            self.rutas=[]
            rutas = f.readlines()
            rutas_items = []
            for r in rutas:
                self.rutas.append(r)
                ruta = r.replace('\n','').split(',')
                rutas_items.append(ruta)
            self.populate_table(rutas_items)

    def table_config(self):
        column_headers = ("Metodo", "Endpoint", "Body")
        self.RouteTables.setColumnCount(len(column_headers))
        self.RouteTables.setHorizontalHeaderLabels(column_headers)

    def populate_table(self,data):
        self.RouteTables.setRowCount(0)
        self.RouteTables.setRowCount(len(data))
        for(index_row, row) in enumerate(data):
            for(index_cell, cell) in enumerate(row):
                self.RouteTables.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))
        self.RouteTables.resizeRowsToContents()
        self.RouteTables.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.RouteTables.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

    def select_file_routes(self):
        self.FILE_ROUTES_APP = QFileDialog.getOpenFileName()[0] # show an "Open" dialog box and return the path to the selected file
        if(self.FILE_ROUTES_APP == ""):
            self.FILE_ROUTES_APP=os.getenv('FILE_ROUTES_APP')

    def select_file_routes_ale(self):
        self.FILE_ALEATORY_EX_APP = QFileDialog.getOpenFileName()[0] # show an "Open" dialog box and return the path to the selected file
        if(self.FILE_ALEATORY_EX_APP == ""):
            self.FILE_ALEATORY_EX_APP=os.getenv('FILE_ALEATORY_EX_APP')

    def select_file_dependencies(self):
        self.FILE_DEPENDENCIES_APP = QFileDialog.getOpenFileName()[0] # show an "Open" dialog box and return the path to the selected file
        if(self.FILE_DEPENDENCIES_APP == ""):
            self.FILE_DEPENDENCIES_APP=os.getenv('FILE_DEPENDENCIES_APP')

    def select_file_dependencies_ale(self):
        self.FILE_ALEATORY_APP = QFileDialog.getOpenFileName()[0] # show an "Open" dialog box and return the path to the selected file
        if(self.FILE_ALEATORY_APP == ""):
            self.FILE_ALEATORY_APP=os.getenv('FILE_ALEATORY_APP')

    def change_file_routes(self):
        self.FILE_ROUTES_APP=self.LinePort.toPlainText()
        if(self.FILE_ROUTES_APP == ""):
            self.FILE_ROUTES_APP=os.getenv('FILE_ROUTES_APP')


    def change_file_routes_ale(self):
        self.FILE_ALEATORY_EX_APP=self.LinePort.toPlainText()
        if(self.FILE_ALEATORY_EX_APP == ""):
            self.FILE_ALEATORY_EX_APP=os.getenv('FILE_ALEATORY_EX_APP')

    def change_file_dependencies(self):
        self.FILE_DEPENDENCIES_APP=self.LinePort.toPlainText()
        if(self.FILE_DEPENDENCIES_APP == ""):
            self.FILE_DEPENDENCIES_APP=os.getenv('FILE_DEPENDENCIES_APP')


    def change_file_dependencies_ale(self):
        self.FILE_ALEATORY_APP=self.LinePort.toPlainText()
        if(self.FILE_ALEATORY_APP == ""):
            self.FILE_ALEATORY_APP=os.getenv('FILE_ALEATORY_APP')

    def change_host(self):
        self.HOST=self.LineHost.toPlainText()
        if(self.HOST == ""):
            self.HOST=os.getenv('HOST')

    def change_port(self):
        self.PORT=self.LinePort.toPlainText()
        if(self.PORT == ""):
            self.PORT=os.getenv('PORT')

    def execution_dinamic(self):
        self.proceso_ejecucion= EjecucionLoadThread("python3 loadtestweb.py -d")
        self.proceso_ejecucion.start()
        self.proceso= ThreadAlive(self.DinamicExecution,self.StaticExecution, self.proceso_ejecucion)
        self.proceso.start()

    def execution_static(self):
        exclution=""
        if(self.exclude_route_ale):
            exclution= exclution + " " + self.exclude_route_ale
        if(self.exclude_route):
            exclution= exclution + " " + self.exclude_route
        if(self.exclude_route or self.exclude_route_ale):
            self.proceso_ejecucion= EjecucionLoadThread("python3 loadtestweb.py -s -E " + exclution)
            self.proceso_ejecucion.start()
        else:
            self.proceso_ejecucion= EjecucionLoadThread("python3 loadtestweb.py -s")
            self.proceso_ejecucion.start()
        self.proceso= ThreadAlive(self.DinamicExecution,self.StaticExecution, self.proceso_ejecucion)
        self.proceso.start()

    def condition_route_ale(self):
        self.exclude_route_ale=self.CheckRouteAle.isChecked()

    def condition_route(self):
        self.exclude_route=self.CheckRoute.isChecked()

