import paramiko
import cmd
import time
import sys

buff = ''
resp = ''

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.11.8', username='pi', password='ramires2313')
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
chan = ssh.invoke_shell()

# turn off paging
chan.send('terminal length 0\n')
time.sleep(1)
resp = chan.recv(9999)
output = resp.decode('utf-8').split(',')
#print (''.join(output))

# Display output of first command
chan.send('cd GIT/RaspberryPi')
chan.send('\n')
time.sleep(1)
resp = chan.recv(9999)
output = resp.decode('utf-8').split(',')
print (''.join(output))

# Display output of second command
chan.send('ls')
chan.send('\n')
time.sleep(1)
resp = chan.recv(9999)
output = resp.decode('utf-8').split(',')
print (''.join(output))

ssh.close()  