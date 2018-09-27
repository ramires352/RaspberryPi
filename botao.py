import RPi.GPIO as GPIO
import datetime
import locale
import os
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

#Diretorio das mensagens
msgDir = "/home/pi/Desktop/Mensagens/"

GPIO.setup(pinBotCam, GPIO.IN, pull_up_down=GPIO.PUD_UP)

estadoAntBotCam = True

def capturarImagem():
    print("Botao Apertado")
        
    #pega a data atual
    info = datetime.datetime.now().strftime("%B %d, %Y\n%H:%M")
        
    dia = datetime.datetime.now().strftime("%d-%m-%Y/")
    hr = datetime.datetime.now().strftime("%H-%M-%S")
        
    #Verifica se ja existe um pasta com o dia
    if not os.path.exists(msgDir + dia):
        os.makedirs(msgDir + dia)
        
    #Verifica se ja existe uma pasta com a hora
    if not os.path.exists(msgDir + dia + "/" + hr):
        os.makedirs(msgDir + dia + "/" + hr)
            
    camera.start_preview()
                                               
    #escreve a data atual na imagem                                       
    camera.annotate_text = info
                                               
    sleep(2)
    
    camera.capture(msgDir + dia + hr + "/" + hr + ".jpg")
    print("Imagem capturada")
    
    

while True:
    estadoBotCam = GPIO.input(pinBotCam)
    
    if estadoBotCam == False and estadoAntBotCam == True:
        capturarImagem()
        
    estadoAntBotCam = estadoBotCam