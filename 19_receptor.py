import serial
from time import sleep

puerto= serial.Serial("COM10", 115200, timeout=3) #COM10 es el puerto, 115200 es la velocidad de comunicacion
sleep(3)

puerto.reset_input_buffer()

while True: #ciclo infinito
    dato = puerto.readline().decode().strip() #lee el dato enviado desde la tarjeta y elimina el salto de línea al final

    if dato:
        distancia = float(dato) #convierte el dato a float
        print("Distancia medida:", distancia, "cm") #muestra la distancia en la terminal
