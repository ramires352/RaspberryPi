# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import datetime
import locale
import os
import I2C_LCD_driver
import time
from time import sleep
from picamera import PiCamera


#Localização PT-BR
#A localização pt-BR buga para escrever caractere especial na imagem, por exemplo "março"
#locale.setlocale(locale.LC_ALL, str("pt_BR.UTF-8"))

#Utiliza a numeração física dos pinos GPIO
GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)

camera = PiCamera()
display = I2C_LCD_driver.lcd()

#Rotaciona a Imagem 180 graus
camera.rotation = 180

#Pino do botao que aciona a camera
pinBotCam = 12

pinRecTimeUP = 35
pinRecTimeDOWN = 37
pinLedAmarelo = 40
pinLedVermelho = 38
pinLedVerde = 36


#Diretorio das mensagens
msgDir = "/home/pi/Desktop/Mensagens/"

GPIO.setup(pinBotCam, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pinRecTimeUP, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pinRecTimeDOWN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pinLedAmarelo, GPIO.OUT)
GPIO.setup(pinLedVermelho, GPIO.OUT)
GPIO.setup(pinLedVerde, GPIO.OUT)

estadoAntBotCam = True
estadoAntBotRecUP = True
estadoAntBotRecDOWN = True

#Tempo inicial de gravacao (segundos)
recTime = 10

display.lcd_display_string("Porta Interativa",1,2)
display.lcd_display_string("Tempo: %is" % recTime,4,0)

#intervalo para limpar a linha 3 do display (segundos)
intervalo = 2

t1 = 0


def capturarImagem(path, info):
    display.lcd_display_string("Capturando Imagem...",2,0)
        
    GPIO.output(pinLedAmarelo, GPIO.HIGH)
    
    camera.start_preview()
                                               
    #escreve a data atual na imagem                                       
    camera.annotate_text = info
                                               
    sleep(2)
    
    camera.capture(path + ".jpg")
    
    limparLinha(2)
    display.lcd_display_string("Imagem Caputurada!",2,0)
    
    GPIO.output(pinLedAmarelo, GPIO.LOW)
    
    sleep(2)
    limparLinha(2)
    
def gravarAudio(path, recTime):
    display.lcd_display_string("Gravando Audio...",2,0)
    
    GPIO.output(pinLedVermelho, GPIO.HIGH)
    
    os.system("arecord -D hw:1,0 -d " + str(recTime) + " -f cd " + path + ".wav -c 1")
    
    limparLinha(2)
    display.lcd_display_string("Audio Gravado!",2,0)
    
    GPIO.output(pinLedVermelho, GPIO.LOW)
    
    sleep(2)
    limparLinha(2)

def limparLinha(linha):
    display.lcd_display_string(" "*20,linha,0)

while True:
    t0 = time.time()
    
    estadoBotCam = GPIO.input(pinBotCam)
    if estadoBotCam == False and estadoAntBotCam == True:
        #pega a data atual
        info = datetime.datetime.now().strftime("%B %d, %Y\n%H:%M")
        
        dia = datetime.datetime.now().strftime("%d-%m-%Y/")
        hr = datetime.datetime.now().strftime("%H-%M-%S")
        
        path = msgDir + dia + hr + "/" + hr
        
        #Verifica se ja existe um pasta com o dia
        if not os.path.exists(msgDir + dia):
            os.makedirs(msgDir + dia)
            
        #Verifica se ja existe uma pasta com a hora
        if not os.path.exists(msgDir + dia + "/" + hr):
            os.makedirs(msgDir + dia + "/" + hr)
            
        capturarImagem(path, info)
        gravarAudio(path, recTime)
        
        limparLinha(2)
        display.lcd_display_string("Mensagem Gravada!",2,0)
        
        GPIO.output(pinLedVerde, GPIO.HIGH)
        sleep(2)
        GPIO.output(pinLedVerde, GPIO.LOW)
        
        limparLinha(2)
        recTime = 10
        display.lcd_display_string("Tempo: %is" % recTime,4,0)
    estadoAntBotCam = estadoBotCam
    
    estadoBotRecUP = GPIO.input(pinRecTimeUP)
    if estadoBotRecUP == False and estadoAntBotRecUP == True:
        recTime += 5
        if recTime == 35:
            t1 = time.time()
            recTime = 30
        display.lcd_display_string("Tempo: %is" % recTime,4,0)
    estadoAntBotRecUP = estadoBotRecUP
    
    estadoBotRecDOWN = GPIO.input(pinRecTimeDOWN)
    if estadoBotRecDOWN == False and estadoAntBotRecDOWN == True:
        recTime -= 5
        if recTime == 5:
            display.lcd_display_string("Tempo: 0%is" % recTime,4,0)
            
        elif recTime == 0:
            recTime = 5
            t1 = time.time()
            display.lcd_display_string("Tempo: 0%is" % recTime,4,0)
            
        else:
            display.lcd_display_string("Tempo: %is" % recTime,4,0)
            
    estadoAntBotRecDOWN = estadoBotRecDOWN
    
    sleep(0.1)