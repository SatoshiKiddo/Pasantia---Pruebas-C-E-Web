#!/usr/bin/env python3
from environment_config import carga_variables_entorno
import os
import getopt, sys

exclution=""
master=""
worker=""

def environment():
    carga_variables_entorno()

def simulation():
    os.system("python3 ./webdriver/serverrpc.py &")
    os.system("locust " + master + exclution + worker + " -f user_simulation.py")

def dinamic():
    if os.path.exists("./scrappage/urls.json"):
        os.remove("./scrappage/urls.json")
    os.system("cd scrappage ; scrapy crawl scrapper -o urls.json ; cd ..")
    os.system("locust " + master + exclution + worker + " -f rutas_dinamicas.py")

def static():
    if os.path.exists("./routes/routes.conf"):
        if os.path.exists("./routes/dependencies.conf"):
            os.system("locust " + master + exclution + worker + " -f rutas_fijas.py")
        else:
            print("El archivo dependencies.conf no esta configurado o creado.")
    else:
        print("El archivo routes.conf no esta configurado o creado.")

def usage():
    pass

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "mvheE:o:w:dsu", ["help", "output="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    output = None
    verbose = False
    for o, a in opts:
        if o == "-v":
            verbose = True
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-m", "--master"):
            master="--master "
            worker=""
        elif o in ("-w", "--worker"):
            worker="--worker --master-host=" + a + " "
            master=""
        elif o in ("-o", "--output"):
            output = a
        elif o in ("-d", "--dinamic"):
            ##Ejecucion dinamica de pruebas
            dinamic()
        elif o in ("-s", "--static"):
            static()
        elif o in ("-e", "--env"):
            environment()
        elif o in ("-u", "--user-simulation"):
            simulation()
        elif o in ("-E", "--exclude"):
            exclution="-E"
            for arg in a:
                exclution= exclution + " " + arg
        else:
            assert False, "unhandled option"
    # ...

if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        sys.exit(125)