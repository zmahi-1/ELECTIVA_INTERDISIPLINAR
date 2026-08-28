print("_______ INGRESE LOS SIGUIENTES DATOS________")
nombrecliente = input( "Nombre del Cliente")
producto= input("Producto")
precioun= float(input("Precio unitario ")) # FLOAT, COMO EL INPUT RECIBEL EL DATO Y LO MANDA STL, EL FLOAT LO DEJA EN DECIMAL LO VUELVE DECIMAL 
cantidad=int(input("Cantidad"))

total= precioun*cantidad

print("_______ RESUMEN DE COMPRA________")
print("Nombre: ", nombrecliente)
print("Producto: ",producto)
print("Cantidad: ",cantidad)
print("Precio unidad: ",precioun)
print("Total compra: ",total)






print("_______ INGRESE LOS SIGUIENTES DATOS________")
nombre = input( "Nombre:      ") # STRING, COMO EL INPUT RECIBEL EL DATO Y LO MANDA STL, EL STRING LO DEJA EN TEXTO LO VUELVE TEXTO")
edad = int(input("Edad:      ")) # INT, COMO EL INPUT RECIBEL EL DATO Y LO MANDA STL, EL INT LO DEJA EN ENTERO LO VUELVE ENTERO
temperaturacorporal= float(input("Temperatura Corporal    ")) # FLOAT, COMO EL INPUT RECIBEL EL DATO Y LO MANDA STL, EL FLOAT LO DEJA EN DECIMAL LO VUELVE DECIMAL"))
nota=float(input("Nota de 0.0 a 5.0       ")) # FLOAT, COMO EL INPUT RECIBEL EL DATO Y LO MANDA STL, EL FLOAT LO DEJA EN DECIMAL LO VUELVE DECIMAL 
carnet=(input(" ¿TIENE CARNET? Si o no    ")) # STRING, COMO EL INPUT RECIBEL EL DATO Y LO MANDA STL, EL STRING LO DEJA EN TEXTO LO VUELVE TEXTO")
print("___________________________________")
mayor_edad = edad>=18
temp_adecuada =  temperaturacorporal== 37.5
cap_aprovada = nota>=0.0 and nota<=5.0
tiene_carnet = carnet== "si"
cumple_requisitos= mayor_edad and temp_adecuada and cap_aprovada and tiene_carnet
 
print("CUMPLE REQUISO DE INGRESO ",     cumple_requisitos)
print("___________________________________")
print("ES MAYOR DE EDAD: ",             mayor_edad)
print("TIENE TEMPERATURA NORMAL: ",     temp_adecuada)
print("TIENE NOTA VALIDA: ",            cap_aprovada)
print("TIENE CARNET: ",                 tiene_carnet)



