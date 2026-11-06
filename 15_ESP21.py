#primero pasa por el sensor, luego a tarjeta, 
# velocidades de comunicacion 9600, 115200, 250000, 500000, 1000000
#trabajamos con 115200 baudios, deben coincidir las vecidades
#py seria/ libreria  que permite usar el puerto serial, se llama import serial
#para abrir el puerto serial, se usa la funcion serial.Serial() 
# si cambia el puerto, cambia la programa, si cambia la velocidad, cambia la velocidad de comunicacion
#puerto = serial.Serial("COM10", 115200) #COM10 es el puerto, 115200 es la velocidad de comunicacion
#puerto.write(..) ## en writte solo envia 
## encode, debemos convertir los bytes, enviamos str, usamos encode para convertir a bytes, y luego enviamos
# puerto.write((mensaje + "\n").encode()) ## enviamos el mensaje, y luego un salto de linea, y luego convertimos a bytes
## el salto de linea, determina en que punto termina el mensaje
# de la esp  Pyton, readline, lee linea por line
#definimos una variable y luego puerto.readline 
#decode es de la tarjeta a el programa, convertimos de bytes a str
#dato = puerto.readline().decode()
## como usar los datos, strip, elimina los espacios en blanco, espacios , demas
#dato=puerto.readline().decode().strip() ## eliminamos los espacios en blanco, y demas
## lo convertimos a float, o lo que nesescitems
#sleep es una pausa 

from machine import Pin
from time import sleep

led = Pin (18, Pin.OUT)

while True:
    led.value(1)
    sleep(1)

    led.value(0)
    sleep(1)

# para subirlos, abro terminal, escribo python -m mpremote connect COMM11 run 15_ESP21.py

##python -m mpremote connect COMM11 fs ls 15_ESP21.py :main.py
