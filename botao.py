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

pinRecTimeUP = 35
pinRecTimeDOWN = 37
pinLedAmarelo = 40
pinLedVermelho = 38


#Diretorio das mensagens
msgDir = "/home/pi/Desktop/Mensagens/"

GPIO.setup(pinBotCam, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pinRecTimeUP, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pinRecTimeDOWN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pinLedAmarelo, GPIO.OUT)
GPIO.setup(pinLedVermelho, GPIO.OUT)

estadoAntBotCam = True
estadoAntBotRecUP = True
estadoAntBotRecDOWN = True

#Tempo inicial de gravacao (segundos)
recTime = 10

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
        
    GPIO.output(pinLedAmarelo, GPIO.HIGH)
    
    camera.start_preview()
                                               
    #escreve a data atual na imagem                                       
    camera.annotate_text = info
                                               
    sleep(2)
    
    camera.capture(msgDir + dia + hr + "/" + hr + ".jpg")
    print("Imagem capturada")
    
    GPIO.output(pinLedAmarelo, GPIO.LOW)
    
    

while True:
    estadoBotCam = GPIO.input(pinBotCam)
    if estadoBotCam == False and estadoAntBotCam == True:
        capturarImagem()
        print("botao camera")
    estadoAntBotCam = estadoBotCam
    
    estadoBotRecUP = GPIO.input(pinRecTimeUP)
    if estadoBotRecUP == False and estadoAntBotRecUP == True:
        recTime += 5
        if recTime == 35:
            print("tempo maximo de 30 segundos")
            recTime = 30
        print("Tempo de gravação: %i" % recTime)
    estadoAntBotRecUP = estadoBotRecUP
    
    estadoBotRecDOWN = GPIO.input(pinRecTimeDOWN)
    if estadoBotRecDOWN == False and estadoAntBotRecDOWN == True:
        recTime -= 5
        if recTime == 0:
            print("tempo minimo de 5 segundos")
            recTime = 5
        print("Tempo de gravação: %i" % recTime)
    estadoAntBotRecDOWN = estadoBotRecDOWN
    
    sleep(0.1)