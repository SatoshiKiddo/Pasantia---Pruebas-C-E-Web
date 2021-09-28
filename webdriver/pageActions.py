from webMechanical import SeleniumScrapper
import os
import json

class PageActions(object):

    def __init__(self):
        self.ruta=(str(os.getenv('HOST'))+ str(os.getenv('PORT')))
        self.tester=SeleniumScrapper(self.ruta)

    def ingresoPagina(self):
        self.tester.deleteSession()
        self.tester.get_request()

    def inicioSesion(self):
        self.tester.url= (str(self.ruta) + '/mi-cuenta/')
        self.tester.get_request()
        self.tester.waitElementClass('woocommerce-form-login__submit')
        jsonObject=self.tester.cargaJson('./forms/body_login.json')
        self.tester.cargaFormulario(jsonObject)
        self.tester.clickElementName("login")
        self.tester.waitElementClass('woocommerce-MyAccount-navigation')

    def addLibro(self):
        self.tester.waitElement('menu-item-4165')
        self.tester.clickElement('menu-item-4165')
        self.tester.waitElementClass('woocommerce-loop-product__link')
        self.tester.clickElementClass('woocommerce-loop-product__link')
        self.tester.waitElementName('add-to-cart')
        self.tester.clickElementName('add-to-cart')

    def compraLibro(self):
        self.tester.url= (str(self.ruta) + '/carrito/')
        self.tester.get_request()
        self.tester.waitElementClass('checkout-button')
        self.tester.clickElementClass('checkout-button')

    def cierreApp(self):
        self.tester.close()

    