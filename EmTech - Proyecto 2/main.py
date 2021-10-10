from database import *                                                          # Importamos el archivo de base de datos
from functions import *                                                         # Importamos todas las funciones

while(True):                                                                    # While True para evitar que el programa finalice 
    print("Synergy Lo1gistics - Analysis")

    print("[1] 10 rutas mas demandadas. Acorde a los flujos de importación y exportación.")
    print("[2] 3 medios de transporte más importantes para Synergy logistics considerando el valor de las importaciones y exportaciones.")
    print("[3] Países que generan el '80%' del valor de las exportaciones e importaciones.")

    value = input("Selecciona el numero de operacion a realizar: ")             # Ingresar el numero de operacion a realizar.

    if (value == "1"):                                                          # Si el valor ingresado es igual a 1.
        print()
        Option_1()                                                              # > Envia a la funcion 1.

    elif (value == "2"):                                                        # Si el valor ingresado es igual a 2.
        print()
        Option_2()                                                              # > Envia a la funcion 2.
    
    elif (value == "3"):                                                        # Si el valor ingresado es igual a 3.
        print()
        Option_3()                                                              # > Envia a la funcion 3.

    else:                                                                       # Si el valor no existe.
        print("Valor no encontrado.")
    
    rst = input("¿Desea ir al inicio? y/n: ")                                   # Input para reiniciar el programa.

    if(rst == "n" or rst == "no"):                                              # Si el valor es igual a no.
        break                                                                   # Rompe el ciclo y termina el programa.
    
    elif(rst == "y" or rst == "yes"):                                           # Si el valor es igual a si.
        clear()                                                                 # Limpia la consola.
    else:
        print("Valor no encontrado.")
