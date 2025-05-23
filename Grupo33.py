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
    seleccion = int(input("Ingrese su elección: "))

    #Registro de gasto
    if seleccion == 1:
        gasto = {"Monto" : float(input("Ingrese el monto gastado:")),
                  "Categoría" : input("A qué categoría pertenece este gasto? "),
                  "Descripción" : input("Describa en qué se gastó: "),
                  "Fecha 1" : input("Día (ej.: 07): "),
                  "Fecha 2" : input("Mes (ej.: 03): "),
                  "Fecha 3" : input("Año (ej.: 2021): ")}
        gastos_lista.append(gasto)
        print("Gasto registrado!")
        print("Qué desea hacer a continuación?")

    #Submenu consulta de gastos
    elif seleccion == 2:
        while True:
            print("Seleccione una opción:")
            print("1 -Consultar gasto por fecha específica")
            print("2 -Consultar gasto por mes")
            print("3 -Consultar gasto por año")
            print("4 -Consultar gasto por categoría")
            print("5 -Consultar gasto total")
            sel_2 = int(input("Ingrese su elección: "))

            #Mostrar gasto x fecha específica
            while sel_2 == 1 :
                fecha_dia = input("Ingrese el día (ej.: 03): ")
                fecha_mes = input("Ingrese el mes (ej.: 07): ")
                fecha_anio = input("Ingrese el año (ej.: 2019): ")
                correccion = input("La fecha seleccionada es: ", fecha_dia, "/", fecha_mes, "/",
                                   fecha_anio, "Esto es correcto? (S/N): ")
                if correccion == "S" :
                    print(gastos_lista["Fecha 1" : fecha_dia, "Fecha 2" : fecha_mes,
                          "Fecha 3" : fecha_anio])
                elif correccion == "N" :
                    print("Ingrese la fecha nuevamente por favor")
                else:
                    break

            #Mostrar gasto x mes
            while sel_2 == 2 :
                fecha_mes = input("Ingrese el mes (ej.: 07): ")
                correccion = input("El mes seleccionado es: ", fecha_mes,
                "Esto es correcto? (S/N): ")
                if correccion == "S" :
                    print(gastos_lista["Fecha 2" : fecha_mes])
                elif correccion == "N" :
                    print("Ingrese la fecha nuevamente por favor")
                else:
                    break

            #Mostrar gasto x año
            while sel_2 == 3:
                fecha_anio = input("Ingrese el año (ej.: 2019): ")
                correccion = input("El mes seleccionado es: ", fecha_anio,
                                   "Esto es correcto? (S/N): ")
                if correccion == "S":
                    print(gastos_lista["Fecha 2": fecha_anio])
                elif correccion == "N":
                    print("Ingrese la fecha nuevamente por favor")
                else:
                    break



    elif seleccion == 3:
        break
    else:
        print("Opción inválida, por favor seleccione 1, 2 o 3.")