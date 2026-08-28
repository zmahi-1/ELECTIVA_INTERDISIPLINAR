print("_______ INGRESE LOS SIGUIENTES DATOS________")
nombre = input( "Nombre:      ") # STRING, COMO EL INPUT RECIBEL EL DATO Y LO MANDA STL, EL STRING LO DEJA EN TEXTO LO VUELVE TEXTO")
edad = int(input("Edad:      ")) # INT, COMO EL INPUT RECIBEL EL DATO Y LO MANDA STL, EL INT LO DEJA EN ENTERO LO VUELVE ENTERO
temperaturacorporal= float(input("Temperatura Corporal    ")) # FLOAT, COMO EL INPUT RECIBEL EL DATO Y LO MANDA STL, EL FLOAT LO DEJA EN DECIMAL LO VUELVE DECIMAL"))
nota=float(input("Nota de 0.0 a 5.0       ")) # FLOAT, COMO EL INPUT RECIBEL EL DATO Y LO MANDA STL, EL FLOAT LO DEJA EN DECIMAL LO VUELVE DECIMAL 
carnet=(input(" ¿TIENE CARNET? Si o no    ")) # STRING, COMO EL INPUT RECIBEL EL DATO Y LO MANDA STL, EL STRING LO DEJA EN TEXTO LO VUELVE TEXTO")
print("___________________________________")

mayor = edad>=18
tem =  temperaturacorporal== 37.5
notain = nota>=0.0 and nota<=5.0
ingreso = carnet== "si"
cr= mayor and tem and notain and ingreso
 
print("CUMPLE REQUISO DE INGRESO ",     cr)
print("___________________________________")
print("ES MAYOR DE EDAD: ",             mayor)
print("TIENE TEMPERATURA NORMAL: ",     tem)
print("TIENE NOTA VALIDA: ",            notain)
print("TIENE CARNET: ",                 ingreso)



