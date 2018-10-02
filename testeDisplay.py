import I2C_LCD_driver
import socket
import fcntl
import struct
import time

lcdi2c = I2C_LCD_driver.lcd()

lcdi2c.lcd_display_string("Testando",1,4)
lcdi2c.lcd_display_string("Andre Verona", 2,0)
lcdi2c.lcd_display_string("Raul Ramires",3,0)
lcdi2c.lcd_display_string("Porta Interativa",4,0)