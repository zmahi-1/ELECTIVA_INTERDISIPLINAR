# # Parte B   MANEJO DE ARCHIVOS 


# productos  = []

# # with open("productos.txt", "w") as archivo:
# #     for i in range(3):
# #         nombre = input("Producto: ")
# #         cantidad = int(input("Ingrese la cantidad: "))
# #         precioun = float(input("ingrese el precio unitario:"))

# #         archivo.write(f"{nombre},{cantidad},{precioun} \n")


# total=0

# with open ("productos.txt","r") as archivo:
#     for linea in archivo:
#         informacion = linea.strip().split(",")
#         nombre= informacion[0]
#         cantidad = int(informacion[1])
#         precioun= float(informacion[2])

#         totalun = cantidad * precioun
#         total += totalun


#         print(f"{nombre} = $ {precioun} *{cantidad}  und,= subtotal de {totalun}")

# print("------------------------------------")
# print("Total general")
# print(f"Valor total de todos los productos: ${total}")




## PARTE C POO

class Dispositivo:
    def __init__(self, nombre, marca, precio):
        self.nombre = nombre
        self.marca = marca
        self.precio = precio

    def mostrar_info(self):
        print(f"{self.nombre} {self.marca} ${self.precio}")

    def calcular_descuento(self, porcentaje): 
        return self.precio - (self.precio * porcentaje)

class Sensor(Dispositivo):
    def __init__(self, nombre, marca, precio, tipo, unidad,estado):
        super().__init__(nombre, marca, precio)
        self.__tipo= tipo
        self.unidad= unidad

    def consultar_estado (self):
        return self.__estado

    print(f"El estao del sensor es: {estado}")

    if estado in ["Activo", "Inactivo"]:
            self.__estado = estado
