# PROGRAMA DE REGISTRO DE GASTOS DIARIOS
#
# La finalidad del programa es de tener un registro de los gastos del usuario, pidiendo que
# ingrese los datos requeridos y categorizando de una manera conveniente cada gasto. Se añade a
# una versión anterior la capacidad de tener multiples entradas de gastos.
#
# ################## PSEUDOCÓDIGO ########################

# MOSTRAR mensaje de bienvenida
# LEER nombre del usuario
# MOSTRAR menú principal con opciones:
#   1 - Registrar un gasto
#   2 - Consultar un gasto
#   3 - Salir
#
# MIENTRAS el usuario no elija salir:
#   SI elige registrar un gasto:
#       LEER monto, categoría, descripción, día, mes, año
#       MOSTRAR los datos ingresados
#       PREGUNTAR si los datos son correctos
#       SI es correcto:
#           ALMACENAR el gasto como un diccionario en una lista
#       SI NO es correcto:
#           VOLVER a pedir los datos
#
#   SI elige consultar un gasto:
#       MOSTRAR submenú:
#           1 - Por fecha específica
#           2 - Por mes
#           3 - Por año
#           4 - Por categoría
#           5 - Ver gasto total
#           (Otra tecla: volver al menú principal)
#
#       SEGÚN la opción elegida:
#           LEER el valor a buscar (fecha, mes, año, categoría)
#           PREGUNTAR si es correcto
#           SI es correcto:
#               RECORRER la lista de gastos
#               MOSTRAR los que coinciden con el criterio
#               SI no se encuentra nada, MOSTRAR mensaje correspondiente
#
#           SI elige ver gasto total:
#               CALCULAR la suma total de los montos
#               MOSTRAR la cantidad de gastos, el total y el promedio
#
#   SI elige salir:
#       TERMINAR el programa
#
#   SI NO:
#       MOSTRAR mensaje de error por opción inválida

# Bienvenida al programa
print("Hola, bienvenido a REVI, tu ayudante para registrar y revisar tus gastos!")

# Ingreso de nombre del usuario
nombre_usuario = input("Me dirías tu nombre? ")

# Ingreso al menú de opciones
print(f"Un placer {nombre_usuario}! Por favor selecciona una opción para continuar:")

gastos_lista = [] #lista donde se van a almacenar los datos

# Inicio de bucle para el menú
while True:
    print("1 -Registrar un gasto")
    print("2 -Consultar un gasto")
    print("3 -Salir")
    seleccion = input("Ingrese su elección (1, 2 o 3): ")

# Registro de gasto
    if seleccion == "1":
        while True :
            gasto = {"Monto" : float(input("Ingrese el monto gastado (ej.: 210.50): ")),
                          "Categoría" : input("A qué categoría pertenece este gasto? "),
                          "Descripción" : input("Describa en qué se gastó: "),
                          "Fecha 1" : input("Día (ej.: 07): "),
                          "Fecha 2" : input("Mes (ej.: 03): "),
                          "Fecha 3" : input("Año (ej.: 2021): ")}
            correccion = input(f"El gasto ingresado es: {gasto}.\n"
                                   f"Esto es correcto? (S/N): ")
            if correccion.lower() == "s" :
                    gastos_lista.append(gasto)
                    print("Gasto registrado!")
                    break
            elif correccion.lower() == "n" :
                print("Ingrese el gasto nuevamente")
            else:
                print("Qué desea hacer a continuación?")
                break

    #Submenu consulta de gastos
    elif seleccion == "2":
        while True:
            print("Seleccione una opción:")
            print("1 -Consultar gasto por fecha específica")
            print("2 -Consultar gasto por mes")
            print("3 -Consultar gasto por año")
            print("4 -Consultar gasto por categoría")
            print("5 -Consultar gasto total")
            print("Volver al menú anterior: presione cualquier otra tecla")
            sel_2 = input("Ingrese su elección: ")

            #Mostrar gasto x fecha específica
            if sel_2 == "1" :
                fecha_dia = input("Ingrese el día (ej.: 03): ")
                fecha_mes = input("Ingrese el mes (ej.: 07): ")
                fecha_anio = input("Ingrese el año (ej.: 2019): ")
                correccion = input(f"La fecha seleccionada es: "
                                   f"{fecha_dia}/{fecha_mes}/{fecha_anio}.\n"
                                    f"Esto es correcto? (S/N): ")
                if correccion.lower() == "s" :
                    for gasto in gastos_lista:
                        encontrado = False
                        if (gasto["Fecha 1"] == fecha_dia and
                            gasto["Fecha 2"] == fecha_mes and
                            gasto["Fecha 3"] == fecha_anio):
                            print(f"{gasto}\n")
                            encontrado = True
                        elif not encontrado:
                            print("No se encontraron gastos para esa fecha.")
                elif correccion.lower() == "n" :
                    print("Ingrese la fecha nuevamente por favor")
                else:
                    break

            #Mostrar gasto x mes
            elif sel_2 == "2" :
                fecha_mes = input("Ingrese el mes (ej.: 07): ")
                correccion = input(f"El mes seleccionado es: {fecha_mes}.\n"
                                    f"Esto es correcto? (S/N): ")
                if correccion.lower() == "s" :
                    for gasto in gastos_lista:
                        encontrado = False
                        if gasto["Fecha 2"] == fecha_mes :
                            print(gasto)
                            encontrado = True
                        elif not encontrado:
                            print("No se encontraron gastos en ese mes.")
                elif correccion.lower() == "n" :
                    print("Ingrese el mes nuevamente por favor")
                else:
                    break

            #Mostrar gasto x año
            elif sel_2 == "3":
                fecha_anio = input("Ingrese el año (ej.: 2019): ")
                correccion = input(f"El año seleccionado es: {fecha_anio}.\n"
                                    f"Esto es correcto? (S/N): ")
                if correccion.lower() == "s" :
                    encontrado = False
                    for gasto in gastos_lista:
                        if gasto["Fecha 3"] == fecha_anio:
                            print(gasto)
                            encontrado = True
                        elif not encontrado:
                            print("No se encontraron gastos es ese año.")
                elif correccion.lower() == "n" :
                    print("Ingrese el año nuevamente por favor")
                else:
                    break

            #Mostrar gasto x categoría
            elif sel_2 == "4":
                categoria = input("Ingrese la categoría a consultar: ")
                correccion = input(f"Usted ha seleccionado: {categoria}."
                                    f"Esto es correcto? (S/N): ")
                if correccion.lower() == "s" :
                    encontrado = False
                    for gasto in gastos_lista:
                        if gasto["Categoría"] == categoria :
                            print(gasto)
                            encontrado = True
                        elif not encontrado:
                            print("No se encontraron gastos para esa categoría.")
                elif correccion.lower() == "n" :
                    print("Ingrese la categoría nuevamente por favor")
                else:
                    break

            #Mostrar gasto total
            elif sel_2 == "5":
                total = sum(gasto["Monto"] for gasto in gastos_lista)
                print(f"Hay {len(gastos_lista)} anotados")
                print(f"El total de gastos es de : ${total}")
                print("El gasto promedio es de : $", total / len(gastos_lista))

            #Volver al menú anterior
            else:
                break

    #Salir del programa
    elif seleccion == "3":
        break

    #Opción incorrecta
    else:
        print("Opción inválida, por favor seleccione 1, 2 o 3.")