#!/bin/bash

##Instalacion de comandos para extraer los datos
apt-get install wget -y 
apt-get install dpkg -y 
apt-get install zip gzip tar -y

##Cambio al ambiente de paquetes de drivers
cd selenium-web-drivers

##DEBIAN
#wget -c https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -O chrome64.deb
#dpkg -i chrome64.deb
#wget -O ChromeDriver.zip https://chromedriver.storage.googleapis.com/92.0.4577.107/chromedriver_linux64.zip
#unzip ChromeDriver.zip

##MAC
brew install --cask google-chrome
wget -O ChromeDriver.zip https://chromedriver.storage.googleapis.com/92.0.4515.107/chromedriver_mac64.zip
unzip ChromeDriver.zip

export CHROME_DRIVER=./selenium-web-drivers/chromedriver

cd ..