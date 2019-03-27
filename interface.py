from tkinter import *
from paramiko import SSHClient
import paramiko
import time

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

        self.quintoContainer = Frame(master)
        self.quintoContainer["padx"] = 20
        self.quintoContainer.pack()

        self.sextoContainer = Frame(master)
        self.sextoContainer["pady"] = 20
        self.sextoContainer.pack()
  
        self.titulo = Label(self.primeiroContainer, text="Porta Interativa")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()
  
        self.IPLabel = Label(self.segundoContainer,text="IP", font=self.fontePadrao)
        self.IPLabel.pack(side=LEFT)
  
        self.IP = Entry(self.segundoContainer)
        self.IP["width"] = 30
        self.IP["font"] = self.fontePadrao
        self.IP.pack(side=LEFT)

        self.usuarioLabel = Label(self.terceiroContainer,text="Usuário", font=self.fontePadrao)
        self.usuarioLabel.pack(side=LEFT)
  
        self.usuario = Entry(self.terceiroContainer)
        self.usuario["width"] = 26
        self.usuario["font"] = self.fontePadrao
        self.usuario.pack(side=LEFT)

        self.senhaLabel = Label(self.quartoContainer,text="Senha", font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)
  
        self.senha = Entry(self.quartoContainer)
        self.senha["width"] = 27
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)
  
        self.mensagemLabel = Label(self.quintoContainer, text="Mensagem", font=self.fontePadrao)
        self.mensagemLabel.pack(side=LEFT)
  
        self.mensagem = Entry(self.quintoContainer)
        self.mensagem["width"] = 23
        self.mensagem["font"] = self.fontePadrao
        self.mensagem.pack(side=LEFT)

        self.aviso = Label(self.sextoContainer, text="", font=self.fontePadrao)
        self.aviso.pack()

        self.enviar = Button(self.sextoContainer)
        self.enviar["text"] = "Escrever"
        self.enviar["font"] = ("Calibri", "10")
        self.enviar["width"] = 12
        self.enviar["command"] = self.enviarMensagem
        self.enviar.pack(side=RIGHT)

        self.sair = Button(self.sextoContainer)
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Calibri", "10")
        self.sair["width"] = 12
        self.sair["command"] = self.primeiroContainer.quit
        self.sair.pack(side=LEFT)

    def enviarMensagem(self):
        ip = self.IP.get()
        mensagem = self.mensagem.get()
        usuario = self.usuario.get()
        senha = self.senha.get()
        self.aviso["text"] = "Mensagem Enviada!"

        comandoMsg = "python3 GIT/RaspberryPi/escreverMsg.py -m '" + mensagem + "'"

        ssh = SSH(ip, usuario, senha)
        ssh.exec_cmd(comandoMsg)

        #self.aviso["text"] = ""

class SSH:
    def __init__(self, ip, usuario, senha):
        self.ssh = SSHClient()
        self.ssh.load_system_host_keys()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(hostname=ip,username=usuario,password=senha)
 
    def exec_cmd(self,cmd):
        stdin,stdout,stderr = self.ssh.exec_command(cmd)
        if(stderr.channel.recv_exit_status() != 0):
            print(stderr.read())
        else:
            print(stdout.read())

root = Tk()
Application(root)
root.mainloop()