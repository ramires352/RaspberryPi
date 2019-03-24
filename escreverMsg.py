#Código responsável por receber uma mensagem por parametro e mostrar no display
import I2C_LCD_driver
import sys, getopt

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hm:")
    except getopt.GetoptError:
        print("escreverMsg.py -m <menssagem>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print("escreverMsg.py -m <menssagem>")
            sys.exit()
        elif opt == "-m":
            mensagem = arg
    
    display = I2C_LCD_driver.lcd()

    #Escrever mensagem no display
    display.lcd_display_string(mensagem, 3, 0)
    #Esperar 5 segundos
    sleep(5)
    #Apagar a mensagem do display
    display.lcd_display_string(" "*20,3,0)

if __name__ == "__main__":
    main(sys.argv[1:])