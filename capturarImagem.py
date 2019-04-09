from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.rotation = 180

camera.start_preview()

sleep(2)

camera.capture("/home/pi/Desktop/IMG.jpg")
