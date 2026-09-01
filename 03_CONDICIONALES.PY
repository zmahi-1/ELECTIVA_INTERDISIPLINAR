print("___________________________________")
print("EJERCICIO 1")

edad = 20
if edad >= 18:
    print("mayor de edad") #evalua la condicio, si es verdadera ejecuta el print, si es falsa no hace nada
    print ("Bienvenido") #identacion, son los niveles de sangria, si no se hace la identacion el programa no funciona, el print es parte del if, si no se hace la identacion el print no es parte del if

if edad >=18:
    print("Puede ingresar")
print("___________________________________")
print("EJERCICIO 2")
nota = 4.0
if nota >= 3.0:
    print("Aprobado")
else:
    print("No aprobado")

print("___________________________________")
print("EJERCICIO 3")


nota = 4.3

if nota <= 3.0:
    print("Insuficiente")
elif nota < 4.0:
    print("Básico")
elif nota < 4.6:
    print("Alto")
else:
    print("Superior")

print("___________________________________")
print("EJERCICIO 4")


nota= 4.8
if nota >= 3.0:
    print("Aprobado")  
elif nota >= 4.5:
        print("Excelente")

print("___________________________________") ## orden importa porque si nno se salta las instruccuines 

print("EJERCICIO 5")

nota = float(input("Nota "))
if nota < 0 or nota > 5:    
    print("Nota no valida")
elif nota < 3:
    print("Insuficiente")
elif nota < 4:
    print("Básico")
elif nota < 4.6:
    print("Alto")
else:
    print("Superior")   

print("___________________________________")
print("EJERCICIO 6")

edad = 22
carnet = True
if edad >= 18 and carnet:   
    print("Puede ingresar")

# IF ANIDADO 
edad = 25
matricula = "si"
contraseña = "azul21"
if edad < 18:
    print("acceso restringido")
else:
    if matricula == "si": ## este if pertenece al else del if anterior si no se cumpple baja al else de ni matricula
            if contraseña == "azul21":
                print("Bienvenido")
            else:
                print("Contraseña incorrecta")
    else:
            print("No matriculado")

 ## EJERCCICIO DE SISTEMA DE ACCESO   
print("EJERCICIO 7")      
print("___________________________________")
print("_______ Sistema de acceso  ________")

nombre = input("Nombre:            ")
edad = int(input("Edad:            "))
invitacion = input("¿Tiene invitación? (si/no):         ") ##Hats aqui ingresa los datos 
invitacion= invitacion.lower() ## lower() convierte a minuscula el string, para que no importe si el usuario ingresa SI, Si, sI, si
if edad >= 18:
    if invitacion == "si": 
        print("Acceso permitido. Bienvenido, ", nombre)
    else:
        print("Acceso denegado. Se requiere invitación.") 
  ## uso del if anidado porque por booleano, solo tomaria la opcion de si 
else:
    print("Acceso denegado.")

print("___________________________________")
print("EJERCICIO 9")


numero = 1 
while numero <= 5:
    print("Número:", numero)
    numero = numero + 1  # Incrementa el número en 1

print("___________________________________")
##contador
contador = 1 
while contador <= 5:
    print("Número:", contador)
    contador = contador + 1  # Incrementa el número en 1
print("___________________________________") ##aqui se va infinito, porque no hay una condicion
numero=1
while numero <= 3:
    print("Número:", numero)
print("___________________________________") ## para deterne el ciclo, ctrl + c en la terminal 

contraseña ="" ## por se una contraseña, mejor no usar el.
while contraseña != "python":
    contraseña = input("contraseña: ")
print("Bienvenido")

print("___________________________________")
print("EJERCICIO 9")

contraseña ="" 
intentos = 0

while contraseña != "python" and intentos < 3:
    contraseña = input("contraseña: ")
    intentos = intentos + 1  # Incrementa el contador de intentos   
if contraseña == "python":
    print("ACCESO AUTORIZADO")
else:
    print("ACCESO BLOQUEADO")

print("___________________________________")
print("PIN DE CAJERO")

 #pin = "2580"
pin= " "
intentos = 0

while pin != "2580" and intentos < 3: ## se guarda el pin como str porque los ceros en el nicio python no lo detecta
    pin = input("PIN: ")
    intentos = intentos + 1  # Incrementa el contador de intentos   
if pin == "2580":
        print("Acceso a la cuenta.")
else:
    print("Tarjeta Bloqueada.")


