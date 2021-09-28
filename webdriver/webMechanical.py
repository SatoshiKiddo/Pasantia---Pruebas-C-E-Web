import requests
import csv
import os
import sys
import time
import mechanicalsoup
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
PATH=os.getenv("CHROME_DRIVER")

class WebMechanical(object):

    def __init__ (self, url, params=""):
        self.url= url
        self.page=""
        self.params=params
        self.browser = mechanicalsoup.StatefulBrowser()

    def get_request(self):
        self.page= self.browser.open(self.url)
        return self.page

    def llenadoForm(self, data, form, element ):
        self.browser.select_form(form)
        self.browser[element] = data

    def envioForm(self):
        self.page = self.browser.submit_selected()
        return self.page

class SeleniumScrapper(object):

    ##El manejo de elementos dentro de selenium en esta clase se realizara por id

    def __init__ (self, url, params=""):
        self.url= url
        self.page=""
        self.params=params
        self.driver= webdriver.Chrome(PATH)

    def cargaJson(self, archivo):
        with open('./forms/body_login.json') as jsonFile:
            jsonObject = json.load(jsonFile)
            jsonFile.close()
        return jsonObject
    
    def cargaFormulario(self, jsonObject):
        for key in list(jsonObject.keys()):
            self.inputValue(key,jsonObject[str(key)])

    def deleteSession(self):
        self.driver.delete_all_cookies()

    def get_request(self):
        self.driver.get(self.url)

    def inputValue(self, id, value):
        input = self.driver.find_element_by_id(id)
        input.clear()
        input.send_keys(value)

    def inputValueClase(self, clase, value):
        input = self.driver.find_element_by_class_name(clase)
        input.send_keys(value)

    def inputValueName(self, name, value):
        input = self.driver.find_element_by_name(name)
        input.send_keys(value)

    def waitElementName(self,id):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, id))
            )
        except Exception as exception:
            print(exception)

    def waitElement(self,id):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, id))
            )
        except Exception as exception:
            print(exception)
    
    def waitElementClass(self,clase):
        try:
            elemento = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, clase))
            )
            print(elemento.text)
        except Exception as exception:
            print(exception)

    def close(self):
        self.driver.quit()
        
    def clickElement(self, id):
        element = self.driver.find_element_by_id(id)
        print(element.text)
        element.click()

    def clickElementClass(self, clase):
        element = self.driver.find_element_by_class_name(clase)
        element.click()

    def clickElementName(self, clase):
        element = self.driver.find_element_by_name(clase)
        element.click()