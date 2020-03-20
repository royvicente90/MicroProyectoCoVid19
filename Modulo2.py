Library = ["0","1","2"]
from collections import *

def Pais():
  import requests

  url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats"

  querystring = {"country":""}

  headers = {
      'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
      'x-rapidapi-key': "10cc64d754msh6ada14806d66f6fp163a2ajsn03dda67c699a"
      }

  response = requests.request("GET", url, headers=headers, params=querystring)

  Z = response.json()

  Datos = []
  pais = []
  provincia = []
  infectados = []
  muertos = []
  recuperados = []
  exData = []
  unico = []
  repetido = []
  SelecPaises = True
  Z = (Z['data']['covid19Stats'])
  # print(X)
  for Y in Z:
    pais.append(Y['country'])
    provincia.append(Y['province'])
    infectados.append(Y['confirmed'])
    muertos.append(Y['deaths'])
    recuperados.append(Y['recovered'])
  Datos.append(pais);Datos.append(provincia)
  exData.append(infectados)
  exData.append(muertos)
  exData.append(recuperados)
  Datos.append(exData)
  #Quitar paises repetidos para mostrar
  for x in Datos[0]:
    if x not in unico:
      unico.append(x)
    else:
      if x not in repetido:
        repetido.append(x)
  print("A continuación se le mostrará una lista de países de los cuales puede escojer cuál quiere ver sus estadísticas sobre el CoVid-19.\n \n=============== Para salir escriba 0. ===============\n")
  for z in unico:
    print(z)
  print();print()
  #Selector de Pais Especifico
  while SelecPaises == True:
    Pais = input("Escoja un país: ")
    if Pais == "0":
      SelecPaises = False
    if Pais in unico:
      import requests

      url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats"

      querystring = {"country":Pais}

      headers = {
          'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
          'x-rapidapi-key': "10cc64d754msh6ada14806d66f6fp163a2ajsn03dda67c699a"
          }

      response = requests.request("GET", url, headers=headers, params=querystring)

      X = response.json()
      
      print("La cantidad de infectados de",str(Pais),"es",X['data']['covid19Stats'][0]['confirmed'])
      
      print("La cantidad de recuperados de",str(Pais),"es",X['data']['covid19Stats'][0]['recovered'])

      print("La cantidad de muertos de",str(Pais),"es",X['data']['covid19Stats'][0]['deaths'])
    else:
      print("Ha introducido un país incorrecto, por favor vuelva a introducir un país.")
      SelecPais = True

def Infectados():
    import requests

    url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats"

    querystring = {"country":""}

    headers = {
        'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
        'x-rapidapi-key': "10cc64d754msh6ada14806d66f6fp163a2ajsn03dda67c699a"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    Infec = response.json()

    import operator

    infectados = {}

    for i in range(len(Infec['data']['covid19Stats'])):
        infectados[Infec['data']['covid19Stats'][i]['country']] = Infec['data']['covid19Stats'][i]['confirmed']

    infectados["China"] = Infec['data']['covid19Stats'][0]['confirmed']    
    infectados = dict(sorted(infectados.items(), key=operator.itemgetter(1)), reverse=True)

    OrgInfec = Counter(infectados)

    TopInfect = OrgInfec.most_common(10)
    
    print("\nTop 10 paises con mas infectados:\n") 

    for i in TopInfect: 
        print(i[0],"tiene",i[1],"infectados")

def Muertes():

    import requests

    url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats"

    querystring = {"country":""}

    headers = {
        'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",  
        'x-rapidapi-key': "10cc64d754msh6ada14806d66f6fp163a2ajsn03dda67c699a"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    dead = response.json()

    muertos = {}

    import operator

    for d in range(len(dead['data']['covid19Stats'])):
        muertos[dead['data']['covid19Stats'][d]['country']] = dead['data']['covid19Stats'][d]['deaths'] 

    muertos["China"] = dead['data']['covid19Stats'][0]['deaths']    
    muertos = dict(sorted(muertos.items(), key=operator.itemgetter(1)), reverse=True)

    OrgMuertos = Counter(muertos)
    
    PaisesMuertes = OrgMuertos.most_common(10)
    
    print("\nTop 10 paises con mas muertes:\n")

    for s in PaisesMuertes:
        print(s[0],"tiene",s[1],"muertes")
 
def Recuperados():

  import requests

  url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats"

  querystring = {"country":""}

  headers = {
      'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
      'x-rapidapi-key': "10cc64d754msh6ada14806d66f6fp163a2ajsn03dda67c699a"
      }

  response = requests.request("GET", url, headers=headers, params=querystring)

  Rec = response.json()

  recuperados = {}

  import operator

  for e in range(len(Rec['data']['covid19Stats'])):
      recuperados[Rec['data']['covid19Stats'][e]['country']] = Rec['data']['covid19Stats'][e]['recovered']

  recuperados["China"] = Rec['data']['covid19Stats'][0]['recovered']    
  recuperados = dict(sorted(recuperados.items(), key=operator.itemgetter(1)), reverse=True)

  OrgRec = Counter(recuperados) 
  
  Top = OrgRec.most_common(10)  
  
  print("\nTop 10 paises con mas recuperados:\n") 

  for q in Top: 
      print(q[0],"tiene",q[1],"recuperados")


#Menú del Módulo 2
def Modulo2():
  print("Bienvenido a la sección de Estadisticas en tiempo real.")
  print();print()
  SelectCorrect = False
  SelectInvalid = False
  while SelectCorrect == False:
    Selector = input("Escriba una opción:\n0.Volver al Menú de Inicio.\n1.Ver el Top de Paises estadisticamente.\n2.Para escojer un país especificamente.\n")
    if Selector not in Library:
        SelectInvalid = True
    else:
        SelectCorrect = True
    #Comprobador de Caracteres Validos
    if SelectInvalid == True:
        print("Ha utilizado un caracter invalido.\nSe le informa que solo se permite usar 0, 1 y 2.")
        SelectInvalid = False
        SelectCorrect = False
  if int(Selector) == 1:
    Infectados()
    Muertes()
    Recuperados()
    Modulo2()
  if int(Selector) == 2:
    Pais()
    Modulo2()
  if int(Selector) == 0:
    pass