# # class producto:
# #     def __init__(self,nombre,cantidad):
# #         self.nombre=nombre
# #         self.cantidad=cantidad
# #     def agregar_stock(self, unidades):
# #         self.cantidad += unidades
# # teclado=producto("teclado",3)        
# # celular=producto("celular",2)
# # mouse=producto("mouse",5)
# # monitor=producto("monitor",2)
# # mouse.agregar_stock(4) 
# # print(celular.cantidad)
# # print(mouse.cantidad)
# # print(monitor.cantidad)
# # print(teclado.cantidad)

# ##  atributos vs parametros, no todo dato usado por un metodo debe guardarse como atributo 

# # class producto:
# #     def __init__(self,nombre,precio): #los atributos son variables y guardan en la clase, los parametros son variables que se usan, metodo
# #         self.nombre=nombre
# #         self.precio=precio
# #     def agregar_stock(self, unidades):
# #         self.precio += unidades
# #     def calcular_total(self, cantidad):
# #         return self.precio * cantidad
    
# # teclado=producto("teclado",20000)        
# # celular=producto("celular",35000)
# # mouse=producto("mouse",5000)
# # monitor=producto("monitor",23000)
# # #mouse.agregar_stock(4) 
# # #mouse.calcular_total(5)
# # # print(teclado.calcular_total(2))
# # # print(celular.calcular_total(3))
# # print(mouse.calcular_total(7))
# #print(monitor.calcular_total(7))
# #DICCIONARIO VS METODO 
# ## self toma el valor del objeto que usamosn ene le momento
# ## crear clase completa
# #1 atributso y parametros que vana a tener los objetos de la clase, 
# ## cuando ya tenemos claes, metodo y atributos, podemos crear objetos de la clase, cada objeto tiene sus propios atributos y metodos, los objetos
# class producto:
#     def __init__(self,nombre,precio,cantidad): #parametrso (nombre...)los atributos son variables y guardan en la clase, los parametros son variables que se usan, metodo
#         self.nombre=nombre #self. nombre es atributo, nombre es parametro
#         self.precio=precio
#         self.cantidad=cantidad
# #def dentro de clase es metodo, def fuera de clase es funcion
#     def mostrar_datos(self):
#         return f"{self.nombre}-{self.precio}-{self.cantidad}"
    
#     def calcular_total(self):
#         return self.precio * self.cantidad

# teclado=producto("teclado",20000,3)        
# celular=producto("celular",35000,2)
# mouse=producto("mouse",5000,5)
# monitor=producto("monitor",23000,2)
# #mouse.agregar_stock(4) 
# #mouse.calcular_total(5)
# # print(teclado.calcular_total(2))
# # print(celular.calcular_total(3))
# print (mouse.calcular_total())

##Reto
class cuenta_bancaria:
    def __init__(self,titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def consultar_saldo(self):
        return self.saldo    
    
    def depositar(self,monto):
        self.saldo += monto
        return self.saldo
    
    def retirar(self,monto):
        if monto <= self.saldo:
            self.saldo -= monto
            return self.saldo
        else:
            print("Saldo insuficiente")
    def mostrar_datos(self):
        return f"Titular:{self.titular}, Saldo:{self.saldo}"
cuenta1 = cuenta_bancaria("Carlos", 1000000)
cuenta2= cuenta_bancaria("Ana", 50000)

cuenta1.depositar(50000)
cuenta2.retirar(30000)
cuenta2.retirar(60000)
print(cuenta1.mostrar_datos())
print(cuenta2.mostrar_datos())