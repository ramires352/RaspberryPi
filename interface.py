from tkinter import *
from paramiko import SSHClient
import paramiko

class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()
  
        self.segundoContainer = Frame(master)
        self.segundoContainer["pady"] = 20
        self.segundoContainer.pack()
  
        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()
  
        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()
  
        self.titulo = Label(self.primeiroContainer, text="Porta Interativa")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()
  
        self.IPLabel = Label(self.segundoContainer,text="IP", font=self.fontePadrao)
        self.IPLabel.pack(side=LEFT)
  
        self.IP = Entry(self.segundoContainer)
        self.IP["width"] = 30
        self.IP["font"] = self.fontePadrao
        self.IP.pack(side=LEFT)
  
        self.mensagemLabel = Label(self.terceiroContainer, text="Mensagem", font=self.fontePadrao)
        self.mensagemLabel.pack(side=LEFT)
  
        self.mensagem = Entry(self.terceiroContainer)
        self.mensagem["width"] = 23
        self.mensagem["font"] = self.fontePadrao
        self.mensagem.pack(side=LEFT)

        self.aviso = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.aviso.pack()

        self.enviar = Button(self.quartoContainer)
        self.enviar["text"] = "Escrever"
        self.enviar["font"] = ("Calibri", "10")
        self.enviar["width"] = 12
        self.enviar["command"] = self.enviarMensagem
        self.enviar.pack(side=RIGHT)

        self.sair = Button(self.quartoContainer)
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Calibri", "10")
        self.sair["width"] = 12
        self.sair["command"] = self.primeiroContainer.quit
        self.sair.pack(side=LEFT)

    def enviarMensagem(self):
        ip = self.IP.get()
        mensagem = self.mensagem.get()
        self.aviso["text"] = "Mensagem Enviada!"
        #Configurar o SSH para conectar ao RaspberryPi
        buff = ''
        resp = ''
        
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, username='pi', password='ramires2313')
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        chan = ssh.invoke_shell()

        comandoMsg = "escreverMsg.py -m " + mensagem

        # turn off paging
        chan.send('terminal length 0\n')
        #time.sleep(1)
        resp = chan.recv(9999)
        output = resp.decode('utf-8').split(',')
        #print (''.join(output))

        # Display output of first command
        chan.send('cd GIT/RaspberryPi')
        chan.send('\n')
        #time.sleep(1)
        resp = chan.recv(9999)
        output = resp.decode('utf-8').split(',')
        print (''.join(output))

        # Display output of second command
        chan.send(comandoMsg)
        chan.send('\n')
        #time.sleep(1)
        resp = chan.recv(9999)
        output = resp.decode('utf-8').split(',')
        print (''.join(output))

        ssh.close()

root = Tk()
Application(root)
root.mainloop()