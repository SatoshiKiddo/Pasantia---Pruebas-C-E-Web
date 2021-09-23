#!/bin/bash

##
## Construir ejecutable de la aplicacion y ejecutarlo
##

pyinstaller --onefile ./deskapp/app.py
mv ./dist/app ./
./app