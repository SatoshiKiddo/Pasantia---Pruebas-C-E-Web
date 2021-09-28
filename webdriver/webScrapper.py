import requests
import csv
from bs4 import BeautifulSoup

class WebScrapper(object):

    def __init__ (self, url, params=""):
        self.url= url
        self.response=""
        self.params=params

    def get_request(self):
        self.response= requests.get(self.url, self.params)
        return self.response
    
    def post_request(self):
        self.response= requests.post(self.url, self.params)
        return self.response

    def put_request(self):
        self.response= requests.put(self.url, self.params)
        return self.response

    def delete_request(self):
        self.response= requests.delete(self.url, self.params)
        return self.response
    
    def html_analysis(self):
        self.html= BeautifulSoup(self.response, 'html.parser')
        return self.html
