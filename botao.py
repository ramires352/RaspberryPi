import RPi.GPIO as GPIO
from time import sleep
from picamera import PiCamera

GPIO.setmode(GPIO.BCM)
camera = PiCamera()
camera.rotation = 180

i = 1


GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

anterior = True

while True:
    atual = GPIO.input(18)
    if atual == False and anterior == True:
        print("Botao Apertado")
        camera.start_preview()
        sleep(2)
        camera.capture("/home/pi/Desktop/imagem"+str(i)+".jpg")
        print("Imagem capturada")
        i+=1
    anterior = atual
