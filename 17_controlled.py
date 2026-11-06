import serial
from time import sleep

puerto=serial.Serial("COM10", 115200) 
sleep(3) 
puerto.reset_input_buffer() 

while True: #ciclo infinito
    mensaje=input("Digite ENCENDER o APAGAR para controlar el led: ") 
    puerto.write((mensaje+ "\n").encode())

    python -m pip install --upgrade mpremote esptoll pyserial