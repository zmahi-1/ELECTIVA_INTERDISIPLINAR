import serial
from time import sleep

puerto= serial.Serial("COM10", 115200, timeout=3) #COM10 es el puerto, 115200 es la velocidad de comunicacion

sleep(3)
puerto.reset_input_buffer()

while True: #ciclo infinito
    dato = puerto.readline().decode().strip() #lee el dato enviado desde la tarjeta y elimina el salto de línea al final

    try:
        distancia = float(dato) #convierte el dato a float
        print("Distancia:", distancia, "cm") #muestra la distancia en la terminal

        if distancia < 10:
            puerto.write(b"ENCENDER\n") #envia el comando para encender el led
        else:
            puerto.write(b"APAGAR\n") #envia el comando para apagar el led
    except ValueError:
        print("Dato recibido no es un número válido:", dato) #muestra un mensaje de error si el dato no es un número
