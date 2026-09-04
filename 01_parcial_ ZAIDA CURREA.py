# ##PUNTO 1 
# print("________________Punto 1 - A________________")
# edad=int(input("Ingrese su edad: "))
# if edad>=18:
#     print("mayor de edad")
# else:
#     print("menor de edad")

# ## El error del programa iniciale es que no se espcifica que tipo de dato se espera del usuario, por lo que al ingresar un valor no numerico el programa genera un error, para solucionarlo se puede utiliza la funcion int() para convertir el valor ingresado a un entero y asi evitar errores.

# #PUNTO 2 
# print("________________Punto 1 - B________________")
# nota=float(input("Ingrese la nota: "))
# if  nota>= 0.0 and nota<=5.0:

#     if nota>=4.5 and nota<=5.0:
#         print(" DESEMPEÑO SUPERIOR")
#     if nota >=3.0 and nota<4.5:
#         print("APROBADO")
#     if nota<3.0:
#         print("NO APROBADO")
# else:
#     print("Nota invalida")


# #PUNTO 2
# print("________________Punto 2________________")
# nota=float(input("Ingrese la nota: "))
# if  nota>= 0.0 and nota<=5.0:
#     if nota>=4.6 and nota<=5.0:
#         print(" DESEMPEÑO SUPERIOR")
#     if nota >=4.0 and nota<4.6:
#         print("DESEMPEÑO ALTO")
#     if nota >=3.0 and nota<4.0:
#         print("DESMPEÑO BASICO")
#     if nota<3.0:
#         print("NO APROBADO")
# else:
#     print("Nota invalida")


##PUNTO 3
print("________________Punto 3________________")
total_ventas = 0
cantidad_ventas = 0
opcion = 0




while opcion != 3:
    print("OPCIONES")
    print("1. Registrar venta")
    print("2. Consultar resumen")
    print("3. Finalizar")
    opcion = int(input("Seleccione una opción: "))
    
    if opcion <=0:
        print ("Valor Invalido")  
    if  opcion == 1:
        input_venta = float(input("Ingrese el valor de la venta: "))
        total_ventas = total_ventas + input_venta
        cantidad_ventas = cantidad_ventas + 1
        print("Venta registrada.", cantidad_ventas)
        print ("________________________________")
    if opcion == 2:
        print("Total de ventas: ", total_ventas)
        print("Cantidad de ventas: ", cantidad_ventas)
        print ("________________________________")
    if opcion == 3:
        print("Finalizando el programa...")
        print("Total de ventas: ", total_ventas)
        print("Cantidad de ventas: ", cantidad_ventas)
        print ("________________________________")