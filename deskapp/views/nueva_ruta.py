# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nueva_ruta.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class NuevaRuta(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 0, 381, 80))
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(3)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 20, 131, 41))
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(120, 100, 59, 16))
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 140, 59, 16))
        self.lineEndpoint = QPlainTextEdit(Form)
        self.lineEndpoint.setObjectName(u"lineEndpoint")
        self.lineEndpoint.setGeometry(QRect(80, 140, 301, 21))
        self.lineEndpoint.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.lineEndpoint.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 180, 41, 16))
        self.lineBody = QPlainTextEdit(Form)
        self.lineBody.setObjectName(u"lineBody")
        self.lineBody.setGeometry(QRect(80, 180, 301, 21))
        self.lineBody.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.lineBody.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(120, 260, 59, 16))
        self.agregarButton = QPushButton(Form)
        self.agregarButton.setObjectName(u"agregarButton")
        self.agregarButton.setGeometry(QRect(70, 250, 41, 32))
        icon = QIcon()
        icon.addFile(u"./deskapp/assets/Iconos/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.agregarButton.setIcon(icon)
        self.agregarButton.setIconSize(QSize(32, 32))
        self.cancelarButton = QPushButton(Form)
        self.cancelarButton.setObjectName(u"cancelarButton")
        self.cancelarButton.setGeometry(QRect(200, 250, 41, 32))
        icon1 = QIcon()
        icon1.addFile(u"./deskapp//assets/Iconos/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cancelarButton.setIcon(icon1)
        self.cancelarButton.setIconSize(QSize(32, 32))
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(250, 260, 59, 16))
        self.error_ruta = QTextEdit(Form)
        self.error_ruta.setObjectName(u"error_ruta")
        self.error_ruta.setEnabled(True)
        self.error_ruta.setGeometry(QRect(78, 220, 301, 20))
        self.error_ruta.setAlignment(Qt.AlignCenter)
        self.error_ruta.setReadOnly(True)
        self.comboBoxMethod = QComboBox(Form)
        self.comboBoxMethod.setObjectName(u"comboBoxMethod")
        self.comboBoxMethod.setGeometry(QRect(200, 90, 91, 32))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Nueva Ruta", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Metodo", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Endpoint", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Body", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Agregar", None))
        self.agregarButton.setText("")
        self.cancelarButton.setText("")
        self.label_6.setText(QCoreApplication.translate("Form", u"Cancelar", None))
        self.error_ruta.setText(QCoreApplication.translate("Form", u"Error", None))
    # retranslateUi

