import os
import getopt, sys

def dinamic():
    if os.path.exists("./scrappage/urls.json"):
        os.remove("./scrappage/urls.json")
    os.system("cd scrappage ; scrapy crawl scrapper -o urls.json ; cd ..")
    os.system("locust -f rutas_dinamicas.py")
    ##Se ejecuta el locust con las url

def static():
    if os.path.exists("./routes/routes.conf"):
        if os.path.exists("./routes/dependencies.conf"):
            os.system("locust -f rutas_fijas.py")
        else:
            print("El archivo dependencies.conf no esta configurado o creado.")
    else:
        print("El archivo routes.conf no esta configurado o creado.")
    ##Se ejecuta el locust con las url

def usage():
    pass

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "vho:ds", ["help", "output="])
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
        elif o in ("-o", "--output"):
            output = a
        elif o in ("-d", "--dinamic"):
            ##Ejecucion dinamica de pruebas
            dinamic()
        elif o in ("-s", "--static"):
            ##Ejecucion dinamica de pruebas
            static()
        else:
            assert False, "unhandled option"
    # ...

if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        sys.exit(125)