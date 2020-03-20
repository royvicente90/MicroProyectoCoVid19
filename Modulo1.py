LibName = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
LibState = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
LibEdad = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', 
'65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117', '118', '119', '120']
LibResp = ["0", "1"]
LibNumPhone = ["0","1","2","3","4","5","6","7","8","9"]
LibDireccion = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
def NoInfect():
    global Name
    global Edad
    global NumPhone
    with open("NoInfectados.txt", "a+") as bd:
        bd.write("{},{},{}\n".format(Name, Edad, NumPhone))
    print('Sus datos han sido guardados exitosamente')

def PosibleInfect():
    global Name
    global Edad
    global NumPhone
    #Variables
    StateCorrect = False
    StateInvalid = False
    CityCorrect = False
    CityInvalid = False
    DireccionCorrect = False
    DireccionInvalid = False
    #Operadores
    print("\nPor motivos de Seguridad, le pedimos que nos responda otras preguntas sobre su ubicación.")
    while StateCorrect == False:
        State = input("Por favor introduzca el Estado donde guardará cuarentena: ")
        for x in State:
            if x not in LibState:
                StateInvalid = True
            else:
                StateCorrect = True
        #Comprobador de Caracteres Validos
        if StateInvalid == True:
            print("Ha utilizado un caracter invalido.\nSe le informa que solo se permite usar caracteres alfabéticos sin caracteres especiales como apóstrofes o acentos.")
            StateInvalid = False
            StateCorrect = False

    while CityCorrect == False:
        City = input("Por favor introduzca la ciudad donde guardará cuarentena: ")
        for x in City:
            if x not in LibName:
                CityInvalid = True
            else:
                CityCorrect = True
        #Comprobador de Caracteres Validos
        if CityInvalid == True:
            print("Ha utilizado un caracter invalido.\nSe le informa que solo se permite usar caracteres alfabéticos sin caracteres especiales como apóstrofes o acentos.")
            CityInvalid = False
            CityCorrect = False

    while DireccionCorrect == False:
        Direccion = input("Por favor introduzca su Direccion: ")
        for x in Direccion:
            if x not in LibDireccion:
                DireccionInvalid = True
            else:
                DireccionCorrect = True
        #Comprobador de Caracteres Validos
        if DireccionInvalid == True:
            print("Ha utilizado un caracter invalido.\nSe le informa que solo se permite usar caracteres alfanuméricos sin caracteres especiales como apóstrofes o acentos.")
            DireccionInvalid = False
            DireccionCorrect = False

    with open("PosiblesInfectados.txt", "a+") as bd:
        bd.write("{},{},{},{},{},{}\n".format(Name, Edad, NumPhone, State, City, Direccion))
    print('Sus datos han sido guardados exitosamente')
def Infect():
    global Name
    global Edad
    global NumPhone
    #Variables
    StateCorrect = False
    StateInvalid = False
    CityCorrect = False
    CityInvalid = False
    DireccionCorrect = False
    DireccionInvalid = False
    DocNameCorrect = False
    DocNameInvalid = False
    #Operadores
    print("\nPor motivos de Seguridad, le pedimos que nos responda otras preguntas sobre su ubicación.")
    while StateCorrect == False:
        State = input("Por favor introduzca el Estado donde guardará cuarentena: ")
        for x in State:
            if x not in LibState:
                StateInvalid = True
            else:
                StateCorrect = True
        #Comprobador de Caracteres Validos
        if StateInvalid == True:
            print("Ha utilizado un caracter invalido.\nSe le informa que solo se permite usar caracteres alfabéticos sin caracteres especiales como apóstrofes o acentos.")
            StateInvalid = False
            StateCorrect = False

    while CityCorrect == False:
        City = input("Por favor introduzca la ciudad donde guardará cuarentena: ")
        for x in City:
            if x not in LibName:
                CityInvalid = True
            else:
                CityCorrect = True
        #Comprobador de Caracteres Validos
        if CityInvalid == True:
            print("Ha utilizado un caracter invalido.\nSe le informa que solo se permite usar caracteres alfabéticos sin caracteres especiales como apóstrofes o acentos.")
            CityInvalid = False
            CityCorrect = False

    while DireccionCorrect == False:
        Direccion = input("Por favor introduzca su Direccion: ")
        for x in Direccion:
            if x not in LibDireccion:
                DireccionInvalid = True
            else:
                DireccionCorrect = True
        #Comprobador de Caracteres Validos
        if DireccionInvalid == True:
            print("Ha utilizado un caracter invalido.\nSe le informa que solo se permite usar caracteres alfanuméricos sin caracteres especiales como apóstrofes o acentos.")
            DireccionInvalid = False
            DireccionCorrect = False

    while DocNameCorrect == False:
        DocName = input("Ingrese el nombre completo de su médico tratante: ")
        for x in DocName:
            if x not in LibName:
                DocNameInvalid = True
            else:
                DocNameCorrect = True
        #Comprobador de Caracteres Validos
        if DocNameInvalid == True:
            print("Ha utilizado un caracter invalido como Nombre.\nSe le informa que solo se permite usar caracteres alfabéticos sin caracteres especiales como apóstrofes o acentos.")
            DocNameInvalid = False
            DocNameCorrect = False

    with open("Infectados.txt", "a+") as bd:
        bd.write("{},{},{},{},{},{},{}\n".format(Name, Edad, NumPhone, State, City, Direccion, DocName))
    print('Sus datos han sido guardados exitosamente')

def Clasificar():
    #Variables
    RespCorrect = False
    RespInvalid = False
    RespCorrect2 = False
    RespInvalid2 = False
    RespCorrect3 = False
    RespInvalid3 = False
    RespCorrect4 = False
    RespInvalid4 = False
    RespCorrect5 = False
    RespInvalid5 = False
    secreciones_nasales = False
    dolor_garganta = False
    tos = False
    fiebre = False
    dificultad_respirar = False
    #Set Clasificador a global
    global Classify
    Classify = 0
    #Operadores
    print("A continuación se le pedirá que responda algunas preguntas de manera afirmativa y negativa.\nPara responder de forma afirmativa escriba 1\nDe lo contrario, escriba 0")
    #Secreciones Nasales
    while RespCorrect == False:
        Resp1 = input ("¿Usted padece Secreciones Nasales?: ")
        if Resp1 not in LibResp:
            RespInvalid = True
        else:
            RespCorrect = True
        #Comprobador de Caracteres Validos
        if RespInvalid == True:
            print("Ha utilizado un caracter invalido.\nSe le informa que solo se permite usar 0 en caso negativo, y 1 en caso positivo.")
            RespInvalid = False
            RespCorrect = False
    #Dolor de Garganta
    while RespCorrect2 == False:
        Resp2 = input ("¿Usted padece de Dolor de Garganta?: ")
        if Resp2 not in LibResp:
            RespInvalid2 = True
        else:
            RespCorrect2 = True
        #Comprobador de Caracteres Validos
        if RespInvalid2 == True:
            print("Ha utilizado un caracter invalido.\nSe le informa que solo se permite usar 0 en caso negativo, y 1 en caso positivo.")
            RespInvalid2 = False
            RespCorrect2 = False
    #Tos
    while RespCorrect3 == False:
        Resp3 = input ("¿Usted padece de Tos?: ")
        if Resp3 not in LibResp:
            RespInvalid3 = True
        else:
            RespCorrect3 = True
        #Comprobador de Caracteres Validos
        if RespInvalid3 == True:
            print("Ha utilizado un caracter invalido.\nSe le informa que solo se permite usar 0 en caso negativo, y 1 en caso positivo.")
            RespInvalid3 = False
            RespCorrect3 = False
    #Fiebre
    while RespCorrect4 == False:
        Resp4 = input ("¿Usted padece de Fiebre?: ")
        if Resp4 not in LibResp:
            RespInvalid4 = True
        else:
            RespCorrect4 = True
        #Comprobador de Caracteres Validos
        if RespInvalid4 == True:
            print("Ha utilizado un caracter invalido.\nSe le informa que solo se permite usar 0 en caso negativo, y 1 en caso positivo.")
            RespInvalid4 = False
            RespCorrect4 = False
    #Dificultad para Respirar
    while RespCorrect5 == False:
        Resp5 = input ("¿Usted padece de Dificultad para Respirar?: ")
        if Resp5 not in LibResp:
            RespInvalid5 = True
        else:
            RespCorrect5 = True
        #Comprobador de Caracteres Validos
        if RespInvalid5 == True:
            print("Ha utilizado un caracter invalido.\nSe le informa que solo se permite usar 0 en caso negativo, y 1 en caso positivo.")
            RespInvalid5 = False
            RespCorrect5 = False
    #Chequeador de Padecimientos
    if int(Resp1) == 1:
        secreciones_nasales = True
    if int(Resp2) == 1:
        dolor_garganta = True
    if int(Resp3) == 1:    
        tos = True
    if int(Resp4) == 1:    
        fiebre = True
    if int(Resp5) == 1:        
        dificultad_respirar = True
    #Clasificador
    if secreciones_nasales == False and dolor_garganta == False and tos == False and fiebre == False and dificultad_respirar == False:
        Classify = 0
        print("Usted no esta infectad@")
        NoInfect()
    else: 
        if secreciones_nasales == True and dolor_garganta == True and tos == True and fiebre == True and dificultad_respirar == True:
            Classify = 2
            print("Usted se encuentra infectado@")
            Infect()
        else:
            Classify = 1
            print("Existe una posibilidad que usted se encuentre infectado")
            PosibleInfect()
#CLASIFICACIÓN: 0 = NO INFECTADO; 1 = POSIBLE INFECTADO; 2 = INFECTADO

def TomaDatos():
    #Variables
    NameCorrect = False
    NameInvalid = False
    EdadCorrect = False
    EdadInvalid = False
    NumCorrect = False
    NumInvalid = False
    #Set global
    global Name
    global Edad
    global NumPhone
    #Comprobador de Name
    while NameCorrect == False:
        Name = input ("Ingrese su nombre completo: ")
        for x in Name:
            if x not in LibName:
                NameInvalid = True
            else:
                NameCorrect = True
        #Comprobador de Caracteres Validos
        if NameInvalid == True:
            print("Ha utilizado un caracter invalido como Nombre.\nSe le informa que solo se permite usar caracteres alfabéticos sin caracteres especiales como apóstrofes o acentos.")
            NameInvalid = False
            NameCorrect = False

    while EdadCorrect == False:
        Edad = input("Ingrese su edad: ")
        if Edad not in LibEdad:
            print("Ha introducido un carácter inválido, por favor vuelva a intentarlo.")
        else:
            EdadCorrect = True
            if int(Edad) == 0:
                EdadCorrect = False
                print("Disculpe, solo aceptamos a personas mayores o iguales a 1 año.")

    while NumCorrect == False:
        NumCounter = 0
        NumPhone = str(input("Por favor ingrese su número de teléfono de contacto: "))
        for x in NumPhone:
            NumCounter += 1
            if x not in LibNumPhone:
                NumInvalid = True
            else:
                NumCorrect = True
        #Comprobador de Caracteres Validos
        if NumInvalid == True:
            print("Ha utilizado un caracter inválido.\nSe le informa que solo se permite usar caracteres numéricos")
            NumInvalid = False
            NumCorrect = False
        if NumCounter > 11 or NumCounter < 10:
            print("Ha introducido un Número de Teléfono inválido. Por favor reescribalo.")
            NumInvalid = False
            NumCorrect = False
    Clasificar()
    
def DatosGlobal():
    global Name
    global Edad
    global NumPhone
    global Classify
    return()