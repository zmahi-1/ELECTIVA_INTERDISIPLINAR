from machine import Pin
import sys 

led = Pin(18, Pin.OUT) #PIN en mayuscula, GPIO18, salida digital

while True: #ciclo infinito
    mensaje= sys.stdin.readline().strip() #lee el mensaje enviado desde la terminal y elimina el salto de línea al final

    if mensaje == "ENCENDER":
        led.value(1) # enciende el led
        
    elif mensaje == "APAGAR":
        led.value(0) # apaga el led