from logging import exception
from PySide2.QtCore import Qt
from PySide2.QtGui import QColor
from PySide2.QtWidgets import QFileDialog, QTableWidgetItem, QWidget
from views.nueva_ruta import NuevaRuta
from dotenv import load_dotenv
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os
import logging

logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

class NuevaRutaController(QWidget, NuevaRuta):

    methods=['GET','POST','PUT','DEL']

    def __init__(self, parent=None):
        super().__init__(parent)

        self.parent=parent

        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.comboBoxMethod.addItems(self.methods)
        self.agregarButton.clicked.connect(self.aggregate_route)
        self.cancelarButton.clicked.connect(self.cancel_aggregate)
        self.error_ruta.setText("")
    
    def logging(self,text, valor):
        self.error_ruta.setText(text)
        if (valor == '-v'):
            logging.info(text)
        elif (valor == '-vv'):
            logging.debug(text)
        elif (valor == '-q'):
            logging.error(text)

    def aggregate_route(self):
        if(self.check_inputs()):
            ruta=self.comboBoxMethod.currentText() + "," + self.lineEndpoint.toPlainText() + "," + self.lineBody.toPlainText()
            self.parent.rutas.append(ruta)
            rutas_items = []
            for r in self.parent.rutas:
                ruta = r.replace('\n','').split(',')
                rutas_items.append(ruta)
            self.parent.populate_table(rutas_items)
            self.clean_inputs()
            self.logging("Ruta agregada", "-v")

    def cancel_aggregate(self):
        self.close()

    def check_inputs(self):
        if(self.lineEndpoint.toPlainText != ""):
            return True
        return False
    
    def clean_inputs(self):
        self.lineEndpoint.clear()
        self.lineBody.clear()