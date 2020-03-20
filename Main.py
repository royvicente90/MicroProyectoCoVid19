from Modulo1 import *
from Modulo2 import *
Lib = ["0","1","2"]
def VirusTracker():
    print();print()
    #Variables
    SelectCorrect = False
    SelectInvalid = False
    while SelectCorrect == False:
        Select = input("Escriba:\n1. Para iniciar su examen de CoVid-19.\n2. Para iniciar las Estadisticas Globales.\n0. Para salir del sistema.\n")
        if Select not in Lib:
            SelectInvalid = True
        else:
            SelectCorrect = True
        #Comprobador de Caracteres Validos
        if SelectInvalid == True:
            print("Ha utilizado un caracter invalido.\nSe le informa que solo se permite usar 0, 1 y 2.")
            SelectInvalid = False
            SelectCorrect = False
    if int(Select) == 1:
        TomaDatos()
    if int(Select) == 2:
        Modulo2()
        VirusTracker()
    if int(Select) == 0:
        exit()
    VirusTracker()
print("=========// Bienvenid@ al Sistema de Detección Automatizado para el CoVid-13 \\\=========")
VirusTracker()