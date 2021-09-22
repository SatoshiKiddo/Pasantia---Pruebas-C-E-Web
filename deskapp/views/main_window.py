# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import PySide2.Qt


class MainWindowForm(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 700)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 781, 131))
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Plain)
        self.frame.setLineWidth(3)
        self.Routes = QPushButton(self.frame)
        self.Routes.setObjectName(u"Routes")
        self.Routes.setGeometry(QRect(10, 10, 113, 91))
        self.Routes.setStyleSheet(u"QPushButton\n"
"{	\n"
"	height: 2em;\n"
" 	border-style: solid;\n"
"	border-width: 2px;\n"
" 	border-color: #0069c0;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   	background-color:#0069c0;\n"
"	color:white;\n"
"}")
        icon = QIcon()
        icon.addFile(u"./deskapp/assets/Iconos/document_edit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Routes.setIcon(icon)
        self.Routes.setIconSize(QSize(100, 100))
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 100, 59, 16))
        self.Dependencies = QPushButton(self.frame)
        self.Dependencies.setObjectName(u"Dependencies")
        self.Dependencies.setGeometry(QRect(130, 10, 113, 91))
        self.Dependencies.setStyleSheet(u"QPushButton\n"
"{	\n"
"	height: 2em;\n"
" 	border-style: solid;\n"
"	border-width: 2px;\n"
" 	border-color: #0069c0;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   	background-color:#0069c0;\n"
"	color:white;\n"
"}")
        self.Dependencies.setIcon(icon)
        self.Dependencies.setIconSize(QSize(100, 100))
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(140, 100, 91, 16))
        self.DependenciesAle = QPushButton(self.frame)
        self.DependenciesAle.setObjectName(u"DependenciesAle")
        self.DependenciesAle.setGeometry(QRect(250, 10, 113, 91))
        self.DependenciesAle.setStyleSheet(u"QPushButton\n"
"{	\n"
"	height: 2em;\n"
" 	border-style: solid;\n"
"	border-width: 2px;\n"
" 	border-color: #0069c0;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   	background-color:#0069c0;\n"
"	color:white;\n"
"}")
        self.DependenciesAle.setIcon(icon)
        self.DependenciesAle.setIconSize(QSize(100, 100))
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(250, 100, 111, 16))
        self.RoutesAle = QPushButton(self.frame)
        self.RoutesAle.setObjectName(u"RoutesAle")
        self.RoutesAle.setGeometry(QRect(370, 10, 113, 91))
        self.RoutesAle.setStyleSheet(u"QPushButton\n"
"{	\n"
"	height: 2em;\n"
" 	border-style: solid;\n"
"	border-width: 2px;\n"
" 	border-color: #0069c0;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   	background-color:#0069c0;\n"
"	color:white;\n"
"}")
        self.RoutesAle.setIcon(icon)
        self.RoutesAle.setIconSize(QSize(100, 100))
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(410, 100, 59, 16))
        self.errorLine = QTextEdit(self.frame)
        self.errorLine.setObjectName(u"errorLine")
        self.errorLine.setGeometry(QRect(508, 19, 251, 91))
        self.errorLine.setLayoutDirection(Qt.LeftToRight)
        self.RouteTables = QTableWidget(Form)
        self.RouteTables.setObjectName(u"RouteTables")
        self.RouteTables.setGeometry(QRect(10, 150, 371, 471))
        self.RouteTables.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.RouteTables.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.CheckRoute = QCheckBox(Form)
        self.CheckRoute.setObjectName(u"CheckRoute")
        self.CheckRoute.setGeometry(QRect(410, 660, 131, 20))
        self.CheckRouteAle = QCheckBox(Form)
        self.CheckRouteAle.setObjectName(u"CheckRouteAle")
        self.CheckRouteAle.setGeometry(QRect(540, 660, 86, 20))
        self.StaticExecution = QPushButton(Form)
        self.StaticExecution.setObjectName(u"StaticExecution")
        self.StaticExecution.setGeometry(QRect(400, 610, 131, 32))
        self.StaticExecution.setStyleSheet(u"\n"
"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}")
        self.DinamicExecution = QPushButton(Form)
        self.DinamicExecution.setObjectName(u"DinamicExecution")
        self.DinamicExecution.setGeometry(QRect(650, 610, 141, 32))
        self.DinamicExecution.setStyleSheet(u"\n"
"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(430, 150, 41, 16))
        self.label.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.LineHost = QTextEdit(Form)
        self.LineHost.setObjectName(u"LineHost")
        self.LineHost.setGeometry(QRect(420, 170, 221, 23))
        self.LineHost.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(660, 150, 59, 16))
        self.LinePort = QTextEdit(Form)
        self.LinePort.setObjectName(u"LinePort")
        self.LinePort.setGeometry(QRect(650, 170, 131, 23))
        self.LinePort.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(410, 200, 381, 16))
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QFrame.HLine)
        self.line_2 = QFrame(Form)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(410, 590, 381, 16))
        self.line_2.setFrameShadow(QFrame.Plain)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QFrame.HLine)
        self.LineRoute = QTextEdit(Form)
        self.LineRoute.setObjectName(u"LineRoute")
        self.LineRoute.setGeometry(QRect(410, 280, 341, 23))
        self.LineRoute.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.LineDependency = QTextEdit(Form)
        self.LineDependency.setObjectName(u"LineDependency")
        self.LineDependency.setGeometry(QRect(410, 360, 341, 23))
        self.LineDependency.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.LineDependencyAle = QTextEdit(Form)
        self.LineDependencyAle.setObjectName(u"LineDependencyAle")
        self.LineDependencyAle.setGeometry(QRect(410, 440, 341, 23))
        self.LineDependencyAle.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.LineRouteAle = QTextEdit(Form)
        self.LineRouteAle.setObjectName(u"LineRouteAle")
        self.LineRouteAle.setGeometry(QRect(410, 520, 341, 23))
        self.LineRouteAle.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        #self.ScrollTable = QScrollBar(Form)
        #self.ScrollTable.setObjectName(u"ScrollTable")
        #self.ScrollTable.setGeometry(QRect(380, 150, 16, 531))
        #self.ScrollTable.setOrientation(Qt.Vertical)
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(520, 220, 131, 16))
        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(410, 260, 59, 16))
        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(410, 340, 101, 16))
        self.label_10 = QLabel(Form)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(410, 420, 181, 16))
        self.label_11 = QLabel(Form)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(410, 500, 131, 16))
        self.RouteFile = QPushButton(Form)
        self.RouteFile.setObjectName(u"RouteFile")
        self.RouteFile.setGeometry(QRect(750, 280, 41, 32))
        icon1 = QIcon()
        icon1.addFile(u"./deskapp/assets/Iconos/folder_open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.RouteFile.setIcon(icon1)
        self.DependencyFile = QPushButton(Form)
        self.DependencyFile.setObjectName(u"DependencyFile")
        self.DependencyFile.setGeometry(QRect(750, 350, 41, 32))
        self.DependencyFile.setIcon(icon1)
        self.DependencyAleFile = QPushButton(Form)
        self.DependencyAleFile.setObjectName(u"DependencyAleFile")
        self.DependencyAleFile.setGeometry(QRect(750, 430, 41, 32))
        self.DependencyAleFile.setIcon(icon1)
        self.RouteAleFile = QPushButton(Form)
        self.RouteAleFile.setObjectName(u"RouteAleFile")
        self.RouteAleFile.setGeometry(QRect(750, 510, 41, 32))
        self.RouteAleFile.setIcon(icon1)
        self.agregarRonda = QPushButton(Form)
        self.agregarRonda.setObjectName(u"agregarRonda")
        self.agregarRonda.setGeometry(QRect(50, 630, 71, 61))
        icon2 = QIcon()
        icon2.addFile(u"./deskapp/assets/Iconos/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.agregarRonda.setIcon(icon2)
        self.agregarRonda.setIconSize(QSize(100, 100))
        self.eliminarRonda = QPushButton(Form)
        self.eliminarRonda.setObjectName(u"eliminarRonda")
        self.eliminarRonda.setGeometry(QRect(130, 630, 71, 61))
        icon3 = QIcon()
        icon3.addFile(u"./deskapp/assets/Iconos/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.eliminarRonda.setIcon(icon3)
        self.eliminarRonda.setIconSize(QSize(100, 100))
        self.actualizarTabla = QPushButton(Form)
        self.actualizarTabla.setObjectName(u"actualizarTabla")
        self.actualizarTabla.setGeometry(QRect(310, 630, 71, 61))
        icon4 = QIcon()
        icon4.addFile(u"./deskapp/assets/Iconos/refresh.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actualizarTabla.setIcon(icon4)
        self.actualizarTabla.setIconSize(QSize(100, 100))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.Routes.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"Rutas", None))
        self.Dependencies.setText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"Dependencias", None))
        self.DependenciesAle.setText("")
        self.label_5.setText(QCoreApplication.translate("Form", u"Dependencias Ale", None))
        self.RoutesAle.setText("")
        self.label_6.setText(QCoreApplication.translate("Form", u"Rutas Ale", None))
        self.CheckRoute.setText(QCoreApplication.translate("Form", u"Excluir Fijas", None))
        self.CheckRouteAle.setText(QCoreApplication.translate("Form", u"Excluir Aleatorias", None))
        self.CheckRouteAle.setFixedWidth(200)
        self.StaticExecution.setText(QCoreApplication.translate("Form", u"Ejecucion Estatica", None))
        self.DinamicExecution.setText(QCoreApplication.translate("Form", u"Ejecucion Dinamica", None))
        self.label.setText(QCoreApplication.translate("Form", u"HOST", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"PORT", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"RUTA DE ARCHIVOS", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"RUTAS", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"DEPENDENCIAS", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"DEPENDENCIAS ALEATORIAS", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"RUTAS ALEATORIAS", None))
        self.RouteFile.setText("")
        self.DependencyFile.setText("")
        self.DependencyAleFile.setText("")
        self.RouteAleFile.setText("")
    # retranslateUi

