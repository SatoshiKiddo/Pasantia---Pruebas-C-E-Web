from webMechanical import SeleniumScrapper, WebMechanical
from webScrapper import WebScrapper
import os
import json

class TestCases(object):

    def __init__(self):
        self.ruta=(str(os.getenv('HOST'))+ str(os.getenv('PORT')))
        self.tester=SeleniumScrapper(self.ruta)

    def ingresoPagina(self):
        self.tester.deleteSession()
        self.tester.get_request()

    def inicioSesion(self):
        self.tester.url= (str(self.ruta) + '/mi-cuenta/')
        self.tester.waitElementTag('woocommerce-form-login__submit')
        username = ""
        password = ""
        with open('./bodies/body_login.json') as jsonFile:
            jsonObject = json.load(jsonFile)
            jsonFile.close()
            username = jsonObject['username']
            password = jsonObject['password']
        self.tester.inputValue('username', username)
        self.tester.inputValue('password', password)
        self.tester.clickElementName("login")
        self.tester.waitElementTag('woocommerce-MyAccount-navigation')

    def addLibro(self,elemento):
        self.tester.waitElement(elemento)
        self.tester.clickElement(elemento)
        self.tester.waitElement('woocommerce-loop-product__link')
        self.tester.clickElement('woocommerce-loop-product__link')
        self.tester.waitElementName('add-to-cart')
        self.tester.clickElementName('add-to-cart')

    def compraLibro(Self):
        self.tester.waitElementTag('fa-shopping-cart')
        self.tester.clickElementClass('fa-shopping-cart')
        self.tester.waitElementTag('checkout-button')
        self.tester.clickElementClass('checkout-button')

    