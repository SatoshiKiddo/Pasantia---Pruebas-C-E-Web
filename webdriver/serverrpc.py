import random
import time
from pageActions import PageActions
from xmlrpc.server import SimpleXMLRPCServer
from dotenv import load_dotenv

##Servidor con los casos de prueba

load_dotenv()

def compraLibro():
    try:
        tester = PageActions()
        tester.ingresoPagina()
        tester.inicioSesion()
        tester.addLibro()
        tester.compraLibro()
        tester.cierreApp()
    except Exception as e:
        print(e)
        raise e
    return True


server = SimpleXMLRPCServer(("localhost", 8877))
print("Listening on port 8877...")
server.register_function(compraLibro, "compraLibro")
server.serve_forever()