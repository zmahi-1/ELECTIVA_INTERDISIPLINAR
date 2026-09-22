# def presentar (nombre, edad):
#     print("Nombre:", nombre)
#     print("Edad:", edad)

# presentar("Laura",22)

##print muestra, return devuelve 

# def sumar (a,b):
#     print (a+b)
# resultado = sumar(5,3)
# print(resultado)
# ##retur le entrega datos al programa 
# def sumar (a,b):
#     return a+b
# resultado = sumar(5,3)
# print(resultado)

# def multiplicar (a,b): ## entre parentesis se colocan los parametros que se van a recibir, en este caso a y b
#     return a*b  ## almacena el 20 para luego sumarle 10 y mostrar el resultado final
# resultado= multiplicar(4,5)+10 ## 4 y 5 evitar lineas de codigo, primero multiplica y luego le suma 10
# print(resultado)

# def calcular_promedio (notas): ## genera variable 
#     suma=0
#     for nota in notas: 
#         suma += nota ## acumula las notas
#     return suma/len(notas) ## suma de las notas entre la cantidad de notas que hay en la lista

# notas_ana=[4.0, 3,5, 5.0]
# promedio = calcular_promedio(notas_ana)
# print(round(promedio,2)) ## redondea el promedio a 2 decimales, rund es una funcion que redondea un numero a la cantidad de decimales que se le indique, en este caso 2

## ambito de variables, donde las variable se crean se puden usar, si se crean dentro de una funcion no se pueden usar fuera de la funcion, si se crean fuera de la funcion se pueden usar dentro de la funcion.

# def calcular ():
#     resultado = 20
#     print (resultado)

# calcular ()
# print (resultado) ## genera error porque la variable resultado se creo dentro de la funcion calcular y no se puede usar fuera de la funcion 

## variable global debe estar por fuuera y la identacion nivel 1 

# nombre="laura"

# def saludar():
#     print (nombre)

# saludar()
## esta variable esta global, pero la quiero renombrar, como es global no se puede cambiar el valor
#contador = 10

# def aumentar ():
#     contador=contador+1
#     print(contador)


# aumentar()


# def aumentar (numero): ## la variable es numero
#     return numero +1 
# contador=10
# contador=aumentar(contador) ## aurgumento 
# print(contador)

#ejercicio 1

# def calcular_total(precio,cantidad): ## def define funcio, precio y cantidad, paramatreos, nombre de funcion es calcular 
#     return precio*cantidad ## devuelve una operacion
# ##diccionario
# producto ={ ## nombre, preio y cantidad son las claves
#     "nombre":"teclado",
#     "precio":80000,
#     "cantidad": 3
# }

# producto ["total"] = calcular_total (
#     producto["precio"],
#     producto["cantidad"]
# )
# print(producto)

## CORREGUIR CODIGO

# puntos=5
# def sumar_puntos():
#     puntos=puntos +10
#     print (puntos)
#sumar_puntos()

# def sumar_puntos (puntos):
#     return puntos +10

# puntos=5
# puntos=sumar_puntos (puntos)
# print (puntos)

## TALLER DE CLASE
## crear una funcion calcular_promedio(notas) que devuelva el promedio de notas de una lista

estudiantes=[
    {"nombre":"Ana", "nota":[4.0,3.5,5.0]},  
    {"nombre":"Luis", "nota":[2.5,3.0,2.8]},
    {"nombre":"Carlos", "nota":[4.5,4.0,4.8]}
]
def calcular_promedio(notas):
    suma=0
    promedio=sum(notas)/len(notas)
    return promedio
    promdioestudiantes =calcular_promedio(estudiante[1]["nota"])
    print(round(promedioestudiantes,2))
for estudiante in estudiantes:
    promedio = calcular_promedio(estudiante["nota"]) 
    if promedio>=3.0:
        estado = "Aprobado"
    else:
        estado = "No aprobado"

    estudiante["promedio"]=round(promedio,2)
    estudiante["estado"]=estado    
print(estudiantes)