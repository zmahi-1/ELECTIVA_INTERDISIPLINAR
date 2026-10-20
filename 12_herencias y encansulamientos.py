# ##clase padrres herada a clase hija
# ## pass, nos deja ejecutar sin necesiad de tener codigo
# class Persona: 
#     def __init__(self, nombre): # debe estar el self, el nombre es un parametro, el parametro asigna un valor 
#         self.nombre = nombre # guarga el valoor dentro del objeto

#     def saludar (self):
#         return f("Hola, soy {self.nombre}")
# ##persona tiene contructor, tiene metodo, estuddiante no agrega nada pero hereda lo de persona 
# class Estudiante(Persona): #hereda de la clase persona, estudiante es una clase hija, persona es clase padre
#     ##pass
# ##agregar objeto a estudiante
# estudiante1 = Estudiante("pepito")
# print (estudiante1.saludar())

## 

# class Persona:
#     def __init__(self, nombre,):
#         self.nombre = nombre 

#     def saludar(self):
#         return (f"Hola,soy {self.nombre} ")
# class Estudiante(Persona): 
#         pass
# estudiante1 = Estudiante("Pedrito")
# print(estudiante1.saludar())

# class Persona:
#     def __init__(self, nombre, edad):
#         self.nombre = nombre
#         self.edad = edad
# ## super() llama al constructor de la clase padre, para que se ejecute el constructor de la clase padre y se inicialicen los atributos de la clase padre
# class Estudiante (Persona):
#     def __init__(self, nombre, edad, carrera):
#         super().__init__(nombre, edad)
#         self.carrera = carrera
# estudiant1 = Estudiante("pepito", 20, "Lic Tec")
# print(estudiant1.nombre)

# class Persona:
#     def __init__(self, nombre, edad):
#         self.nombre = nombre
#         self.edad = edad

# class Estudiante(Persona):
#     def __init__(self, nombre, edad, carrera,nota):
#         super().__init__(nombre, edad)
#         self.carrera = carrera
#         self.nota = nota
# estdiante1 = Estudiante("pepito", 20, "Lic Tec", 4.5)

# # estudiante1.presentarse()
# # #metodo heredado de persona 
# # estudiante1.mostrar_nota()
# # #metodo propio del estudiante
# # estudiante1.obtener_estado()
# # #metodo prpio del estudiante

# ##sobre escritura de metodos
# ## la case  hija puede redfinir un metodo hererado

# # class Persona:
# #     def presentarse(self):
# #         return "soy una persona"

# # class Estudiante(Persona):
# #     def presentarse(self):
# #         return "soy un estudiante"

# # class Estudiante:
# #     def __init__(self, nota):
# #         self.__nota = nota ## para evitar que se modifique usamos __

# #     def mostrar_nota(self):
# #         return self.__nota 
# # ##atributos publicos, y atributos privados, son niveles de proteccion, un guion advierte 2 restringe 
# # self.nota ## modificacable en cualquier parte
# # self.__nota ## solo se puede modificar dentro de la clase 


# # class Sensor:
# #     def __init__(self):
# #     self.ubicacion = "sala" #interno por convencion
# #     self.__temperatura = 25 # se controla desde metodos

# ## metodo getter y setter
# ## getter:  solo leer o consultar el atributo
# ##setter: modificar el atributo, cambiar el valor del atributo

# class Estudiante:
#     def __init__(self, nota):
#         self.__nota = nota
# ## getter 
#     def mostrar_nota(self):
#         return self.__nota
# ## setter
#     def cambiar_nota (self, nueva_nota): 
#         if  0<= nueva_nota <= 5:
#             self.__nota = nueva_nota
#     def obtener_estado(self):
#         if self.__nota >= 3:
#             return f"Aprobado: {self.__nota}"
#         else:
#             return f"Reprobado: {self.__nota}"


# ## validar antes de modificar 

# estudiante1 = Estudiante(4.5) ## estuaidante1 es on objeto de la clase estudiante
# print(estudiante1.mostrar_nota()) ##getter

# estudiante1.cambiar_nota(3.8)  ## setter
# print(estudiante1.mostrar_nota())

# estudiante1.cambiar_nota(7)  ## setter
# print(estudiante1.mostrar_nota()) ## no cambia porque no cumple la condicion del setter

# print(estudiante1.obtener_estado())
# ##dos objetos son estuidante pero aca uno su infor
# estudiante1=Estudiante("luis",34,"lic tec",4.5)
# estudiante2=Estudiante("pedro",255,"lic tec",2.8)

# print(estudiante1.obtener_estado())
# print(estudiante2.obtener_estado())

# ## se encapsula para mantener el contro, de los datos

# class Cuenta:
#     def __init__(self, titular, saldo):
#         self.titular = titular
#         self.__saldo = saldo    

#     def consultar_saldo(self):
#         return self.__saldo
    
#     def depositar(self, cantidad):
#         if cantidad > 0:
#             self.__saldo += cantidad



##ACTIVIDAD 
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad 


    def presentarse(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años."

class Estudiante(Persona):
    def __init__(self,nombre,edad,carrera,nota):
        super().__init__(nombre, edad)
        self.carrera = carrera
        self.__nota = nota
    # getter 
    def mostrar_nota(self):
        return self.__nota
    #setter
    def cambiar_nota (self, nueva_nota): 
        if  0<= nueva_nota <= 5:
            self.__nota = nueva_nota
    def obtener_estado(self):
        if self.__nota >= 3:
            return f"Aprobado: {self.__nota}"
        else:
            return f"Reprobado: {self.__nota}"

estudiante1 = Estudiante("luis", 20, "lic tec", 4.0)
print(estudiante1.presentarse())
print(estudiante1.mostrar_nota())
print(estudiante1.obtener_estado())

estudiante2 = Estudiante("ana", 18, "lic tec", 0)
print(estudiante2.presentarse())
print(estudiante2.mostrar_nota())
print(estudiante2.obtener_estado())

estudiante1.cambiar_nota(2)
print(estudiante1.presentarse())
print(estudiante1.mostrar_nota())
print(estudiante1.obtener_estado())

estudiante2.cambiar_nota(7)
print(estudiante2.presentarse())
print(estudiante2.mostrar_nota())
print(estudiante2.obtener_estado())