#!/usr/bin/env python3
from environment_config import carga_variables_entorno
import os
import getopt, sys

def environment():
    carga_variables_entorno()

def simulation(exclution,master,worker):
    os.system("python3 ./webdriver/serverrpc.py &")
    os.system("locust " + master + exclution + worker + " -f user_simulation.py")

def dinamic(exclution,master,worker):
    if os.path.exists("./scrappage/urls.json"):
        os.remove("./scrappage/urls.json")
    os.system("cd scrappage ; scrapy crawl scrapper -o urls.json ; cd ..")
    os.system("locust " + master + exclution + worker + " -f rutas_dinamicas.py")

def static(exclution,master,worker):
    if os.path.exists("./routes/routes.conf"):
        if os.path.exists("./routes/dependencies.conf"):
            os.system("locust " + master + exclution + worker + " -f rutas_fijas.py")
        else:
            print("El archivo dependencies.conf no esta configurado o creado.")
    else:
        print("El archivo routes.conf no esta configurado o creado.")

def usage():
    print("\nEste comando permite centralizar todos los procedimientos acciones para la ejecucion de pruebas de carga y estres. Recuerde ir a la direccion especificada en su direccion *Localhost:8089*\n"
    + "\t-h or --help: Indica la ayuda para la ejecucion del comando.\n"
    + "\t-m or --master: Indica si el computador que ejecuta el comando es considerado como maestro para la herramienta Locust.\n"
    + "\t-w [host:port] or --worker [host:port]: Indica si el computador que ejecuta el comando es considerado como un worker en locust y apunta al maestro especificado.\n"
    + "\t-d or --dinamic: Indica que se ejecute el metodo de pruebas dinamicas usando Scrappy.\n"
    + "\t-s or --static: Indica que se ejecute el metodo de pruebas estatica.\n"
    + "\t-u or --user-simulation: Indica que e ejecute el metodo de simulacion de usuarios.\n")
    + "\t-E or --exclude: Indica los tags a excluir segun el archivo de locust. Usualmente refiere a los proceso aleatorios o de orden segun la condicion del usuario.\n"

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
    exclution=''
    master=''
    worker=''
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
        elif o in ("-e", "--env"):
            environment()
        elif o in ("-u", "--user-simulation"):
            simulation()
        elif o in ("-E", "--exclude"):
            exclution="-E"
            exclution= exclution + " " + a
        elif o in ("-d", "--dinamic"):
            ##Ejecucion dinamica de pruebas
            dinamic(exclution,master,worker)
        elif o in ("-s", "--static"):
            ##Ejecucion estatica de pruebas
            static(exclution,master,worker)
        elif o in ("-u", "--user-simulation"):
            ##Ejecucion de simulacion de usuario
            simulation(exclution,master,worker)
        else:
            assert False, "unhandled option"
    # ...

if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        sys.exit(125)