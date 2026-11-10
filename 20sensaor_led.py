from machine import Pin, time_pulse_us #determina el tiempo que tarda en recibir la señal de retorno del sensor ultrasónico
from time import sleep, sleep_us #importando los pines que se estan utilizando
import sys #importando la libreria sys, para poder leer el mensaje enviado desde la terminal
import select #importando la libreria select, para poder leer el mensaje enviado desde la terminal

trig=Pin(18, Pin.OUT) #PIN en mayuscula, GPI18, salida digital
trig=Pin(19, Pin.IN) #PIN en mayuscula, GPI19, entrada digital
trig=Pin(23, Pin.OUT) #PIN en mayuscula, GPI23, salida digital

led.value(0) # se apaga el led al inicio del programa

while True: #ciclo infinito
    trig.value(0) # se pone en 0 el pin de salida, para que no haya señal
    sleep_us(2) # se espera 2 microsegundos, para que el pin de salida se estabilice

    trig.value(1) # se pone en 1 el pin de salida, para que haya señal
    sleep_us(10) # se espera 10 microsegundos, para que el pin
    trig.value(0) # se pone en 0 el pin de salida, para que no haya señal

    tiempo= time_pulse_us(echo, 1,30000) # se mide el tiempo que tarda en recibir la señal de retorno del sensor ultrasónico, en microsegundos, y se guarda en la variable tiempo

    if tiempo < 0: # si el tiempo es menor a 0, significa que no se recibió la señal de retorno del sensor ultrasónico
        distance=tiempo/58 # se calcula la distancia en cm, dividiendo el tiempo entre 58
        print(round(distance,1)) # se imprime la distancia en cm, redondeada a 1 decimal

    if select.select([sys.stdin], [], [], 0.0)[0]: # si hay un mensaje enviado desde la terminal
        comando= sys.stdin.readline().strip() # se lee el mensaje enviado desde la terminal y elimina el salto de línea al final

        if comando == "ENCENDER":
            led.value(1) # enciende el led

        elif comando == "APAGAR":
            led.value(0) # apaga el led
sleep(0.5) # se espera 0.5 segundo, para que el sensor ultrasónico se estabilice y no se sature de mediciones