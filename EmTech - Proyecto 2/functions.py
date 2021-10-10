from collections import Counter                                                                         # Importar la funcion contar.
import csv                                                                                              # Importar lo necesario para trabajar con archivos csv
from typing import ForwardRef   
from os import system, name                                                                             # Importar la funciones OS.

# --------------------------------------------------- #

def clear():                                                                                            # - Funcion limpiar consola.
  
    if name == 'nt':
        _ = system('cls')  
    else:
        _ = system('clear')

# --------------------------------------------------- #

def print_bar(quantity,total, prefix = "", suffix = ""):                                                # - Funcion imprimir las barras de porcentaje en consola.
    filledLength = int(20 * quantity // total)                                                          # Variable donde se guarda la anchura de la barra.
    bar = '█' * filledLength + '-' * (20 - filledLength)                                                # Variable donde se guarda la cantidad barra llena.
    print(f'\r{prefix} |{bar}| {quantity} {suffix}', '\r')                                              # Imprime la barra de porcentaje.

# --------------------------------------------------- #

def Top_routes(dir = "", where = True):                                                                 # - Funcion para calcular las rutas mas usadas.
    
    with open("database\synergy_logistics_database.csv", "r") as arch:                                  # Utililzar el csv de la base de datos.
        reader = csv.DictReader(arch)                                                                   # Recibir la base de datos en un diccionario

        temp_list = []                                                                                  # Creacion Lista temporal

        for item in reader:                                                                             # For para recorrer el diccionario.
            if where == True:                                                                           # If True ingresa los valores por el tipo de direccion.
                if item["direction"] == dir:                                                            # If ingrear por Exportacion o por Importacion.
                    temp_list.append(item["origin"] + " to " + item["destination"])                     # Ingresa en la lista la ciudad origen y destino en una sola variable.
            else:                                                                                       # If False ingresa todos los valores.
                temp_list.append(item["origin"] + " to " + item["destination"])                         # Ingresa en la lista la ciudad origen y destino en  una sola variable.
        
        temp_dict = dict(Counter(temp_list))                                                            # Funcion Counter para contar los datos repetidos y la cantidad de estos
                                                                                                        # y convertilos en un diccionario.
        temp_listsorted = list(sorted(temp_dict.items(), key=lambda item: item[1], reverse=True))       # Convierte el diccionario en lista, con los datos ordenados tomando en
                                                                                                        # cuenta los datos en el index 1.

        return temp_listsorted                                                                          # Regresa la lista.

# --------------------------------------------------- #

def Top_transports():                                                                                   # - Funcion para calcular los transportes mas utilizados
                                                                                                        # tomando en cuenta el valor.
    temp_list = []                                                                                      # Creacion Lista temporal
    temp_listset = []                                                                                   # Creacion Lista temporal

    with open("database\synergy_logistics_database.csv", "r") as arch:                                  # Utililzar el csv de la base de datos.
        reader = csv.DictReader(arch)                                                                   # Recibir la base de datos en un diccionario
        
        s = set()                                                                                       # Creacion de set / Los elementos repetidos se eliminan

        for item in reader:                                                                             # For para recorrer el diccionario e agregar todos los datos distintos.
            s.add(item["transport_mode"])

        for i in s:                                                                                     # For para ingresar los datos en una lista.
            temp_listset.append(i)

    for i in range(0, len(temp_listset)):                                                               # For para recorrer la lista.
        total_cost = 0
        with open("database\synergy_logistics_database.csv", "r") as arch:                              # Utililzar el csv de la base de datos.
            reader = csv.DictReader(arch)                                                               # Recibir la base de datos en un diccionario.

            for item in reader:                                                                         # For recorrer el diccionario.
                if(item["transport_mode"] == temp_listset[i]):                                          # If el transporte es igual al numero de index
                   total_cost = total_cost + int(item["total_value"])                                   # suma el valor de este al total.

            temp_list.append([temp_listset[i], total_cost])                                             # Ingresa el nombre del transporte y el costo total.

    temp_list.sort(reverse=True, key=lambda item: item[1])                                              # Ordena la lista tomando en cuenta el valor en el index 1.

    return temp_list                                                                                    # Regresa la lista.

# --------------------------------------------------- #

def Option_1():                                                                                         # - Funciones 1

    list_routes = Top_routes( where = False)                                                            # Ingresa en la variable el total de las rutaas.
    max_value = list_routes[0][1]                                                                       # Ingresa la mayor cantidad de rutas existente.

    list_import = Top_routes(dir = "Imports")                                                           # Ingresa el total de rutas por Importacion.
    list_export = Top_routes(dir = "Exports")                                                           # Ingresa el total de rutas por Exportacion.

    print("#--- Top 10 Rutas por importacaciones ---#",'\n')

    for row, item in enumerate(list_import):                                                            # Imprimir la lista de imporaciones. Enumerable para agregar un index.
        if row < 10:                                                                                    # Solo imprimir 10.
            print(row + 1,".-", item[0])                                                                # Imprimir el row.
            print_bar(item[1], max_value, prefix= "^", suffix="importaciones")                          # Imprimir la barra de porcentaje.
            print()
    
    print("#--- Top 10 Rutas por exportaciones ---#", '\n')                                             # Imprimir la lista de exporaciones. Enumerable para agregar un index.
    for row, item in enumerate(list_export):                                                            # Solo imprimir 10.
        if row < 10:
            print(row + 1,".-", item[0])
            print_bar(item[1], max_value, prefix= "^", suffix="exportaciones")
            print()

    print("#--- Top 10 Rutas general ---#", '\n')                                                       # Imprimir la lista general de rutas. Enumerable para agregar un index.
    for row, item in enumerate(list_routes):
        if row < 10:
            print(row + 1,".-", item[0])
            print_bar(item[1], max_value, prefix= "^", suffix="rutas")
            print()

# --------------------------------------------------- #

def Option_2():                                                                                         # - Funcion 2.
    print("#--- Medios de transporte por valor ---#")
    list_transport = Top_transports()                                                                   # Ingresa en la variable la lista de los transportes
    max_value = list_transport[0][1]                                                                    # Ingresa el valor maximo.

    for row, item in enumerate(list_transport):                                                         # Imprimir la lista general de rutas. Enumerable para agregar un index.
        
        if(row == 3):                                                                                   # Separar despues de el tercer lugar.
            print("# ----------------------------------------- #","\n")

        print(row + 1, ".-", item[0])
        print_bar(item[1], max_value, prefix="^ $", suffix="ingresos generados")
        print()

# --------------------------------------------------- #

def Option_3():

    with open("database\synergy_logistics_database.csv", "r") as arch:                                  # Utililzar el csv de la base de datos.
        reader = csv.DictReader(arch)                                                                   # Recibir la base de datos en un diccionario.

        temp_listset = []
        temp_list = []

        s = set()                                                                                       # Creacion de set / Los elementos repetidos se eliminan

        for item in reader:                                                                             # Agrega todas las ciudades existentes en la base de datos.
            s.add(item["origin"])
            s.add(item["destination"])

        for i in s:                                                                                     # Convierte el set en una lista.
            temp_listset.append(i)

    for i in range(0, len(temp_listset)):                                                               # For recorrer la cantidad de datos en la lista.
        total_cost = 0
        with open("database\synergy_logistics_database.csv", "r") as arch:                              # Utililzar el csv de la base de datos.
            reader = csv.DictReader(arch)                                                               # Recibir la base de datos en un diccionario.
            for item in reader:                                                                         # Recorrer el diccionario.
                if(item["origin"] == temp_listset[i]):                                                  # Si el origen es igual al index
                    total_cost = total_cost + int(item["total_value"])                                  # Suma el valor al total.
                elif(item["destination"] == temp_listset[i]):                                           # Si el destino es igual al index.
                    total_cost = total_cost + int(item["total_value"])                                  # Suma el valor al total.

        temp_list.append([temp_listset[i], total_cost])                                                 # Ingresa el valor del nombre y el total en una lista.

    temp_list.sort(reverse=True, key=lambda item: item[1])                                              # Ordena la lista tomando el valor en el index 1.

    max_value = temp_list[0][1]                                                                         # Ingresa el valor maximo.
    total = 0
    count = 0

    for values in temp_list:                                                                            # Suma el total de ingresos de todo.
        total = total + int(values[1])
    
    total_percent = (80 * total) / 100                                                                  # Calcula el 80% del total.
    print("Total de Ingresos: $", total)                                                                # Imprime el total.
    print("80'%' de ingresos: $", total_percent, "\n")                                                  # Imprime el 80% del total.

    printable = True
    for row, item in enumerate(temp_list):                                                              # Imprime la lista. Enumerable para agregar el index.
        
        count = count + int(item[1])                                                                    # Cuenta el total de ingresos impreso.

        if count > total_percent and printable == True:                                                 # Si contador sobrepasa al porcentaje total imprime un separador.
            printable = False                                                                           # Variable para solo imprimir una vez.
            print("# ----------------- [-80% ] ----------------- #","\n")
        
        print(row + 1, ".-", item[0])
        print_bar(item[1], max_value, prefix="^ $", suffix="ingresos generados")
        print()
        

        