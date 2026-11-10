from machine import Pin, time_pulse_us ##toma un tiempo que dura un pulso 
from time import sleep, sleep_us

trig = Pin(18, Pin.OUT) #pin de salida
echo = Pin(19, Pin.IN) #pin de entrada , usan milisegundos 

while True:
    trig.value(0) #apaga el pin de salida
    sleep_us(2) #espera 2 microsegundos

    trig.value(1) #enciende el pin de salida        
    sleep_us(10) #espera 10 microsegundos
    trig.value(0) #apaga el pin de salida

    tiempo=time_pulse_us(echo, 1,30000) #espera a que el pin de entrada se ponga en alto, y mide el tiempo que dura en alto

    if tiempo > 0:
        distancia = tiempo /58  ## universal en cm 
        print(round(distancia, 1)) #redondea a 1 decimal
    else: 
        print("sin medicion valida")

sleep(1) #espera 1 segundo

