import socket
import threading

c = socket.socket()

c.connect(('localhost',9999))
name=input("Enter your name: ")
c.send(bytes(name,'utf8'))
print(c.recv(1024).decode())

def recieve():
    msg=c.recv(1024).decode()
    print(msg)

def sendmsg(name):
    msg=input(f"{name}>>")
    msg1=f'\n{name}>> '+msg
    c.send(bytes(msg1,'utf-8'))


while True:
    rec=threading.Thread(target=recieve)
    rec.start()

    snd=threading.Thread(target=sendmsg(name))
    snd.start()
    



c.close()



