import socket
import _thread

s = socket.socket()

s.bind(('localhost',9999))

s.listen(100)
print('Waiting for connections')

usr=[]

def client(c, addr,name):
 
    while True:
            try:
                message = c.recv(2048).decode()
                if message:
                     print ('\n' + message)
                     msg= ">>>" + message
                     msg_send(msg, c)
                else:
                    remove(c)
            except:
                continue
def msg_send(msg, c):
    for i in usr:
        if i!=c:
            try:
                i.send(bytes(msg, 'utf-8'))
            except:
                i.close()
                remove(i)

def remove(c):
    if c  in usr:
        usr.remove(c)

while True:

    c, addr = s.accept()
    name=c.recv(1024).decode()
    usr.append(c)
    print("Welcome to the chat",name)
    print(usr)
    c.send(bytes("Welcome to the chat!!",'utf-8'))
    _thread.start_new_thread(client,(c,addr,name))
    print(len(usr))
c.close()
s.close()

