from Tv import Tv
from Consola import Consola
from Scooter import Scooter
from Bicicleta import Bicicleta

lista_tvs = []
lista_consolas = []
lista_scooters = []
lista_bicicletas = []

def cotizar_tvs():
    for i in lista_tvs:
        print(i.calcular_descuento())


def Registrar_tv():
    marca = input("Ingrese la marca del TV: ")
    voltaje = int(input("Ingrese el voltaje del TV: "))
    precio = float(input("Ingrese el precio del TV: "))
    eficiencia = input("Ingrese el nivel de eficiencia del TV (A, B, C, D, E, F): ").upper()
    tamano = float(input("Ingrese el tamaño del TV: "))
    tv = Tv(marca,voltaje,precio,eficiencia,tamano)
    lista_tvs.append(tv)

    print('Se registro su TV con exito')   
    

def Registrar_consola():
    marca = input("Ingrese marca de la consola: ")
    voltaje = input("Ingrese voltaje de la consola: ")
    precio = float(input("Ingrese precio de la consola: "))
    eficiencia = input("Ingrese nivel de eficiencia (A, B, C, D, E, F): ")
    nombre = input("Ingrese nombre de la consola: ")
    version = input("Ingrese versión(Lite o no): ")
    consola = Consola(marca,voltaje,precio,eficiencia,nombre,version)
    lista_consolas.append(consola)
    print("Se registro su consola con exito")

def Registrar_scooter():
    marca = input("Ingrese marca del scooter: ")
    aro = input("Ingrese aro del scooter: ")
    velocidad = input("Ingrese la velocidad del scooter: ")
    peso = float(input("Ingrese peso del scooter (en kg): "))
    precio = float(input("Ingrese precio del scooter: "))
    scooter = Scooter(marca, aro, velocidad, peso, precio)
    lista_scooters.append(scooter)
    print("\nScooter registrado exitosamente.")

def Registrar_bicicleta():
    aro = float(input("Ingrese el aro de la bicicleta: "))
    peso = float(input("Ingrese el peso de la bicicleta (en kg): "))
    precio = float(input("Ingrese el precio de la bicicleta: "))
    marca = input("Ingrese la marca de la bicicleta: ")
    bicicleta = Bicicleta(aro,peso,precio,marca)
    lista_bicicletas.append(bicicleta)
    print("Se registro su bicicleta con exito")
    


while True:
    print("\nMenú:")
    print("1. Registrar TV")
    print("2. Registrar Consola")
    print("3. Registrar Scooter")
    print("4. Registrar Bicicleta")
    print("5. Salir")
    opcion = int(input("Selecciona una opción: "))

    if opcion == 1:
        Registrar_tv()
        cotizar_tvs()

    elif opcion == 2:
        Registrar_consola()

    elif opcion == 3:
        Registrar_scooter()
    
    elif opcion == 4:
        Registrar_bicicleta()
    
    else:
        print("Opcion no valida, intente nuevamente")