import RPi.GPIO as GPIO
import datetime
import locale
from time import sleep
from picamera import PiCamera

#Localização PT-BR
locale.setlocale(locale.LC_ALL, str("pt_BR.UTF-8"))

#Utiliza a numeração física dos pinos GPIO
GPIO.setmode(GPIO.BOARD)

camera = PiCamera()

#Rotaciona a Imagem 180 graus
camera.rotation = 180

#Pino do botao que aciona a camera
pinBotCam = 12

i = 1

GPIO.setup(pinBotCam, GPIO.IN, pull_up_down=GPIO.PUD_UP)

anterior = True

while True:
    bot_cam = GPIO.input(pinBotCam)
    if bot_cam == False and anterior == True:
        print("Botao Apertado")
        
        #pega a data atual
        now = datetime.datetime.now().strftime("%B %d, %Y\n%H:%M")
                                               
        camera.start_preview()
                                               
        #escreve a data atual na imagem                                       
        camera.annotate_text = now
                                               
        sleep(2)
        camera.capture("/home/pi/Desktop/imagem%s.jpg" % i)
        print("Imagem capturada")
        i+=1
    anterior = bot_cam
