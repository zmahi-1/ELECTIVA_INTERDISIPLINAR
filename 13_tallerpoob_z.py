
# equipos = []

# with open("equipos.txt", "w") as archivo:
#     for i in range(4):
#         nom_equipo = input("Ingrese el nombre del equipo: ")
#         cantidad = int(input("Ingrese la cantidad de unidades: "))
#         valor_und = float(input("Ingrese el valor de la unidad: "))
        
#         equipo = {  # Aqui creamos un diccionario para cada equipo
#             "nombre": nom_equipo,
#             "cantidad": cantidad,
#             "valor_unitario": valor_und
#         }
#         equipos.append(equipo)  # Aqui agregamos a la lista los diccionarios que creamos en el bucle 
        
#         # Aqui escribimos en el archivo la lista de diccionarios que creamos
#         archivo.write(str(equipo["nombre"] + "," + str(equipo["cantidad"]) + "," + str(equipo["valor_unitario"]) + "\n"))

# total_general = 0

# with open("equipos.txt", "r") as archivo:
#     for linea in archivo:
#         datos = linea.strip().split(",")
#         nom_equipo = datos[0]
#         cantidad = int(datos[1])
#         valor_und = float(datos[2])
        
#         total = cantidad * valor_und  # Aqui calculamos el total de cada equipo
#         total_general += total        # Aqui acumulamos correctamente el total general
        
#         print(f"El producto {nom_equipo} tiene un total de {total}")

#         if total > 2000000:  # Muestre los equipos que superen el valor de 2 millones
#             print(f"El equipo {nom_equipo} supera el valor de 2 millones, total: {total}")

# print(f"Valor total de todos los equipos: ${total_general}")  # Aqui mostramos el total de todos los equipos



class Dispositivo:
    def __init__(self, nombre, marca, precio):
        self.nombre = nombre
        self.marca = marca
        self.precio = precio

    # mostramos la info básica del dispositivo 
    def mostrar_info(self):
        print(f"{self.nombre} {self.marca} ${self.precio}")

    # Método 
    def calcular_descuento(self, porcentaje): 
        return self.precio - (self.precio * porcentaje)

class Computador(Dispositivo): ## objeto que hereda de la clase Dispositivo
    def __init__(self, nombre, marca, precio, memoria_ram, estado):
        super().__init__(nombre, marca, precio)
        self.memoria_ram = memoria_ram
        
        # Validamos de una vez el 
        if estado in ["Disponible", "Prestado"]:
            self.__estado = estado
        else:
            self.__estado = "Disponible"
            print(f"Error inicial: '{estado}' no es válido. Se asignó 'Disponible'.")

    # Método segun  validación
    def cambiar_estado(self, nuevo):
        if nuevo in ["Disponible", "Prestado"]:
            self.__estado = nuevo
        else:
            print(f"Error: '{nuevo}' no es válido. Solo Disponible o Prestado.")

    # Getter 
    def consultar_estado(self):
        return self.__estado

    # cambiamos  el método para mostrar toda la info 
        print(f"Computador: {self.nombre} Marca: {self.marca} Precio: ${self.precio} RAM: {self.memoria_ram}GB Estado: {self.__estado}")

    # si tiene 16GB de RAM o más
    def tiene_16_o_mas(self):
        return self.memoria_ram >= 16



pc1 = Computador("Gamer Asus", "Asus", 3500000, 16, "Disponible")
pc2 = Computador("Oficina Lenovo", "Lenovo", 2000000, 8, "Disponible")


pc1.mostrar_info()
print("¿16GB o más?", pc1.tiene_16_o_mas())


pc2.mostrar_info()
print("¿16GB o más?", pc2.tiene_16_o_mas())


# setter
print("\nCambiando PC1 a Prestado:")
pc1.cambiar_estado("Prestado")
print("Estado actual:", pc1.consultar_estado())


print("\nIntentando poner estado 'Dañado':")
pc1.cambiar_estado("Dañado")
print("Estado actual:", pc1.consultar_estado())


# descuento al computador 1
print(f"\nPrecio con 10% descuento en PC1: ${pc1.calcular_descuento(0.10)}")