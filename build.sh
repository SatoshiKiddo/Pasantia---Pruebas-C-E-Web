#!/bin/bash

##
## Construir ejecutable de la aplicacion y ejecutarlo
##

. ./scripts-utility/webDriverDownload.sh
pyinstaller --onefile ./deskapp/app.py
mv ./dist/app ./
rm -r ./dist
./app