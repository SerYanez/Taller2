# PROGRAMA DE REGISTRO DE GASTOS DIARIOS
#
# La finalidad del programa es de tener un registro de los gastos del usuario, pidiendo que
# ingrese los datos requeridos y categorizando de una manera conveniente cada gasto. Se añade a
# una versión anterior la capacidad de tener multiples entradas de gastos.
#
#################### Pseudocódigo #########################
#
#
#
#
#
from re import match

# Bienvenida al programa
print("Hola, bienvenido a REVI, tu ayudante para registrar y revisar tus gastos!")

# Ingreso de nombre del usuario
nombre_usuario = input("Me dirías tu nombre? ")

# Ingreso al menú de opciones
print(f"Un placer {nombre_usuario}! Por favor selecciona una opción para continuar:")
# Inicio de bucle para el menú
while True:
    print("1 -Registrar un gasto")
    print("2 -Consultar un gasto")
    print("3 -Salir")
    seleccion = int(input("Ingrese su elección: "))

    if seleccion == 1:
        gasto = {"Monto" : float(input("Ingrese el monto gastado:")),
                  "Categoría" : input("A qué categoría pertenece este gasto? "),
                  "Descripción" : input("Describa en qué se gastó: "),
                  "Fecha 1" : int(input("Día (ej.: 07): ")),
                  "Fecha 2" : int(input("Mes (ej.: 11): ")),
                  "Fecha 3" : int(input("Año (ej.: 2021):"))}
        print("Gasto registrado!")
        print("Qué desea hacer a continuación?")
    elif seleccion == 2:
        while True:
            print("Seleccione una opción:")
            print("1 -Consultar gasto por fecha")
            print("2 -Consultar gasto por categoría")
            print("3 -Consultar gasto total")
            sel_2 = int(input("Ingrese su elección: "))
    elif seleccion == 3:
        break
    else:
        print("Opción inválida, por favor seleccione 1, 2 o 3.")






#print()#Opción 1: registrar un gasto
#print()#Opción 2: consultar un gasto
#        print()#Opción 2.1: consultar gasto por fecha
#                print()#Opción 2.1.1: consultar gasto por mes
#                print()#Opción 2.1.2: consultar gasto por año
#        print()#Opción 2.2: consultar gasto por categoría
#        print()#Opción 2.3: consultar gasto total

print("Quisieras hacer alguna otra consulta? Sí/No ")#Mensaje de vuelta al bucle o fin de programa