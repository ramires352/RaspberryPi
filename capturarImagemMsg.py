from picamera import PiCamera
from time import sleep
import argparse

def main():
    parser = argparse.ArgumentParser(description="Tira uma foto na hora da gravação da mensagem.")
    parser.add_argument("-p","--path",help="Caminho onde a imagem será salva.")
    parser.add_argument("-i","--info",help="Informação de data que será escrita na imagem.")

    args = parser.parse_args()

    path = args.path
    info = args.info

    camera = PiCamera()

    camera.rotation = 180

    camera.start_preview()

    camera.annotate_text = info

    sleep(2)

    camera.capture(path + ".jpg")

if __name__ == "__main__":
    main()