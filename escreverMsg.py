#Código responsável por receber uma mensagem por parametro e mostrar no display
import I2C_LCD_driver
import sys, getopt
from time import sleep

display = I2C_LCD_driver.lcd()

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hm:d:")
    except getopt.GetoptError:
        print("escreverMsg.py -m <menssagem>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print("escreverMsg.py -m <menssagem>")
            sys.exit()
        elif opt == "-m":
            mensagem = arg
        elif opt == "-d":
            tempo = arg
    
    #Escrever mensagem no display
    display.lcd_display_string(mensagem, 3, 0)
    #Esperar tempo minutos
    sleep(int(tempo)*60)
    #Apagar a mensagem do display
    display.lcd_display_string(" "*20,3,0)

if __name__ == "__main__":
    display.lcd_display_string("Porta Interativa",1,2)
    display.lcd_display_string("Tempo: 10s",4,0)
    main(sys.argv[1:])