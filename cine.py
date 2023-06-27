
def mostrar_cartelera () :
    peliculas = [] #lista para almacenar las peliculas en cartelera
    opcion = 0

    while opcion != 2:
        print('menu')
        print("1. agregar pelicula a la cartelera")
        print("sali")

        opcion = int(input("ingrese una opcion"))

        if opcion == 1:
            pelicula = input("ingrese el nombre de la pelicula")

        peliculas.append(peliculas)
        print("pelicula agregada a la cartelera")
        print("pelicula en cartelera: ")
        for pelicula in peliculas:
            print(pelicula)
        mostrar_cartelera()

def mostrar_butacas_disponibles():
    filas = 10
    columnas = 15
    butacas_disponibles = filas * columnas

    print(f"la cantidad de butacas disponibles es de {butacas_disponibles}. ")
    mostrar_butacas_disponibles()

def mostrar_asientos():
    filas = 10
    columnas= 15
    asientos_reservados = [(1, 'B'), (4, 'D'),(7, 'H')] #ejemplo de asientos reservados 

    print("mapa de asientos: ")
    print(" ", end="")
    for letra in range(columnas):
        print(chr(65 + letra), end=(" "))
        print() 

        for fila in range(1, filas + 1):
            print(fila, end=" ")
            for columna in range(columnas):
                if(fila, chr(65 + columna)) in asientos_reservados:
                 print("X", end=" ")
                else:
                    print(".", end=" ")
                print()
            mostrar_asientos()

def comprar_entrada():
    nombre = input("ingresa su nombre: ")
    es_alumno_duoc = input("¿es alumno de duoc? (s/n): ").lower() == "s"
    fila = int(input("ingresa el numero de fila: "))
    columna =(input("ingresa la letra de columna"))

    print("detalles de la compra")
    print("nombre: ", nombre)
    print("alumno de duoc: ", "SI" if es_alumno_duoc else "NO")
    print("ubicacion del asiento: ", f"{fila}{columna}")      

    precio_entrada = 10 #precio base de la entrada 
    if es_alumno_duoc:
        precio_entrada -= 2 #descuento de $2 para alumnos duoc
        print("precio de la entrada: ", precio_entrada)
        comprar_entrada()

import json

def comprar_entrada():
    peliculas = input("ingrese el nombre de la pelicula: ")
    num_entradas = int(input("ingresa la cantidad de entradas que desea comprar: "))

    usuarios = [] #lista para almacenar los usuarios y detalles de compra 

    for _ in range(num_entradas): nombre = input("ingrese su nombre: ")
    fila = int(input("ingrese el numero de fila de asiento: "))
    columna = input("ingrese la letra de la columna del asiento: ")

    usuario = {"nombre": nombre, "asiento": F"{fila}{columna}"}
    usuarios.append(usuario)

    print("usuarios que compraron entradas: ")
    for usuario in usuarios: 
        print("nombre: ", usuario["nombre"])
        print("asientos: ", usuario["asiento"])
        print()
  
    opcion = input("presione 's' para volver al menu principal o cualquier otra tecla para salir: ")
    if opcion.lower() == "S": 
        mostrar_menu()

  # Ordenar las entradas por orden de compra (según la posición en la lista)
    usuarios_ordenados = sorted(usuarios, key=lambda x: usuarios.index(x))

    # Guardar las entradas en un archivo de texto
    with open("entradas.txt", "a") as archivo:
        for usuario in usuarios_ordenados:
            linea = f"Película: {pelicula}, Asiento: {usuario['Asiento']}, Nombre: {usuario['Nombre']}\n"
            archivo.write(linea)

    print("Entradas guardadas exitosamente.")

    opcion = input("Presione 's' para volver al menú principal o cualquier otra tecla para salir: ")
    if opcion.lower() == "s":
        mostrar_menu()

def mostrar_entradas():
    # Leer y mostrar todas las entradas guardadas en el archivo
    with open("entradas.txt", "r") as archivo:
        entradas = archivo.readlines()
        if entradas:
            print("Listado completo de boletas emitidas:")
            for entrada in entradas:
                print(entrada.strip())
        else:
            print("No se han emitido boletas.")

    opcion = input("Presione 's' para volver al menú principal o cualquier otra tecla para salir: ")
    if opcion.lower() == "s":
        mostrar_menu()

def guardar_basedatos():
    pelicula = input("Ingrese el nombre de la película: ")
    base_datos = []

    while True:
        nombre = input("Ingrese el nombre del usuario ('0' para salir): ")
        if nombre == '0':
            break
        fila = input("Ingrese el número de fila del asiento: ")
        columna = input("Ingrese la letra de columna del asiento: ")

        usuario = {"Nombre": nombre, "Asiento": f"{fila}{columna}"}
        base_datos.append(usuario)

    with open(f"{pelicula.lower().replace(' ', '_')}_basedatos.json", "w") as archivo:
        json.dump(base_datos, archivo)
        print("Base de datos guardada exitosamente.")

    opcion = input("Presione 's' para volver al menú principal o cualquier otra tecla para salir: ")
    if opcion.lower() == "s":
        mostrar_menu()

def importar_basedatos():
    pelicula = input("Ingrese el nombre de la película: ")
    archivo = input("Ingrese el nombre del archivo JSON (incluya la extensión .json): ")

    try:
        with open(archivo, "r") as file:
            base_datos = json.load(file)

        print


def mostrar_menu():
    print("-----Menu principal-----")
    print("1. comprar entrada")
    print("2. salir")

    opcion = input("ingresa una opcion")
    if opcion == "1" :
        comprar_entrada()
    elif opcion == "2":
         print("gracias por usar el programa ¡hasta luego!")
    else: 
        print("opcion invalida. por favor, ingrese una opcion valida. ")
        mostrar_menu()





