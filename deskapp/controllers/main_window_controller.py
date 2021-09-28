from logging import exception
from PySide2.QtCore import Qt
from PySide2.QtGui import QColor
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
import sys
import logging

load_dotenv()

logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

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

    def __init__(self, buttonDinamic, buttonStatic, buttonSimulation, hilo):
        threading.Thread.__init__(self)
        self.buttonDinamic= buttonDinamic
        self.buttonStatic= buttonStatic
        self.buttonSimulation= buttonSimulation
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
    celda=-1
    table_populated=False

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
        self.RouteTables.cellClicked.connect(self.cell_selected)
        self.RouteTables.cellChanged.connect(self.cell_changed)
        self.actualizarTabla.clicked.connect(self.refreshTable)
        self.eliminarRonda.clicked.connect(self.delete_route)
        self.agregarRonda.clicked.connect(self.aggregate_route)
        self.radioButtonMaster.clicked.connect(self.radioButtonMasterClick)
        self.radioButtonWorker.clicked.connect(self.radioButtonWorkerClick)
        self.LinePort.setPlaceholderText(self.PORT)
        self.LineHost.setPlaceholderText(self.HOST)
        self.LineRoute.setPlaceholderText(self.FILE_ROUTES_APP)
        self.LineDependency.setPlaceholderText(self.FILE_DEPENDENCIES_APP)
        self.LineDependencyAle.setPlaceholderText(self.FILE_ALEATORY_APP)
        self.LineRouteAle.setPlaceholderText(self.FILE_ALEATORY_EX_APP)
        self.table_config()

    def aggregate_route(self):
        if(self.FILE_SELECTED):
            from controllers.nueva_ruta_controller import NuevaRutaController
            window = NuevaRutaController(self)
            window.show()
            self.celda=-1
        else:
            self.logging("No hay archivo seleccionado para agregar", "-q")

    def event(self, event: PySide2.QtCore.QEvent) -> bool:
        try:
            return super().event(event)
        except Exception as e:
            self.logging(e, "-q")
        return False

    def closeEvent(self, event):
        if(self.proceso_ejecucion):
            if(self.proceso_ejecucion.is_alive()):
                self.proceso_ejecucion.stop()
        if(self.proceso):
            if(self.proceso.is_alive()):
                self.proceso.stop()
        self.logging("Cierre de aplicacion", "-v")
        event.accept()

    def existencia_file(self, ruta):
        try:
            open(ruta)
            self.logging("Archivo cargado", "-v")
        except:
            self.logging("Archivo inexistente", "-q")
            return False
        return True

    def logging(self,text, valor):
        if (valor == '-v'):
            self.errorLine.setTextColor(QColor(255,255,255))
            logging.info(text)
        elif (valor == '-vv'):
            self.errorLine.setTextColor(QColor(255,255,255))
            logging.debug(text)
        elif (valor == '-q'):
            self.errorLine.setTextColor(QColor(255,0,0))
            logging.error(text)
        self.errorLine.setText(text)

    def refresh(self):
        os.environ['HOST']= self.HOST
        os.environ['PORT']= self.PORT
        os.environ['FILE_ROUTES_APP']= self.FILE_ROUTES_APP
        os.environ['FILE_ALEATORY_EX_APP']= self.FILE_ALEATORY_EX_APP
        os.environ['FILE_DEPENDENCIES_APP']= self.FILE_DEPENDENCIES_APP
        os.environ['FILE_ALEATORY_APP']= self.FILE_ALEATORY_APP
        self.logging("Actualizacion de variables de entorno", "-v")

    def refresh_file(self, archivo):
        if(self.existencia_file(archivo)):
            os.remove(archivo)
            with open(archivo, 'w') as f:
                f.writelines(self.rutas)
            self.logging("Actualizacion de archivos de entorno", "-v")
        else:
            self.logging("Archivo inexistente o no seleccionado", "-q")

    def refreshTable(self):
        self.refresh()
        self.populate_table(self.rutas)
        self.refresh_file(self.FILE_SELECTED)
        self.celda=-1

    def select_routes(self):
        self.FILE_SELECTED=self.FILE_ROUTES_APP
        if(self.existencia_file(self.FILE_SELECTED)):
            with open(self.FILE_SELECTED) as f:
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
        if(self.existencia_file(self.FILE_SELECTED)):
            with open(self.FILE_SELECTED) as f:
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
        if(self.existencia_file(self.FILE_SELECTED)):
            with open(self.FILE_SELECTED) as f:
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
        if(self.existencia_file(self.FILE_SELECTED)):
            with open(self.FILE_SELECTED) as f:
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
        self.table_populated=False
        self.RouteTables.setRowCount(0)
        self.RouteTables.setRowCount(len(data))
        for(index_row, row) in enumerate(data):
            for(index_cell, cell) in enumerate(row):
                self.RouteTables.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))
        self.RouteTables.resizeRowsToContents()
        self.table_populated=True
        if(self.FILE_SELECTED):
            self.logging("Llenado de tabla con ruta: " + self.FILE_SELECTED, "-v")

    def select_file_routes(self):
        self.FILE_ROUTES_APP = QFileDialog.getOpenFileName()[0] # show an "Open" dialog box and return the path to the selected file
        if(not self.existencia_file(self.FILE_ROUTES_APP)):
            self.FILE_ROUTES_APP=os.getenv('FILE_ROUTES_APP')
        self.logging("Actualizacion de archivo de rutas fijas", "-v")

    def select_file_routes_ale(self):
        self.FILE_ALEATORY_EX_APP = QFileDialog.getOpenFileName()[0] # show an "Open" dialog box and return the path to the selected file
        if(not self.existencia_file(self.FILE_ALEATORY_EX_APP)):
            self.FILE_ROUTES_APP=os.getenv('FILE_ALEATORY_EX_APP')
        self.logging("Actualizacion de archivo de rutas aleatorias", "-v")

    def select_file_dependencies(self):
        self.FILE_DEPENDENCIES_APP = QFileDialog.getOpenFileName()[0] # show an "Open" dialog box and return the path to the selected file
        if(not self.existencia_file(self.FILE_DEPENDENCIES_APP)):
            self.FILE_ROUTES_APP=os.getenv('FILE_DEPENDENCIES_APP')
        self.logging("Actualizacion de archivo de dependencias fijas", "-v")

    def select_file_dependencies_ale(self):
        self.FILE_ALEATORY_APP = QFileDialog.getOpenFileName()[0] # show an "Open" dialog box and return the path to the selected file
        if(not self.existencia_file(self.FILE_ALEATORY_APP)):
            self.FILE_ROUTES_APP=os.getenv('FILE_ALEATORY_APP')
        self.logging("Actualizacion de archivo de dependencias aleatorias", "-v")

    def change_file_routes(self):
        self.FILE_ROUTES_APP=self.LineRoute.toPlainText()
        if(not self.existencia_file(self.FILE_ROUTES_APP)):
            self.FILE_ROUTES_APP=os.getenv('FILE_ROUTES_APP')
            self.logging("No existe archivo de rutas fijas", "-v")
        else:
            self.logging("Actualizacion de archivo de rutas fijas", "-v")


    def change_file_routes_ale(self):
        self.FILE_ALEATORY_EX_APP=self.LineRouteAle.toPlainText()
        if(not self.existencia_file(self.FILE_ALEATORY_EX_APP)):
            self.FILE_ROUTES_APP=os.getenv('FILE_ALEATORY_EX_APP')
            self.logging("No existe archivo de rutas aleatorias", "-v")
        else:
            self.logging("Actualizacion de archivo de rutas aleatorias", "-v")

    def change_file_dependencies(self):
        self.FILE_DEPENDENCIES_APP=self.LineDependency.toPlainText()
        if(not self.existencia_file(self.FILE_DEPENDENCIES_APP)):
            self.FILE_ROUTES_APP=os.getenv('FILE_DEPENDENCIES_APP')
            self.logging("No existe archivo de dependencias", "-v")
        else:
            self.logging("Actualizacion de archivo de dependencias fijas", "-v")


    def change_file_dependencies_ale(self):
        self.FILE_ALEATORY_APP=self.LineDependencyAle.toPlainText()
        if(not self.existencia_file(self.FILE_ALEATORY_APP)):
            self.FILE_ROUTES_APP=os.getenv('FILE_ALEATORY_APP')
            self.logging("No existe archivo de dependencias aleatorias", "-v")
        else:
            self.logging("Actualizacion de archivo de dependencias aleatorias", "-v")

    def change_host(self):
        self.HOST=self.LineHost.toPlainText()
        if(self.HOST == ""):
            self.HOST=os.getenv('HOST')
        self.logging("Actualizacion de HOST objetivo", "-v")

    def change_port(self):
        self.PORT=self.LinePort.toPlainText()
        if(self.PORT == ""):
            self.PORT=os.getenv('PORT')
        self.logging("Actualizacion de PORT objetivo", "-v")

    def execution_dinamic(self):
        self.logging("Ejecucion dinamica de pruebas de carga y estres", "-v")
        option_distributed=""
        if(self.radioButtonMaster.isChecked()):
            option_distributed=" -m"
        elif(self.radioButtonWorker.isChecked()):
            option_distributed=" -w " + self.HOST_MASTER
        self.proceso_ejecucion= EjecucionLoadThread("python3 loadtestweb.py" + option_distributed + " -s")
        self.proceso_ejecucion.start()
        self.proceso= ThreadAlive(self.DinamicExecution,self.StaticExecution, self.SimulationExecution, self.proceso_ejecucion)
        self.proceso.start()

    def execution_static(self):
        self.logging("Ejecucion estatica de pruebas de carga y estres", "-v")
        exclution=""
        if(self.exclude_route_ale):
            exclution= exclution + " " + self.exclude_route_ale
        if(self.exclude_route):
            exclution= exclution + " " + self.exclude_route
        if(self.exclude_route or self.exclude_route_ale):
            exclution= "-E " + exclution
        option_distributed=""
        if(self.radioButtonMaster.isChecked()):
            option_distributed=" -m"
        elif(self.radioButtonWorker.isChecked()):
            option_distributed=" -w " + self.HOST_MASTER
        self.proceso_ejecucion= EjecucionLoadThread("python3 loadtestweb.py" + exclution + option_distributed + " -s")
        self.proceso_ejecucion.start()
        self.proceso= ThreadAlive(self.DinamicExecution,self.StaticExecution, self.SimulationExecution, self.proceso_ejecucion)
        self.proceso.start()

    def execution_simulation(self):
        self.logging('Ejecucion de simulacion de usuarios', '-v')
        option_distributed=""
        if(self.radioButtonMaster.isChecked()):
            option_distributed=" -m"
        elif(self.radioButtonWorker.isChecked()):
            option_distributed=" -w " + self.HOST_MASTER
        self.proceso_ejecucion= EjecucionLoadThread("python3 loadtestweb.py" + option_distributed + " -u")
        self.proceso_ejecucion.start()
        self.proceso= ThreadAlive(self.DinamicExecution,self.StaticExecution, self.SimulationExecution, self.proceso_ejecucion)
        self.proceso.start()

    def condition_route_ale(self):
        self.exclude_route_ale=self.CheckRouteAle.isChecked()
        self.logging("Rutas aleatorias excluidas", "-v")

    def condition_route(self):
        self.exclude_route=self.CheckRoute.isChecked()
        self.logging("Rutas estaticas excluidas", "-v")
    
    def cell_selected(self, row, column):
        self.celda=row
        self.logging("Ruta " + (str(row + 1)) + " seleccionada.", "-v")

    def cell_changed(self, row, column):
        if(self.table_populated):
            items=[]
            for i in range(self.RouteTables.columnCount()) :
                items.append(self.RouteTables.item(row, i).text())
            print(items)
            self.rutas[row]= items[0] + "," + items[1] + "," + items[2]
            self.logging("Ruta " + (str(row + 1)) + " modificada.", "-v")

    def delete_route(self):
        if(self.table_populated and self.celda != -1):
            self.rutas.remove(self.rutas[self.celda])
            rutas_items = []
            for r in self.rutas:
                ruta = r.replace('\n','').split(',')
                rutas_items.append(ruta)
            self.populate_table(rutas_items)
            self.logging("Celda " + self.celda.__str__() +" eliminada.", "-v")
        else:
            self.logging("No hay celda seleccionada o archivo seleccionado.", "-q")

    def radioButtonMasterClick(self):
        self.logging('Metodo master: ' + str(self.radioButtonMaster.isChecked()), '-v')
        self.radioButtonWorker.setChecked(False)

    def radioButtonWorkerClick(self):
        self.logging('Metodo worker: ' + str(self.radioButtonWorker.isChecked()), '-v')
        if(not self.HOST_MASTER.text()):
            self.logging('Se necesita establecer el host al que apunta el worker', '-q')
            self.radioButtonWorker.setChecked(False)
        self.radioButtonMaster.setChecked(False)

