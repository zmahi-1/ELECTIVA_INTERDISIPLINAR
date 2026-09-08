# total = 0
# for vueltas in range(4):
#      numero = int(input("numero: "))
#      total = total + numero
# print ("Numero:", numero)     

# contador = 0
# suma = 0 
# for numero in range (1,11):
#     if numero % 2 == 0:
#         contador += 1
#         suma += numero
# print("cantidad de pares :", contador)    
# print("suma de pares :" , suma )  




# for numero in range (1,8 ):
#     if numero ==4:
#         print(numero)


# texto = "Hola"

# for letra in texto:
#     print("letra: ", letra)

# texto = "Area Tecnica"
# texto = texto.lower()
# for letra in "aeiouáéíóú":
#     cantidad = texto.count(letra)

# texto = "Python" ## en paiton numera desde el cero, sirve para los indicies, para ubicar mas facilmente las letras de una palabra, y tambien sirve para hacer rebanadas de palabras, es decir, cortar palabras en partes.

# len(texto) #6
# texto[0] #P
# texto[-1] #n
# texto[0:3] #Pyt
# texto[::-1] #thon


# ##listas 

# notas = [4.5, 3.8, 5.0, 2.9] #las listas usan corchetes 
# print(notas[0]) #4.5
# print(notas[-1]) #5.0 en tonces menos uno es de derecha aizquierda 
# print(len (notas)) #5 aqui cuenta la cantidsad de elementos que hay en la lista, en este caso 5


# notas = [4.5, 3.0, 5.0]
# for nota in notas:
#     print("nota:", nota) 

# suma = 0
# for nota in notas:
#     suma += nota
# promedio = suma / len(notas)
# print("Promedio:", promedio)

# notas = []
# for vueltas in range(3):
#     nota = float(input("Ingrese la nota: "))
#     notas.append(nota) #append sirve para agregar elementos a la lista  

# print(notas) #imprime denro de corchetes, es decir, como una lista

# frutas = ["manzana", "pera", "uva"]

# frutas [1] = "mango" #aqui se reemplaza el elemento de la lista, en este caso la pera por naranja
# # [manzana, "mango", uva]

# frutas.remove("uva") #aqui se elimina el elemento de la lista, en este caso la uva, mirar que elimina 
# #elimina por valor 

# eliminado = frutas.pop(0) #aqui se elimina el elemento de la lista
# print("Elemento eliminado:", eliminado)

# numeros = [30,10,40,20 ]

# numeros.sort() #aqui se ordena la lista de menor a mayor, sin que modifique posicion si se quiere de mayor a menor se pone reverse = True
# print(numeros) # [20, 10, 30, 40]
# ordenada=sorted (numeros) #ordena asendente y cambia los indices, si llamo print numeros saca una y print ordenada con la otra
# print(ordenada) # [10, 20, 30, 40]
# numeros.reverse() #aqui se invierte el orden de la lista, es decir, de derecha a izquierda, sin modificar posicion, si se quiere de mayor a menor se pone reverse = True
# print(numeros) # [40, 30, 20, 10]
# numeros.count(20) #aqui se cuenta cuantas veces aparece el elemento en la lista, en este caso el 10, si no aparece devuelve 0
# print(numeros.count(20)) #1
# numeros.index(40) #aqui se busca el indice del elemento en la lista, en este caso el 30, si no aparece devuelve un error
# print(numeros.index(40)) #3


# nombres = ["Ana", "Luis", "Carlos"]
# for i in range(len(nombres)):
#     print("Estudiante:", i+1, ":", nombres[i])    #numerando

# notas = [2.5, 3.0, 4.0] # este prgrama cambia la notas seguncondicion, entonces, si es menor a 3.0, la cambia a 3.0, si es mayor a 3.0
# for i in range(len(notas)):
#     if notas[i] < 3.0:
#         notas[i] = 3.0 

# print("Notas:", notas)

#Lista anidada
# estudiantes = [
#     ["Ana", 4.5], # esto es una lista 0
#     ["Luis", 3.0], #1
#     ["Carlos", 2.5] #2 corchetes independiente
# ] # una posicion guarda dos datos
# print(estudiantes)
# print(estudiantes[0]) # Ana
# for estudiante in estudiantes:
#     print(estudiante[0], estudiante[1]) # Ana 4.5

estdudiantes = [
    ["Ana", [4.0, 3.5, 5.0]],   # esto es una lista 0
    ["Luis", [2.8, 3.0, 4.2]],   #1
]

for estudiante in estdudiantes:
    suma=0
    for nota in estudiante[1]:
        suma += nota
    promedio = suma / len(estudiante[1])
    print("Estudiante:", estudiante[0], "Promedio:", round(promedio, 2))